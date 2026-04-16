#!/usr/bin/env python3
"""
校验单次 /side-hustle 产出的推荐报告结构。

用法:
    python3 scripts/validate.py results/2026-04-16_designer_figma/recommendations.md

退出码:
    0  全部通过
    1  有硬性失败
    2  有警告（结构 OK 但评分/内容存疑）

校验内容:
    - 推荐方向数量在 5-10 之间
    - 每个方向包含 6 个维度分数，每项 1-5，总分与各项之和一致
    - 每个方向有"匹配理由"和"风险"字段
    - 推荐按总分降序排列
    - 方向名称不是笼统词（"做自媒体"、"搞电商"等）
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

GENERIC_DIRECTION_WORDS = [
    "做自媒体", "搞电商", "做内容", "做副业", "搞副业",
    "做生意", "做电商", "做主播",
]

DIMENSION_NAMES = [
    "技能匹配", "时间适配", "启动成本",
    "收入天花板", "冷启动", "可持续性",
]


@dataclass
class Direction:
    rank: int | None
    name: str
    total: int | None
    dim_scores: dict[str, int] = field(default_factory=dict)
    reason: str = ""
    risk: str = ""
    raw: str = ""


@dataclass
class Report:
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    directions: list[Direction] = field(default_factory=list)

    def fail(self, msg: str) -> None:
        self.failures.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def parse_directions(text: str) -> list[Direction]:
    """按 '## ' 或 '### ' 分块；每块至少要有一个 '#N' 或 '总分' 标志。"""
    blocks = re.split(r"(?m)^(?=#{2,3}\s+#\d+)", text)
    directions: list[Direction] = []
    for block in blocks:
        if not re.search(r"#\d+", block):
            continue
        d = parse_one(block)
        if d is not None:
            directions.append(d)
    return directions


def parse_one(block: str) -> Direction | None:
    rank_match = re.search(r"#(\d+)\b", block)
    rank = int(rank_match.group(1)) if rank_match else None

    name_match = re.search(r"#\d+\s+([^\n│|]+?)(?:\s{2,}|\s*\||\s*│|\n)", block)
    name = name_match.group(1).strip() if name_match else ""

    total_match = re.search(r"(\d+)\s*/\s*30\s*分", block)
    total = int(total_match.group(1)) if total_match else None

    dim_scores: dict[str, int] = {}
    for dim in DIMENSION_NAMES:
        m = re.search(rf"{dim}\D{{0,10}}(\d)(?!\d)", block)
        if m:
            dim_scores[dim] = int(m.group(1))

    reason_m = re.search(r"匹配理由[：:]\s*([^\n│]+)", block)
    risk_m = re.search(r"(?:风险提示|风险)[：:]\s*([^\n│]+)", block)

    return Direction(
        rank=rank,
        name=name,
        total=total,
        dim_scores=dim_scores,
        reason=reason_m.group(1).strip() if reason_m else "",
        risk=risk_m.group(1).strip() if risk_m else "",
        raw=block,
    )


def validate(path: Path) -> Report:
    report = Report()
    text = path.read_text(encoding="utf-8")

    directions = parse_directions(text)
    report.directions = directions

    n = len(directions)
    if n < 5:
        report.fail(f"推荐方向数量过少: {n}（至少 5 个）")
    elif n > 10:
        report.warn(f"推荐方向数量偏多: {n}（超过 10 个可能稀释优质推荐）")

    for d in directions:
        label = f"#{d.rank} {d.name or '(无名)'}"

        if not d.name:
            report.fail(f"{label}: 缺少方向名称")
        else:
            for bad in GENERIC_DIRECTION_WORDS:
                if bad in d.name:
                    report.fail(f"{label}: 方向名称过于笼统（命中 '{bad}'）")

        for dim in DIMENSION_NAMES:
            score = d.dim_scores.get(dim)
            if score is None:
                report.fail(f"{label}: 缺少维度 '{dim}' 的分数")
            elif not 1 <= score <= 5:
                report.fail(f"{label}: 维度 '{dim}' 分数越界 ({score})")

        if d.total is not None and len(d.dim_scores) == 6:
            s = sum(d.dim_scores.values())
            if s != d.total:
                report.fail(
                    f"{label}: 总分 {d.total} 与各维度之和 {s} 不一致"
                )

        if not d.reason:
            report.fail(f"{label}: 缺少 '匹配理由'")
        if not d.risk:
            report.warn(f"{label}: 缺少 '风险提示'")

    totals = [d.total for d in directions if d.total is not None]
    if totals != sorted(totals, reverse=True):
        report.fail("推荐未按总分降序排列")

    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("recommendations", type=Path)
    args = parser.parse_args()

    if not args.recommendations.exists():
        print(f"文件不存在: {args.recommendations}", file=sys.stderr)
        return 1

    report = validate(args.recommendations)

    print(f"校验: {args.recommendations}")
    print(f"解析出 {len(report.directions)} 个方向")
    print()

    if report.failures:
        print("❌ 失败项:")
        for msg in report.failures:
            print(f"  - {msg}")
    if report.warnings:
        print("⚠️  警告项:")
        for msg in report.warnings:
            print(f"  - {msg}")

    if not report.failures and not report.warnings:
        print("✅ 全部通过")
        return 0
    if report.failures:
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())

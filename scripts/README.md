# 测试脚本

这些脚本用于自测 `/side-hustle` 的输出质量，尤其在修改 `SKILL.md`、`prompts/` 或 `knowledge/categories.md` 之后。

## 目录结构

```
scripts/
├── fixtures/
│   └── profiles/           # 测试画像（不同典型用户）
│       ├── designer.md
│       ├── backend_engineer.md
│       └── stay_at_home_parent.md
└── validate.py             # 校验 recommendations.md 的结构和内容
```

## 使用方式

### 1. 选一个画像，跑一次完整流程

在 Claude Code 里（安装了本 skill 之后）执行：

```
/side-hustle
```

当 agent 问画像时，把 `scripts/fixtures/profiles/designer.md` 的 **画像** 段落贴进去。输出会保存到 `results/{date}_{slug}/`。

### 2. 校验输出结构

```bash
python3 scripts/validate.py results/2026-04-16_designer_figma/recommendations.md
```

退出码：
- `0` — 全部通过
- `1` — 有硬性失败（格式错误、分数越界、推荐太少等）
- `2` — 有警告（风险字段缺失等，结构 OK）

### 3. 对照 fixture 的预期行为手动验收

每个 fixture 的 **预期行为** 段落列出了这个画像该/不该出现哪些方向。跑完后人工对照一下，能发现 validate.py 捕捉不到的语义问题（比如推荐了命中排除项的方向）。

## 后续规划

- [ ] 把预期行为写成机器可校验的 YAML（让 validate.py 能自动对照 fixture）
- [ ] 加 snapshot 测试：把某个 profile 的 output 存成 golden file，prompt 改动后 diff
- [ ] 加 `scripts/eval.py` 统计历次 `results/` 里推荐方向的分布，发现系统性偏好

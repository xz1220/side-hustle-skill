# 真实案例库

> 用于评分时做 grounding。WebSearch 之前应先查本库，WebSearch 应只补缺失。
> 被 `prompts/discovery.md` Phase 3 引用。

## 目的

WebSearch 的内容质量两极分化，SEO 污染严重。本库是经过人工核验的真实案例集合，用于：

1. **评分 grounding**：评分前先确认本库是否已有该方向的案例，优先使用本库数据
2. **反"头部案例偏见"**：每个方向尽量覆盖不同分位点（P50 中位数、P95 头部、失败复盘）
3. **引用透明化**：推荐报告里可直接链接到具体案例文件

## 案例选取原则

- **可溯源**：作者本人公开撰写或 IndieHackers Open Startups 自主公开 MRR
- **分布覆盖**：同一方向优先收录多个分位点（不只收头部）
- **包含失败**：不只讲成功路径，也收录失败/停滞案例
- **拒绝"月入十万"营销案例**：见 `source_trust.md` 红旗短语字典

## 案例文件 Schema

每个案例使用 YAML frontmatter + Markdown 叙述：

```yaml
---
slug: short-slug
name: 作者名或产品名
archetype: solo-saas | content-creator | freelance | ecom | ...
category: 对应 categories.md 中的方向
language: en | zh
start_date: YYYY-MM
first_revenue_date: YYYY-MM
current_revenue: $X/mo MRR 或 ¥X/月
distribution_position: P50 | P75 | P95 | failed
confidence: high | medium | low
source: URL
last_verified: YYYY-MM-DD
---

# {案例标题}

## Timeline
- YYYY-MM: 开始
- YYYY-MM: 里程碑
- ...

## 做对的事
- ...

## 做错的事
- ...

## 关键引语（作者本人原话）
> ...

## 评分启示（本库专用）
- 对 `{category}` 方向的收入天花板维度：...
- 对冷启动维度：...
- 对可持续性维度：...
```

## 当前案例索引

| Slug | 方向 | 分位 | 收入 | 置信度 |
|------|------|------|------|--------|
| [marc_lou](marc_lou.md) | 独立开发 AI SaaS（产品矩阵）| P99 | $100 万+/年 | high |
| [papermark](papermark.md) | 独立开发 SaaS（DocSend 替代）| P95 arc | $45k MRR | high |
| [plausible](plausible.md) | 独立开发 SaaS（Analytics）| P99 | $258k MRR | high |
| [resume_tool_35yo](resume_tool_35yo.md) | 独立开发工具（简历）| **P50** | ¥3000/月 | high |
| [systemdailynotes](systemdailynotes.md) | 小报童技术付费专栏 | P75 | ¥几千-数万一次性 | medium |
| [feiba_800subs](feiba_800subs.md) | 小报童 7 天 800 订阅 | P75 | ¥6k+ 首周 | medium |
| [samuel_rondot](samuel_rondot.md) | 独立开发产品矩阵 | P95 | $28k/月 | medium |

## 维护

- 每次跑 `/side-hustle` 遇到新的真实案例，补录到本库
- 案例 URL 失效或信息过期（`last_verified` > 6 月）→ 重新核验或下架
- 新方向进入品类库时，至少配 1 个 P50 案例、1 个 P95 案例

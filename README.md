<div align="center">

# 副业.skill

> *"别再花钱买课了，让 AI 帮你找到真正适合你的副业。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

想做副业，但不知道从哪开始？<br>
花了几千块买课，学完发现不适合自己？<br>
看了一堆"月入过万"的帖子，越看越焦虑？<br>

**别猜了。用 AI 帮你系统分析，找到真正适合你的副业方向。**

<br>

输入你的技能、时间、资源和兴趣<br>
AI Agent 并发搜索、交叉评估、量化打分<br>
给你一份**个性化的副业推荐报告**，而不是千篇一律的"做自媒体"

[快速开始](#安装) · [使用方法](#使用) · [效果示例](#效果示例) · [评分体系](#评分体系) · [详细安装说明](INSTALL.md) · [**English**](README_EN.md)

</div>

---

## 它能做什么

| 步骤 | 说明 |
|------|------|
| **1. 了解你** | 通过结构化对话，快速建立你的个人画像（技能、时间、资源、兴趣、约束） |
| **2. 帮你找** | 基于你的画像，AI Agent 并发搜索和分析适合你的副业方向 |
| **3. 帮你选** | 按 6 个维度量化打分，给出排序推荐 + 每个方向的优劣分析 |
| **4. 帮你起步** | 对你感兴趣的方向，生成一份冷启动 checklist |

---

## 安装

### Claude Code

```bash
# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/xz1220/side-hustle-skill .claude/skills/side-hustle

# 或安装到全局（所有项目都能用）
git clone https://github.com/xz1220/side-hustle-skill ~/.claude/skills/side-hustle
```

### OpenClaw

```bash
git clone https://github.com/xz1220/side-hustle-skill ~/.openclaw/workspace/skills/side-hustle
```

重启 session 后输入 `/side-hustle` 即可启动。

> 详细安装说明见 [INSTALL.md](INSTALL.md)

---

## 使用

在 Claude Code 中输入：

```
/side-hustle
```

按提示回答几个问题，AI 会帮你完成剩下的事。

### 命令列表

| 命令 | 说明 |
|------|------|
| `/side-hustle` | 启动完整流程：画像 → 搜索 → 评分 → 推荐 |
| `/side-hustle-quick` | 快速模式：跳过深度画像，直接基于一句话描述推荐 |
| `/side-hustle-score {方向}` | 对单个副业方向做深度评分分析 |
| `/side-hustle-kickstart {方向}` | 对某个方向生成冷启动 checklist |
| `/side-hustle-history` | 查看历史推荐记录 |

---

## 效果示例

### 画像阶段

```
AI  > 先聊聊你的情况，我问你几个问题：
    >
    > 1. 你现在做什么工作？（职位/行业）
    > 2. 你擅长什么？不限于工作技能，生活技能也算
    > 3. 每周能拿出多少小时做副业？
    > 4. 有没有启动资金预算？（0 也完全没问题）
    > 5. 有什么是你绝对不想做的？

用户 > 我是一个UI设计师，擅长Figma和插画
    > 周末两天大概有10小时
    > 没什么预算，0启动
    > 不想做直播，社恐
```

### 推荐阶段

```
AI  > 基于你的画像，我找到了 8 个方向，评分排序如下：
    >
    > ## #1 Figma 模板/UI Kit 售卖  25/30 分
    > 匹配理由：直接变现现有技能，无需露脸，零启动成本
    > 冷启动第一步：在 Gumroad/小红书 发 3 套免费模板引流
    >
    > ## #2 插画约稿（小红书/闲鱼）  23/30 分
    > 匹配理由：插画技能直接变现，社恐友好（线上沟通）
    > 冷启动第一步：闲鱼挂 3 个不同风格的样品，定价 50-200
    >
    > ## #3 设计类自媒体（小红书图文）  21/30 分
    > 匹配理由：不需要直播，图文形式社恐友好
    > 风险提示：起号周期长，前 3 个月可能零收入
    >
    > ...
    >
    > 想深入了解哪个方向？我可以帮你做冷启动规划。
```

---

## 评分体系

每个副业方向按 6 个维度打分，满分 30 分：

| 维度 | 1 分 | 5 分 |
|------|------|------|
| **技能匹配度** | 需要从零学起 | 直接用现有技能 |
| **时间适配度** | 需要全职投入 | 碎片时间可做 |
| **启动成本** | 需要大额投入 | 零成本启动 |
| **收入天花板** | 月入几百封顶 | 可规模化到万+ |
| **冷启动难度** | 需要大量积累 | 一周内能出第一单 |
| **可持续性** | 一次性收入 | 可复利增长 |

**推荐阈值：**
- 25-30：强烈推荐，立刻开始
- 20-24：值得尝试，注意风险点
- 15-19：有潜力但门槛较高
- <15：不推荐，匹配度低

---

## 项目结构

```
side-hustle-skill/
├── SKILL.md              # Skill 入口（AgentSkills 标准 frontmatter）
├── prompts/              # Prompt 模板
│   ├── intake.md         #   用户画像录入引导
│   ├── discovery.md      #   副业方向搜索与分析方法论
│   ├── scorer.md         #   6 维度评分标准与规则
│   └── kickstart.md      #   冷启动 checklist 生成
├── knowledge/            # 知识库
│   └── categories.md     #   副业品类库与元数据
├── results/              # 用户的推荐结果存档（gitignored）
├── INSTALL.md            # 详细安装说明
├── README_EN.md          # English documentation
└── LICENSE
```

---

## 隐私说明

- 所有对话和分析均在本地完成
- 不收集、不上传任何个人信息
- 推荐结果仅保存在你本地的 `results/` 目录
- 你可以随时删除所有数据

---

## 常见问题

**Q: 和直接问 ChatGPT "我该做什么副业" 有什么区别？**

A: ChatGPT 给你的是通用建议。副业.skill 会通过结构化画像深度了解你，然后用量化评分体系做交叉评估——不是拍脑袋推荐，是系统分析。

**Q: 需要付费吗？**

A: 不需要。开源免费。你只需要有 Claude Code 或 OpenClaw 的使用权限。

**Q: 支持英文吗？**

A: 支持。Skill 会根据你第一条消息的语言自动切换。

---

## License

[MIT](LICENSE)

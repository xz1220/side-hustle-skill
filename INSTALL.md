# 副业.skill 安装说明

---

## 选择你的平台

### A. Claude Code（推荐）

本项目遵循官方 [AgentSkills](https://agentskills.io) 标准，整个 repo 就是 skill 目录。克隆到 Claude skills 目录即可：

```bash
# ⚠️ 必须在 git 仓库根目录执行！
cd $(git rev-parse --show-toplevel)

# 方式 1：安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/perkfly/side-hustle-skill .claude/skills/side-hustle

# 方式 2：安装到全局（所有项目都能用）
git clone https://github.com/perkfly/side-hustle-skill ~/.claude/skills/side-hustle
```

然后在 Claude Code 中说 `/side-hustle` 即可启动。

推荐结果默认写入 `./results/` 目录。

---

### B. OpenClaw

```bash
git clone https://github.com/perkfly/side-hustle-skill ~/.openclaw/workspace/skills/side-hustle
```

重启 OpenClaw session，说 `/side-hustle` 启动。

---

## 无需额外依赖

本 Skill 纯文本运行，不需要安装 Python 或其他依赖。

所有功能通过 Claude Code 内置的 Read、Write、WebSearch、WebFetch 工具完成。

---

## 快速验证

安装完成后，在 Claude Code 中输入：

```
/side-hustle-quick
```

输入一句话描述自己，如果能收到推荐结果，说明安装成功。

---

## 目录结构说明

```
side-hustle-skill/            ← clone 到 .claude/skills/side-hustle/
├── SKILL.md                  # Skill 入口（AgentSkills 标准 frontmatter）
├── prompts/                  # Prompt 模板
│   ├── intake.md             #   用户画像引导问题
│   ├── discovery.md          #   副业搜索方法论
│   ├── scorer.md             #   评分标准
│   └── kickstart.md          #   冷启动方案模板
├── knowledge/                # 知识库
│   └── categories.md         #   副业品类库
├── results/                  # 推荐结果存档（gitignored）
│   └── {date}_{slug}/
│       ├── profile.md        #   用户画像
│       ├── recommendations.md #  推荐报告
│       └── kickstart_*.md    #   冷启动方案
├── INSTALL.md                # 本文件
├── README_EN.md              # English docs
└── LICENSE
```

---

## 卸载

删除 skill 目录即可：

```bash
# 项目级安装
rm -rf .claude/skills/side-hustle

# 全局安装
rm -rf ~/.claude/skills/side-hustle
```

推荐结果在 `results/` 目录中，如需保留请先备份。

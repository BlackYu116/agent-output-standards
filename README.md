# Agent 语言与输出规范

让读者更快理解、判断和使用 Agent 的结果，同时保留事实、条件和不确定性。

这是一套面向不同 Agent 的表达技能，中文优先，原则可用于其他语言。核心规则不依赖模型、工具或操作系统；具体接入取决于宿主能否读取技能文件。它受 Karpathy 的[原帖](https://x.com/karpathy/status/2105819303471976479)、评论区和受控语言实践启发；不是 ASD-STE100 的翻译、官方实现或合规认证。

当前版本：**0.2.0-rc.1 · 2026-10-02**。这是待用户验收的候选版。尚未完成多模型、多语言或真实读者验证，不承诺在所有 Agent 上效果一致。

## 从哪里开始

| 你要做什么 | 读什么 |
| --- | --- |
| 让 Agent 使用规范 | [技能入口](skills/clear-output/SKILL.md) |
| 写作、改写、解释 | [语言标准](skills/clear-output/references/language.md) |
| 选择输出形式、交付成果 | [输出标准](skills/clear-output/references/output.md) |
| 给另一个 Agent 交接 | [交接约定](skills/clear-output/references/handoff.md) |
| 看数字、判断与人情味如何兼顾 | [十个典型场景](skills/clear-output/references/scenarios.md) |
| 看精确改写的边界 | [前后对照](skills/clear-output/references/examples.md) |
| 了解来源与取舍 | [原帖研究](research/2026-10-02-karpathy.md)、[表达设计](research/2026-10-02-communication-design.md) |
| 检验或修改规范 | [评估用例](evals/README.md)、[维护方法](CONTRIBUTING.md) |

## 四个关键决定

1. **清晰不能以失真为代价。** 改写保留条件、例外、数量、否定、概率和要求强度。不要把“可能”改成“会”。
2. **媒介按任务选。** 文字、表格、图解、交互页面、PDF、音频和视频各有用途。HTML 和视频不天然高于文字。
3. **数字直观，语言交代意义。** 保留重要数量与口径，用简短的解释帮助读者理解影响；体贴来自具体帮助，不靠套话或无依据的安慰。
4. **可检查不等于已理解。** 格式检查可以发现问题；只有内容核验和读者能否正确使用，才能说明沟通是否成功。

## Agent 接入

支持读取文件的 Agent，可以在任务中直接指定本仓库的 `skills/clear-output/SKILL.md`。入口会按需加载相邻 references；不要默认把研究笔记、全部例子和评估答案塞入上下文。

如使用支持 `SKILL.md` 的技能系统，把 **整个 `skills/clear-output/` 目录**复制到该工具配置的技能目录。保留 `references/`。发现路径和刷新方法以所在工具为准。本仓库不自动修改任何全局 Agent 设置。

如果只支持项目指令，可合并这一段到项目已有的指令文件，并把路径换成实际位置：

```text
涉及解释、研究交付、技术写作或结果汇报时，读取 <本仓库路径>/skills/clear-output/SKILL.md，并按任务加载所需参考。
以当前任务、事实完整性和已有接口约定为先。不要为套用规范增加交付物或改变输出格式。
```

只有路径说明而没有读取能力，不会自动生效。接入后用 [evals/cases.json](evals/cases.json) 中的一个相关任务验证实际输出。

## 本地检查

```sh
python3 scripts/check_repo.py
```

该命令只检查仓库文件、相对链接、技能入口和评估数据的基础结构，不检查事实、文风或模型行为。行为评估另见 evals。

维护时先记录一个实际误解，再修改最小规则和对应样例。不要把一次不喜欢的措辞升级成所有任务的禁令。

候选版已记录[四项基本行为检查及修订](evals/2026-10-02-v02-smoke.md)，不代表全部用例或多语言验收通过。

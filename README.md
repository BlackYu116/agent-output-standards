# Agent 语言与输出规范

让读者更快理解、判断和使用 Agent 的结果，同时保留事实、条件和不确定性。

这是一套面向不同 Agent 的表达技能，中文优先，原则可用于其他语言。核心规则不依赖模型、工具或操作系统；具体接入取决于宿主能否读取技能文件。它受 Karpathy 的[原帖](https://x.com/karpathy/status/2105819303471976479)、评论区和受控语言实践启发；不是 ASD-STE100 的翻译、官方实现或合规认证。

当前版本：**0.2.0-rc.2 · 2026-10-02**。这是公开候选版。尚未完成多模型、多语言或真实读者验证，不承诺在所有 Agent 上效果一致。

## 从 GitHub 直接使用

把下面这段发送给能读取网页的 Agent 或聊天助手即可：

```text
请读取并应用这个 Skill：
https://github.com/BlackYu116/agent-output-standards/blob/main/skills/clear-output/SKILL.md

如 GitHub 页面不便读取，使用原始文件：
https://raw.githubusercontent.com/BlackYu116/agent-output-standards/main/skills/clear-output/SKILL.md

在本次对话中遵守它的求真、目标纠偏、决策边界和表达原则。
按当前任务读取需要的 references，不要默认加载研究笔记或评估答案。
相对引用以 SKILL.md 所在目录为基准；原始参考文件位于：
https://raw.githubusercontent.com/BlackYu116/agent-output-standards/main/skills/clear-output/references/

如果无法访问这些文件，请明确说明，不要假称已加载。
不必复述规则，直接体现在后续回答和行动中。
```

这是本次对话的使用指令，不会自动安装技能，也不保证其他聊天继承。不能读取网页的助手，需要你粘贴技能正文，或上传完整技能目录；链接本身不会让它获得读取能力。

## 安装为可复用技能

支持从 GitHub 安装技能的 Agent，可指定：

- 仓库：`https://github.com/BlackYu116/agent-output-standards`
- 仓库内技能目录：`skills/clear-output`
- 技能名称：`clear-output`

也可以发送：

```text
请从 https://github.com/BlackYu116/agent-output-standards
安装 skills/clear-output 目录中的 clear-output 技能。
保留整个目录及 references，使用你所在平台支持的技能安装方式。
安装后确认入口和参考文件可读；不要改写我已有的其他规则。
如果不支持安装，请改为在本次对话读取并应用，不要声称已持久安装。
```

手动获取仓库：

```sh
git clone https://github.com/BlackYu116/agent-output-standards.git
```

把完整 `skills/clear-output/` 目录放入目标平台配置的技能目录，保留 `references/`。具体目录和刷新方法以平台为准。安装后的发现、触发和跨聊天生效范围由宿主决定；如果希望每次都使用，在该平台的常驻指令中注明“在回答与协作时应用 clear-output”。已有指令应合并，不要整份覆盖。

`main` 指向最新版本；需要固定行为时，将 GitHub 或 raw 链接中的 `main` 换成你选定的提交 SHA。更新技能后，再用 [评估用例](evals/cases.json) 的相关任务验证效果。

## 语言与兼容范围

技能用中文编写，原则适用于中文、英文和其他语言，实际输出跟随用户要求。它不依赖特定模型、API或本机绝对路径。能理解并读取这些指令的 Agent 可以使用；工具能力、安装机制和执行效果因平台而异。已有中英示例和有限行为检查，尚未完成多模型、多语言系统验证。

## 许可

本仓库原创内容以 [MIT License](LICENSE) 提供，可使用、修改和分发。所引用的第三方标准、文章和商标仍属于各自权利人；本仓库不包含 ASD-STE100 标准正文或官方词典，也不代表 Anthropic、ASD 或其他厂商的认证。

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

## 最高原则

说实话，以证据作判断，及时指出与已确认目标的冲突。涉及目标、范围、重要假设、成本、风险或对外承诺的未授权取舍，由用户决定后再执行；常规措辞和已授权范围内的工作继续完成，不事事追问。详见[目标与决策边界](skills/clear-output/references/decisions.md)。

## 四个关键决定

1. **清晰不能以失真为代价。** 改写保留条件、例外、数量、否定、概率和要求强度。不要把“可能”改成“会”。
2. **媒介按任务选。** 文字、表格、图解、交互页面、PDF、音频和视频各有用途。HTML 和视频不天然高于文字。
3. **数字直观，语言交代意义。** 保留重要数量与口径，用简短的解释帮助读者理解影响；体贴来自具体帮助，不靠套话或无依据的安慰。
4. **可检查不等于已理解。** 格式检查可以发现问题；只有内容核验和读者能否正确使用，才能说明沟通是否成功。

## 本地检查

```sh
python3 scripts/check_repo.py
```

该命令只检查仓库文件、相对链接、技能入口和评估数据的基础结构，不检查事实、文风或模型行为。行为评估另见 evals。

维护时先记录一个实际误解，再修改最小规则和对应样例。不要把一次不喜欢的措辞升级成所有任务的禁令。

候选版已记录[四项基本行为检查及修订](evals/2026-10-02-v02-smoke.md)，不代表全部用例或多语言验收通过。

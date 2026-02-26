# AI 原生研发范式：从“代码中心”到“文档驱动”的演进

## 0. 前言：让 Vibe Coding 可落地

> **TL;DR (太长不看版)**
>
> - **痛点 1：上下文腐烂 (Context Decay)**。随着对话进行，Feature 开发容易跑偏。超长上下文导致大模型注意力分散，代码质量直线下降。或者 New Chat 之后丢失原来的上下文，恢复起来费时费力。
> - **痛点 2：审查瘫痪 (Review Paralysis)**。**这是 AI 时代的各种“鬼故事”之源。** AI 能在几分钟内生成上万行代码。面对这种量级的 Diff，人类根本无法逐行 Review，导致“心里没底”不敢合并，或者盲目合并后埋下巨大隐患。
> - **痛点 3：维护断层 (Maintenance Gap)**。两个月后回来修 Bug，面对全是 AI 生成的陌生代码（且没有文档），不仅人看不懂，新的 AI 也因为缺乏背景知识而无法接手，导致“能跑但不敢动”。
> - **核心**：SDD (Spec-Driven Development) 不是传统文档的复辟，而是 **Vibe Coding 的“存档点” (Save Point)**。
> - **价值**：它用**文档锚点**锁定了上下文，让你在 **"Rerolling over debugging"**（重随优于调试）时，拥有稳定的“种子”。只有 Spec 稳了，代码才能真正成为“可抛弃的消耗品”

### 0.1 方法论的收益与代价（好坏都说清楚）

**收益（为什么值得）**：

- 可回溯：随时 New Chat，靠 Spec 迅速恢复上下文
- 可审查：审文档而非审海量 Diff
- 可维护：文档是资产，代码是耗材

**代价（必须承认）**：

- 前期写 Spec 有固定成本（但可被复利覆盖）
- 流程更“慢一点”，需要纪律与门禁
- 需要团队共识，否则容易半途而废

**不适用/谨慎**：

- 一次性脚本、纯探索实验、极短期小改动
- 对这些场景，建议走**单 Spec 的最小锚点**，而不是完整流程

### 0.2 单 Spec 主线（可选辅助文档）

默认只维护一份 **Spec 文档**，覆盖需求、约束、验收与实施。  
在需要时，再按阶段追加“辅助文档”即可：

- **Research 辅助**：`codemap/`、`context/`（查证现状与链路）
- **变更留痕**：`AI_CHANGELOG.md`（可选，但强烈推荐）

### 0.3 单 Spec 快速上手（30 分钟，可跳过）

目标：30 分钟跑通一次“文档 → 实现 → 复核 → 留痕”，产出 `docs/specs/feature-xxx/` 。

> 命令大模型一键进入单 Spec 的傻瓜交互模式：[《SDD-RIPER-ONE》](../protocols/SDD-RIPER-ONE.md)

1. 0–3min（Initialization）：给 AI 一份“家规/约束/口径”，让它复述确认。

2. 3–10min（Research）：给大模型足够的上下文和清晰的需求，让他出spec文档（In/Out + AC + 约束），你 Sign-off。

3. 10–15min（Plan）：让大模型按照spec文档去规划步骤并且更新到文档中。

4. 15–25min（Execute）：按spec文档的描述分步写代码 + 最小单测。

5. 25–30min（Review）：New Chat/换模型审查 Spec文档 + Diff，然后人工review此次改动并且上线。

### 0.4 手把手案例（可复现）

如果你希望先“照着跑一次完整闭环”（Spec → 实现 → 测试 → 交付留痕），可以先做一个开源项目的小练习

---

# 1. 引言：工具繁荣背后的“工程失序”

大模型与 AI 编程工具进入了快速迭代期：IDE、插件、模型能力每天都在刷新上限。表面上看是生产力爆发，但在真实的团队工程里，我们正在同时遭遇三类“隐性成本”，它们会抵消甚至吞噬工具红利。

### 第一，工具选择过载，导致协作割裂

团队把大量注意力投入在“用哪个模型/哪个 IDE 更强”的选择与配置上。短期看每个人都更快了，但由于缺少统一的输入标准与产出约束：

- 代码风格、工程结构、边界处理各自为政
- 同一需求被不同人用不同工具实现，产物难以合并、难以维护
- 组织层面无法复制经验，只能“个人英雄式提效”

### 第二，过度关注“锤子”，忽视“房子”的质量指标

评测往往聚焦“写得快不快、能不能一把梭”，但工程需要回答的是：

- 可维护性是否提升（结构清晰、可读、可扩展）
- 缺陷率是否下降（边界、异常、兼容性是否可靠）
- 需求变更时是否敢改、改得动（是否可追溯、可验证）

如果 AI 只是更快地产生“一次性代码”或“幻觉代码”，组织获得的不是效率，而是**技术债累积速度**。

### 第三，使用方式停留在“Chatbot 助手”

不少人仍把 AI 当成“问答框”：

- 报错就贴日志问原因
- 要函数就要片段
- 甚至不理解逻辑就直接接收产出

这种“补丁式/填空式”使用，缺少流程、缺少门禁、缺少协作协议，团队协作时很难形成稳定产能。

### 结论：我们缺的不是更强的模型，而是一套新的“AI 工程方法”

工具已经进入 AI 时代，但研发流程与协作方式仍停留在“人肉编码”的惯性里。要让 AI 真正成为可规模化的生产力，需要把个人技巧升级为团队 SOP。

> 我自己的真实 case：上个月用模型做了一个复杂功能（代码量大，经历多轮优化与 bugfix）并上线。后续出现几个小 bug、产品追加了几个新点；如果不用 SDD，就得翻提交+人工回忆来重建上下文，既慢也不精确；如果用 SDD，只要把“新需求文档 + 旧实施文档/决策留痕”交给模型，通常 10 分钟内就能启动下一轮迭代。

接下来要介绍的 **SDD（Spec-Driven Development，规范驱动开发）**，核心目标很明确：**让“文档/规范”成为任务的唯一事实来源，让 AI 围绕规范执行与互审，让人回到设计、决策与验收的位置。**

---

# 2. 核心理念：什么是 SDD（Spec-Driven Development）？

SDD 的关键不在“写更多文档”，而在于把 **Spec（Specification）** 当作研发过程的“契约”。在 AI 时代，编程的重心从“人直接写代码”转向“人定义规范，AI 按规范实现”。

## 2.1 核心定义：文档是 AI 之间的“通信协议”

> 💡 **极客时刻：重新定义** `.md` 曾有人提到过一个绝妙的笑话：以前编程语言都是从各种角度设计给人的，什么各种复杂的面向对象、类型系统、语法设计⋯很低效，虽然对于AI来说不在话下。下一个编程语言应该是直接给AI设计的，让AI可以高效创作。我建议命名为Machine Done（机器完成），后缀名都想好了，就叫.md。

> **这不仅仅是个段子，这正是 SDD 的本质。** 在真正的 AI 原生语言出现之前，Markdown 就是我们将意图传递给硅基大脑的最佳**中间语言 (Intermediate Representation)**。它既是人类的可读文档，更是机器的执行指令。写下 `.md` 的那一刻，就意味着：**Human Designed, Machine Done.**

需要纠正一个常见误区：文档不只是写给人看的，它同样是写给 AI 看的。

在 SDD 模式下，Spec 扮演一种“中间表示（IR）”：

- 人把模糊意图明确成可验证的规范（Spec）
- AI 读取 Spec 生成代码、测试、变更说明
- 另一 AI（或另一轮会话/模型）以 Spec 为准绳进行 Review
- 通过“以 Spec 为准”的闭环，减少口头沟通失真与上下文丢失

换句话说：**Spec 是团队里人和 AI 的共同语言，也是跨角色协作的统一输入。**

## 2.2 为什么要这么做？五个直接收益

### 1) 解决上下文丢失：用 Spec 锚定任务（Context Anchoring）

大模型对话天然存在“记忆衰减、注意力丢失、上下文腐烂、重点漂移、换会话丢上下文”等问题。Spec 作为稳定锚点，使得：

- 任务可在任意时间恢复（把 Spec 交给 AI 即可重建上下文）
- 重点更集中（以验收标准/边界条件为中心）
- 沟通更可追溯（争议回到 Spec，而不是回到聊天记录）

### 2) 不需要人类从零写文档：AI 起草，人类 Review / Sign-off

SDD 的典型操作流不是“人从头写一套文档”，而是：

1. 人提供需求/背景/约束（即使是粗糙口述也可以）

2. AI 产出或改写 Spec（结构化、可审阅）

3. 人作为仲裁者 Review，补齐边界与验收标准，并最终签字确认

4. **只有 Spec 通过，才进入编码与交付** 核心变化是：人把精力放在“正确性与决策”，而不是“打字与搬运”。

### 3) 角色边界清晰：不同角色对齐在不同层级的 Spec

SDD 不是让所有人都写同一种文档，而是让协作关系“各看各的关键点”：

- PM/业务：`Requirement Spec`（目标、范围、验收）
- 前后端/客户端：`Interface Spec`（字段、错误码、示例、契约）
- QA：`Test Spec`（用例覆盖、边界、回归策略）
- 架构/核心研发：`Implementation/Architecture Spec`（实现路径、取舍、风险） 大家在各自关心的层面完成对齐，最终通过 Spec 链条咬合成闭环。

### 4) 真正解耦模型与工具：Spec 让产能可迁移

当 Spec 足够清晰、约束足够明确时：

- 模型/工具可以替换（写草稿、重构、补测试、做 Review 可用不同模型）
- 产出更稳定（弱一些的模型也能按规范交付合格结果）
- 组织资产沉淀在 Spec 与规则里，而不是沉淀在某个工具的“私有用法”里

**结论**：SDD 的核心不是“文档本身”，而是“以规范为中心的协作协议 + 可验证门禁”，从而把 AI 的能力变成组织可复制的工程能力。

### 💡 核心辨析：为什么不直接用 OpenSpec 或 Spec-Kit？

市面上已经出现了如 **OpenSpec**、**GitHub Spec Kit** 等优秀的 SDD 自动化工具。它们很棒，但对于许多开发者来说，它们可能“太重了”或者“太死板”。

本文提出的 **Manual SDD 范式** 与这些 **工具框架** 的核心区别在于：

| 维度 | **OpenSpec / Spec-Kit (工具框架)** | **Manual SDD (本文范式)** |
| --- | --- | --- |
| **本质** | **软件工具**：需要安装 CLI，遵循特定工作流 | **思维模式**：一种约定，没有任何工具依赖 |
| **接入成本** | **低-中**：需 `npm install`，配置环境，学习指令 | **零**：新建一个 `.md` 就能跑，任何 IDE 通用 |
| **灵活性** | **受限**：必须遵循框架定义的文件夹结构 (`openspec/`) | **极高**：你想写成单文件还是文件夹，随心所欲 |
| **黑盒程度** | **高**：提示词和逻辑被封装在工具代码里 | **透明**：所有 Prompt 都在你眼皮底下，完全可控 |
| **适用场景** | 团队强制规范、大型协作项目 | **个人开发、快速原型、追求 Vibe 的极客** |

**结论**：OpenSpec 是把 SDD 变成了**流程**，而本文是把 SDD 变成了**习惯**。在 Vibe Coding 中，我们更倾向于“习惯”，因为习惯没有运行时开销。

# 3. 程序员实操 SOP：RIPER 工作流 (The RIPER Cycle)

> "If fixing takes too long, regenerate." (如果修复太慢，就重生成) —— Manifesto for Vibe Coding

> 但重生成的前提是：**Spec 是准确的**。否则重生成就是抽奖。

> 一键进入单 Spec 的傻瓜互动模式：[《SDD-RIPER-ONE》](../protocols/SDD-RIPER-ONE.md)

在这个单元，我们将深入“单兵作战”的细节。

很多程序员抱怨 AI 写的代码不能用，本质原因是 **跳过了思考，直接进入了执行**。为了解决这个问题，我们将传统的编码过程重构为 **Initialization + RIPER + LAFR** 全链路模型。

这不仅仅是写代码，这是一场精心编排的 **人机协作 (Human-AI Symbiosis)**。

## 初始化 (Initialization) —— 装载大脑

**“在开始干活前，先告诉 AI 它是谁，以及家规和历史信息是什么。”**

不要上来就扔需求。大模型就像一个刚入职的天才实习生，你需要先给它做 Onboarding。

- **动作**：
    1. **装载协议**：这是 SDD 的“操作系统”。如果你有没有个人偏好，或者以前没有用过大模型，请先发送以下指令，让 AI 进入“文档驱动模式”：

        > **⚡️ 通用启动指令 (System Prompt)**

        ```markdown
        # Role
        You are a Senior Engineer following the "Spec-Driven Development" protocol.
        
        # Workflow Rules
        1.  **Context First**: Before coding, ALWAYS check if a relevant Spec file exists in `docs/`.
        2.  **No Hallucinations**: If the user request contradicts the Spec, STOP and ask for clarification.
        3.  **Update Loop**: If you change the code logic, suggest updates to the corresponding Spec file immediately.
        
        # File Structure Strategy
        - Use `01_requirements.md` for User Stories.
        - Use `02_interface.md` for Tech Stack & Data Structures.
        - Use `03_implementation.md` for detailed Logic/Prompts.
        
        ```

    2. **加载偏好（可选）**：发送你的 `Prompt_Skill.md` 或 `.cursorrules` 的个性化部分。
        - 告诉它你的“私有家规”（如：“禁止使用 Lombok”、“所有金额计算使用 BigDecimal”）。
        - _注：如果没有特殊喜好，这一步可跳过，直接复用通用的启动指令即可。_
    3. **注入记忆**：把项目里的 README.md和某些功能的过往的历史信息也提供给大模型。
- **🚪 验收门禁**：
  - _AI 是否确认收到了上下文？（让它简单复述一遍主要约束和对此项目的总结）_

---

## The Core Loop: RIPER Model

### Step 1: Research (调研与意图锁定)

**“不要急着给方案，先搞清楚到底要解决什么问题。”**

很多时候，我们的需求描述是模糊的。这个阶段的核心是 **“反向复述”**。

- **输入**：口述需求 + CodeMap/Context 语料（若没有，先生成最小 CodeMap）。建议将材料沉淀到 `codemap/`、`context/` 与 `specs/` 目录中，便于复用。
- **动作**：
    1. **让 AI 阅读并复述**：指令它 —— _“请阅读上述需求，用你自己的话复述一遍，并指出其中不清晰的地方。”_
    2. **澄清边界**：让 AI 告诉你，这个需求涉及哪些业务领域？需要参考哪些现有的代码逻辑？
    3. **查证现状（Facts over Guessing）**：要求 AI 扫描代码库，给出关键文件路径与调用链，产出最小 Code Map，避免“想当然”。
    4. **产出首版 Spec**：要求模型生成第一份 Spec 草案（写进 `specs/`）。
    5. **人工审查 + 多轮修正**：完成意图锁定，再进入后续阶段。
- **产出**：清晰的 **Requirement Spec (需求意图)**。
- **🚪 验收门禁**：
  - _AI 指出的“模糊点”是否都已解答？AI是不是已经完全明白了需求意图和项目结构？_

### Step 2: Innovate (设计与推演)

**“这是体现架构师价值的环节。寻找最优解，而不是第一个想到的解。”**

这一步严禁写代码，而是要进行 **“审讯游戏 (The Interrogation Game)”**。

- **动作**：
    1. **生成草案**：让 AI 根据需求整理一份《技术实施草案》 (HLD)。
    2. **强制“互问互答”**：
        - **你要问它**：“除了这个方案，还有没有更好的？”“这样做的坏处是什么？”
        - **逼它问你**：指令它 —— _“如果你对现有业务逻辑或代码细节有任何不确定的地方，请立刻向我提问，不要自己瞎猜（Hallucinate）。”_
    3. **引入外部智慧**：把你同事的建议，或者你在其他项目的经验喂给它作为补充。

    > **💡 Pro Tip：去拟人化交互 (De-anthropomorphism)** 在向 AI 索要方案时，**千万不要用“你” (You)**。**记住：不要问它“怎么看”，要问它“它模拟的那个专家角色”怎么看。例如：顶尖专家和学者将会如何修改这个bug；或者顶尖程序员和架构师将如何设计这个功能等。**

- **产出**：**Design Spec (设计/技术规格书)**，包含核心技术选型、Pros/Cons 分析。
- **🚪 验收门禁**：
  - _你是否对这个设计方案进行了 review和Sign-off（批准）？_

### Step 3: Plan (规划与契约)

**“从战略下沉到战术。不仅要告诉它造什么房子，还要告诉它每一块砖怎么砌。”**

文档即协议。我们要把模糊的 Design 变成精确的 Implementation Plan。

- **动作**：
    1. **明确物理路径**：Spec 里必须写清楚：
        - 要修改哪几个文件（File Paths）？
        - 要新增哪几个方法和类（Signatures）？
        - **Mock 数据**：在写代码前，先定义好接口的 Request/Response 示例。
    2. **认知对齐**：再次进行 Review。问它：“为什么要在 Service 层做这个校验，而不是 Controller 层？”确保它不是在套模板，而是真的理解了逻辑。
    3. **Plan 即契约**：Plan Approved 之后，禁止随意变更需求；如需变更，必须回到 Plan 重新签字。
- **产出**：**Implementation Spec (详细实施/接口文档)**。
- **🚪 验收门禁**：
  - _实施计划是否拆解到了“原子级”任务，如果换一个大模型是否可以100%完美实施？_

### Step 4: Execute (执行与编码)

**“你不是在看戏，你是在跟 AI 结对编程 (Pair Programming)。”**

- **动作**：
    1. **分步指令**：不要试图一次生成 500 行代码。按照 Plan 的步骤，一步一步来。
        - _“好的，先完成 Step 1 的数据库 Schema 变更。”_
        - _“现在进行 Step 2，实现 Service 层逻辑。”_
    2. **实时自检 (Step-by-Step Check)**：每做完一步，让 AI 自己总结：“我完成了什么，这是否符合 Spec 的要求？”
    3. **人工干预**：如果发现它跑偏了，**立刻暂停**。不要在原来的基础上打补丁，而是回滚这一步，修正 Prompt 后重试。
    4. **Stop & Loop Back**：发现写不下去或逻辑冲突时，立即停止，回到 Spec 修正再继续。
- **产出**：源代码。
- **🚪 硬性门禁 (Hard Gates)**：
  - _**Lint Check**__：生成的代码必须通过 Linter 检查（无语法错误、无未使用的变量）。_
  - _**Compile Check**__：代码必须能编译通过。如果跑不通，严禁进入下一步。_

### Step 5: Review (审查与验收)

**“让一个 AI 去检查另一个 AI 的作业。”**

> **“这是对抗‘代码通胀’的唯一防线。当 Diff 达到几千行时，不要试图人肉 Review，要相信 Spec 的验证能力。”**

- **动作**：
    1. **New Chat / New Model**：实施完成后，**开启一个新的对话窗口**，甚至换一个模型（比如用 Claude Review GPT 的代码）。
    2. **法医式审查**：把 **Spec 文档** 和 **Git Diff** 喂给新 AI。
        - 指令：_“请基于这份 Spec 审查这次代码变更。寻找潜在 Bug、逻辑漏洞或不符合规范的地方。”_
    3. **迭代修正**：把审查报告扔回给负责写的 AI，让它解释并修正。如此循环几次，直到“评审官”满意。
    4. **反向同步（Fix Spec First）**：如果发现 Bug 或不一致，先修 Spec/ChangeLog，再让 AI 重新生成或修复代码。
    5. **旁观者视角 (The Spectator Stance)** 不要问 AI：“_你_觉得刚才写的代码对吗？”（它通常会说“是对的”来讨好你）。 要这样问：“如果请 _Google 的 Principal Engineer_ 来做 Code Review，他会指出这段代码的哪些隐患？” 通过引入**第三方权威视角**，可以有效打破模型的“顺从性幻觉”，强制它开启高强度的批判性思维。
- **产出**：单元测试、Review 报告、最终交付代码。
- **🚪 硬性门禁 (Hard Gates)**：
  - _**Automated Tests**__：自动化测试必须全绿（覆盖门槛按项目等级设定，并在 CI/规则库中固化）。_
  - _**Interface Contract**__：新代码的接口响应必须与_ `_02_interface.md_` _定义的 JSON Schema 完全一致（使用工具自动比对）。_
  - _**未过门禁 = 0 交付**__：任何一项失败，直接退回 Step 4，严禁合并代码。_

---

## RIPER 常见失效原因（坏话说在前面）

1. **跳过 Research**：没有查证现状就下结论，后续全部建立在错误前提上。  

2. **Plan 后随意改需求**：破坏契约，导致执行与验收失去基准。  

3. **只修代码不修文档**：形成 Spec Drift，越修越乱。  

4. **没有第二视角 Review**：单模型自检容易“互相包庇”。  

## 旁路流程：L.A.F.R. 故障排查协议

**“遇到 Bug 时，不要直接改代码。Bug 的本质是‘代码’与‘文档’的对齐失败。”**

当生产环境报错或测试不通过时，请严格执行 **L.A.F.R.** 流程：

1. **Locate (定位)**：构建“案发现场”。投喂黄金三角：**Spec 文档 + 相关代码 + 报错日志**。

2. **Analyze (分析)**：让 AI 判决，是 **“执行层错误”**（代码写错了）还是 **“设计层错误”**（文档没写对）。

3. **Fix (修复)**：

    - 如果是代码错 -> 生成补丁。
    - **如果是文档错 -> 必须先改文档，再重新生成代码。**（避免暗箱修改：先改文档，再改代码）

4. **Record (留痕)**：

    - 更新 `SKILL.md`，防止下次复发。
    - 在文档上打补丁：_“⚠️ \[FIX\] 此处逻辑曾导致死锁，已修正为...”_

---

# 4. 文档解剖学：端到端闭环实战（The Full Loop）

为了让“文档 = 协议”不再停留在概念层，这一章用一个贯穿示例（**用户积分系统 - 签到功能**）展示：**一套最小但完整的 Spec 链条**应该长什么样、写到什么粒度算合格、以及这些文档如何直接驱动 AI 产出与团队并行协作。

本章的核心原则：

- **Spec 不是“说明书”，而是“可执行指令集”**：能直接喂给 AI 生成代码/测试/评审。
- **每份 Spec 都要“可验收”**：写清楚验收标准与边界，减少口头解释空间。
- **一份 Spec 对应一个 Owner 与一次 Sign-off**：否则文档会快速漂移（Spec Drift）。

---

## 4.1 推荐目录结构（Documentation Engineering）

> 目标不是“堆文档”，而是**让 Research 有材料、让 Spec 可复用**。

```text
docs/
├── specs/
│   ├── feature-001-checkin.md            # 单 Spec：需求/约束/验收/实施合一
│   └── feature-001-checkin.appendix.md   # 可选：额外补充或大段上下文
├── codemap/
│   └── checkin.md                        # 功能 ↔ 类/函数映射
├── context/
│   └── checkin/                          # PRD/设计图/讨论记录等原始语料
├── apis/                                 # 可选：接口契约层
│   └── checkin-api.md
├── AI_CHANGELOG.md                       # 变更留痕
└── skills/                               # 可选：团队规则库/“家规”
    └── SKILL.md
```

约定建议（便于团队规模化）：

- **一个 feature 一份 Spec**：不要把多个需求混在一个 Spec 里，避免上下文污染。
- **命名稳定**：以 `20xx-xxxx-xx:xx_feature-xxx.md` 命名，便于检索与对齐。
- **文档有版本意识**：重大变更通过 PR 更新 Spec，让“讨论/决策/结果”都可追溯。

**Research 标准动作（与教程一致）**：口述需求 + CodeMap + Context → 产出首版 Spec → 人工审查修正。

---

## 4.2 核心文档模板与端到端示例

下面给出每类 Spec 的三件事：

1. **最小模板**（团队可直接复制）

2. **签到功能示例片段**（让你知道该写成什么样）

3. **门禁（Definition of Done）**（写到什么程度才允许进入下一步/合并代码）

---

### A. Requirement Spec（需求规格）——意图层（写给人，也写给 AI）

**定位**：把“想要什么”写成可验收的契约，避免实现阶段反复扯皮。   **主要读者**：PM/业务 Owner、研发 TL、QA、AI（用于复述与生成后续文档）。

#### 最小模板：`01_requirement.md`

- 背景（Context）：为什么要做（1 段即可）
- 目标（Goals）：要达成什么结果（条目化）
- 范围（In Scope / Out of Scope）：明确不做什么
- 验收标准（Acceptance Criteria, AC）：**必须可验证**
- 约束（Constraints）：性能/安全/兼容/依赖系统/灰度要求
- 风险与灰度（Risks & Rollout）：上线策略、回滚预案（如适用）

#### 示例片段（签到功能）

```md
## Background
为了提升 DAU 与留存，引入“每日签到得积分”，积分可用于兑换权益。

## In/Out
- In：每日签到、幂等、防重复、查询签到状态、积分发放
- Out：积分商城兑换、积分过期策略（本期不做）

## Acceptance Criteria
- AC1：同一用户同一天只能签到一次，重复请求返回“已签到”且不重复发放积分
- AC2：返回结果需包含：是否签到、签到时间、当次获得积分、当前总积分
- AC3：接口 P95 < 200ms（依赖现有积分查询能力）
- AC4：出现异常时必须可追溯（含必要审计字段）


```

#### 门禁（写完才允许进入接口/实施）

- AC 至少覆盖：**主流程 + 重复请求/幂等 + 至少 2 个失败场景**
- In/Out 明确，避免“做到一半发现还要做 X”
- 关键约束写清楚（性能/安全/灰度/审计），否则后面补救成本更高

---

### B. Interface Spec（接口契约）——协议层（跨角色并行的关键）

**定位**：这是前后端/客户端/测试并行启动的“唯一真相”。   **主要读者**：前端/客户端（生成 types/mock）、后端（实现约束）、QA（生成用例/自动化）、AI（按契约写代码）。

#### 最小模板：`02_interface.md`

- 总览：鉴权方式、幂等要求、错误码规范
- Endpoint：路径、方法、说明
- Request：字段表/Schema（含必填、类型、枚举、校验）
- Response：字段表/Schema（明确成功/失败结构）
- Error Codes：错误码、含义、触发条件
- Examples：成功/失败示例（用于 mock 与契约测试）
- Notes：兼容性、版本策略（如适用）

#### 示例片段（签到接口）

```md
## API: POST /api/v1/points/check-in
Auth: Bearer Token
Idempotency: 同一 userId + 同一 date 必须幂等

### Request
- date (string, optional): YYYY-MM-DD，不传则默认当天（以服务端时区为准）

### Response (Success)
- checkedIn (boolean)
- checkedInAt (string, ISO8601, nullable)
- pointsEarned (int): 本次发放积分（已签到则为 0）
- totalPoints (int)

### Error Codes
- INVALID_DATE：date 格式非法
- UNAUTHORIZED：未登录/Token 无效
- INTERNAL_ERROR：服务端异常（需返回 requestId）

### Examples
Success (first time):
{ "checkedIn": true, "checkedInAt": "2026-01-02T09:00:00Z", "pointsEarned": 5, "totalPoints": 120 }

Success (already checked-in):
{ "checkedIn": true, "checkedInAt": "2026-01-02T09:00:00Z", "pointsEarned": 0, "totalPoints": 120 }


```

#### 门禁（写完才允许前端/测试并行、后端进入实施）

- **必须有成功 + 已签到（幂等） + 至少 1 个失败**示例
- Error Codes 写清“触发条件”，避免后续实现随意发挥
- 字段定义要可直接生成类型（TypeScript/Java DTO），否则契约无法落地

---

### C. Implementation Spec（实施细节）——执行层（给 AI Coder 的“施工图”）

**定位**：把“怎么改”写成可执行计划，控制 AI 的改动范围与顺序。   **主要读者**：实现负责人、AI Coder、Reviewer。

#### 最小模板：`03_implementation.md`

- 目标复述：用 3~5 行复述本次要实现什么（对齐）
- 变更范围：**要改哪些文件/模块**（带路径）
- 数据变更：表结构/索引/迁移（如适用）
- 核心流程：伪代码/步骤（含幂等、并发、事务边界）
- 关键校验与异常：输入校验、错误码映射、审计字段
- 分步执行计划：Step 1/2/3…（每步可独立验收）
- 回滚与兼容：怎么关、怎么回退、影响面

#### 示例片段（实现计划）

```md
## File Changes
- backend/src/main/java/.../CheckInController.java
- backend/src/main/java/.../PointsService.java
- backend/src/main/java/.../PointsRepository.java
- backend/src/test/java/.../PointsServiceTest.java

## Core Logic (pseudo)
1) parse date (default today) -> validate format
2) start tx
3) try insert checkin_record(user_id, date) with unique(user_id, date)
   - if conflict -> return already checked-in (pointsEarned=0)
4) if inserted -> add points (+5) and write ledger/audit
5) commit
6) query totalPoints -> return response

## Execution Plan
- Step1: 增加/确认 checkin_record 唯一约束与实体映射
- Step2: 实现 PointsService.checkIn(date) 幂等逻辑 + 错误码映射
- Step3: Controller 层对齐接口契约（02_interface.md）
- Step4: 补单测（首次签到/重复签到/非法日期）


```

#### 门禁（写完才允许进入编码）

- **明确文件路径 + 方法签名/职责边界**（否则 AI 容易乱改）
- 核心流程必须覆盖：幂等/并发/事务/异常映射
- 执行计划可分步验收（每步完成后可自检/可回滚）

---

### D. Test Spec（测试策略）——验证层（把验收落到可执行用例）

**定位**：把 AC 与接口契约转成测试策略与用例清单，避免“上线后才发现漏测”。   **主要读者**：QA、研发（补单测/集成测试）、AI Test Agent（生成用例/脚本）。

#### 最小模板：`04_test_spec.md`

- 测试范围：覆盖哪些层（Service/Controller/契约/集成）
- 测试策略：哪些用单测，哪些用集成，哪些做契约测试
- 用例列表：编号 + 场景 + 期望结果（对齐 AC/Error Codes）
- 数据准备：前置数据、时间/时区假设、Mock 依赖
- 回归影响：可能影响哪些老功能（提示回归点）

#### 示例片段（用例清单）

```md
## Strategy
- Service 层：单测覆盖幂等与错误码
- Controller 层：契约测试校验 JSON 字段与类型（对齐 02_interface.md）

## Test Cases
- TC1 首次签到：返回 checkedIn=true, pointsEarned=5，totalPoints 增加
- TC2 重复签到：pointsEarned=0，总积分不变，checkedInAt 不变化
- TC3 非法 date：返回 INVALID_DATE
- TC4 并发重复请求：最多一次发放积分（验证唯一约束/幂等）


```

#### 门禁（写完才允许合并/上线）

- 用例必须覆盖：AC 中的关键路径 + Error Codes + 并发/幂等
- 若线上问题修复：必须补充对应回归用例（防复发）

---

### E. 交付与归档模板（让“可追溯”成为默认）

#### 1) Implementation Summary（交付小结，建议进入 PR 描述）

```md
- Feature：实现每日签到得积分（含幂等）
- Changes：新增 checkin_record 唯一约束；新增/修改 PointsService.checkIn；补充单测
- Risks：时区口径（服务端时间为准）；并发下依赖唯一约束兜底
- Rollback：开关关闭签到入口；保留数据表但停止写入
- Related Specs：docs/specs/feature-001-checkin/*


```

#### 2) AI_CHANGELOG.md（决策日志：记录“为什么这么改”）

```md
2026-01-02 feature-001-checkin
- Decision：幂等通过数据库唯一约束实现，而不是 Redis 计数
- Reason：降低一致性风险与依赖复杂度；数据库作为最终一致性来源
- Risk：高并发写入压力；需关注索引与事务耗时


```

---

## 4.3 本章“写作粒度”快速自检清单

在你把 Spec 丢给 AI 之前，先自检 2 分钟：

- Requirement：AC 是否“可测试”、是否包含边界与失败？
- Interface：是否有幂等/错误码/示例？前端能否直接做 mock？
- Implementation：是否写清文件路径、步骤、事务/并发处理与回滚？
- Test：是否覆盖幂等与错误码？是否写清数据准备与回归点？

做到以上四点，章节 3 的 RIPER 执行才会真正稳定；否则再强的模型也会在“缺口处自由发挥”。

---

# 5. 团队协作 SOP：构建“文档即接口”的通信协议

如果说上一章解决的是“如何让 AI 帮你写好代码”，那么这一章要解决的是“如何让 AI 帮团队消除沟通噪音”。

现状是分裂的：我们每个人手里都有了核武器（大模型），但团队协作还在用冷兵器（开会、口述、聊天记录）。我们必须构建一套新的协作 SOP，核心理念只有一条：**人与人的沟通只负责确认意图，AI 与 AI 的沟通负责传递细节。**

## 5.1 理想国：全链路的“去噪音化” (The Ideal Flow)

虽然完全实现尚需时日，但我们应以此为北极星：

1. **需求孵化（前线 -> PM）**

    - 前线人员不再扔一堆杂乱的聊天记录给产品，而是先让 AI 总结：“把这段客户沟通整理成结构化的需求草案，去除废话，保留核心痛点。”
    - **价值**：从源头消灭“不说人话”的需求。

2. **规格定义（PM -> Dev）**

    - 产品经理将草案喂给 AI，生成标准化的 PRD（需求规格书）。
    - **价值**：虽然开发人员知道需求是什么，但**大模型不知道**。PM 用 AI 生成的文档，本质上是在为开发的 AI 准备“精准的 Prompt”。

3. **任务分发（TL -> Member）**

    - Team Leader 维护一份 `Team_Context.md`（组员负责的方向、当前负荷、技术栈偏好）。
    - 让 AI 辅助决策：“基于这个需求文档和团队现状，建议分配给谁？有什么技术风险？”

## 5.2 \[最佳实践\] 文档的“双态”生命周期

在实战中，我们发现强行要求“文档与代码实时完美同步”会严重拖慢开发节奏。因此，我们总结出了 **“双态管理”** 策略，将文档区分为\*\*“热数据”**与**“冷数据”\*\*：

| 状态 | **热文档 (Hot Specs)** | **冷文档 (Cold Docs)** |
| --- | --- | --- |
| **位置** | 个人 Feature 分支 | Main 分支 / 团队 Wiki |
| **归属** | **个人工作台** | **团队资产** |
| **特点** | **高频变动**：甚至可以用伪代码、草稿，只要 AI 能懂就行。 | **稳定精简**：经过代码验证的真理，去除过程噪声。 |
| **动作** | 随 Reroll 随时修改 | 定期时进行一次“清洗 (Prune)”和汇总。 |

**💡 经验之谈**：

- **开发时**：不要有心理负担，把 Spec 当作你的草稿纸。
- **合并时**：就像你会 Squash 那些琐碎的 Git Commit 一样，你也应该 **Squash 你的文档**，只把最终生效的逻辑同步给团队。
- 最终这些文档会合并上传并沉淀在你团队的知识库，成为团队宝贵的资产。

## 5.3 落地现实：技术铁三角的协作闭环 (The Pragmatic Protocol)

鉴于业务侧的不确定性，我们可以优先在**后端、前端/客户端、测试**之间建立强制性的 **Spec 协作流**。

### 责任分工（建议，避免“文档写了没人维护”）

- `01_requirement.md`：Owner=需求/产品或需求提出人；Sign-off=业务 Owner + TL。
- `02_interface.md`：Owner=接口提供方（通常后端）；Sign-off=接口消费者（前端/客户端）+ QA。
- `03_implementation.md`：Owner=实现负责人；Sign-off=TL/核心评审人。
- `04_test_spec.md`：Owner=QA（或测试 Owner）；Sign-off=实现负责人 + QA。

### 阶段一：后端作为“定义者” (Backend as Definer)

后端开发不再是默默写代码，而是先产出“契约”。

- **动作**：后端在写业务逻辑代码前，先让 AI 按照章节2的流程生成**技术文档**、**实施文档**和 `02_interface.md`（接口文档） 。
- **人类介入**：Leader和同事只需要 Review 这些文档。文档通过，等于架构设计通过。

### 阶段二：并行开发 (Parallel Execution)

这是效率提升最显著的环节。传统的“前端等后端接口”模式被彻底打破。

- **前端/客户端 (The Consumer)**：
  - **输入**：拿到后端发来的 `02_interface.md`。
  - **AI 动作**：
        1. _“阅读这份接口文档，为我生成 TypeScript 类型定义 (Interface/Types)。”_
        2. _“基于文档生成一个 Mock Server 的代码，并制造 5 组边缘情况的假数据。”_
  - **结果**：在后端一行代码没写的时候，前端已经基于 AI 生成的“完美模拟器”完成了 UI 开发和逻辑联调。
- **测试/QA (The Validator)**：
  - **输入**：拿到 `01_requirement.md` (需求) + `02_interface.md` (接口)。
  - **AI 动作**：
        1. _“作为 QA 专家，阅读这些文档，生成覆盖所有分支的测试用例列表。”_
        2. _“为这些接口生成自动化测试脚本（如 Pytest/Postman）。”_
  - **结果**：测试可以根据文档来精准确认修改范围和波及的功能，并且可以更快速的更新自动化和回归测试。

### 阶段三：交付与归档 (Handover & Archive)

- **代码不是唯一的交付物**：

  - 提交代码时，必须附带由 AI 更新过的 Implementation Summary **(实施总结)**。
  - 内容包括：改了什么？为什么这么改？哪里有潜在风险？配置项怎么配？
- **项目收尾归档**：

  - 项目结束后，将所有文档（需求、接口、实施、测试）丢给大模型。
  - _“把这些文档归档，更新到项目的_ `_README.md_` _和_ `_Architecture.md_` _中，保持项目知识库的鲜活。”_

## 5.4 为什么这比“开会”好？

1. **大模型的“通天塔”作用**：

    - 前端看不懂后端的 Java 代码，测试看不懂前端的 React 代码。
    - 但所有人的 AI 都能看懂 **Markdown 文档**。文档成为了跨语言、跨角色的通用字节码。

2. **消除“幻觉传递”**：

    - 口述最容易失真。A 说“大概两小时”，B 听成“两小时后上线”。
    - 文档是静态的、可追溯的。AI 基于文档生成的代码，只会忠实于文档，不会忠实于你的“口误”。

3. **极低的接入成本**：

    - 不需要购买复杂的协作软件。
    - 仅仅是多了几个 `.md` 文件。
    - 大家依然用自己喜欢的 IDE 和 AI 工具，只是输入源变了。

4. **归档和溯源**：

    - 现在每个人都需要强制写文档和留存文档了，可以极大的增强文档的覆盖率。
    - 如果出现一些误会和问题，可以快速准确的定位，不需要在翻聊天记录扯皮了。

## 5.5 人类的位置：由于 AI 做了执行，人类必须做决策

千万不要觉得“全都交给 AI 了，人没事干了”。恰恰相反，在这个流程中，**人的“决断力”变得前所未有的重要**。

- **PM** 要决断：AI 生成的需求文档，逻辑是否自洽？是不是用户真正想要的？
- **后端** 要决断：AI 建议的数据库设计，三年后是否会成为系统性风险？
- **前端** 要决断：AI 写的 Mock 数据是不是太理想化了？真实网络环境会怎样？

**SOP 的目的不是把人变成机器，而是把人从“复读机”和“搬运工”的低级劳动中解放出来，去把控那些只有人类能理解的复杂性（Context & Humanity）。**

---

# 6. 基础设施与资产沉淀：Prompt 才是核心资产

在 SDD 模式下，代码变得廉价且易变（Disposable）。那么，团队究竟在积累什么？ 答案是：**积累“如何让 AI 写出好代码”的知识。**

以前，资深工程师的经验存在脑子里；现在，必须把这些经验固化为 **Agent Skills**。

## 6.1 建立团队的“第二大脑” (The Skill Store)

> "Taste is the ultimate filter." (品味是终极过滤器)

不要让每个人都去重复踩坑。

- **动作**：在项目根目录维护一个 `.cursorrules` 文件或 `docs/skills/SKILL.md`。
- **内容**：
- **技术偏好**：_“本项目使用 Java 17，优先使用 Record 类，禁止使用 Lombok。”_
- **业务铁律**：_“所有涉及金额的字段，数据库必须用_ `_Decimal(19,4)_`_，Java 必须用_ `_BigDecimal_`_，禁止用_ `_Double_`_。”_
- **测试规范**：_“单元测试必须使用 JUnit 5，且必须覆盖空指针异常。”_
- **机制**：每次有新同学（或新 AI Session）加入开发时，第一件事就是读取这份文件。这相当于给 AI 装载了团队的“集体记忆”。

## 6.2 错误即规则 (Error to Rule)

这是 SDD 模式下最有复利的进化逻辑。

- **传统模式**：出现 Bug -> 修代码 -> 提交 -> 下次还敢。
- **SDD 模式**：出现 Bug -> **修 Skill** -> 让 AI 重新生成代码。
- 如果你发现 AI 总是忘记处理分页，不要骂它。
- 请在 `SKILL.md` 里加一条：_“规则 #42：所有列表查询接口必须默认包含分页参数。”_
- 从此以后，这个问题绝迹了。
- 累计的错误记录，bug总结，修复方法也会成为团队的宝贵财富。

## 6.3 飞行日志 (The Black Box)

当代码不是人写的，\*\*“由于什么原因改了什么”\*\*变得比代码本身更重要。

- 强制维护 `docs/decisions/AI_CHANGELOG.md`（这点可以使用一些skill来简单高效的完成）。
- 这不是 Git Log，这是**决策日志**。
- 格式：_“2026-01-01: 基于_ `_Spec-Auth-v2.md_` _重构了登录模块。风险点：废弃了旧版 Token 校验逻辑。”_

## 6.4 Spec 资产保鲜：生命周期管理协议 (Lifecycle Management)

文档最怕的是“写完即死”。为了防止 **Spec Drift（规格漂移，即代码改了文档没改）**，必须建立严格的生命周期管理：

1. **Owner 机制**：

- 每份 Spec 必须有明确的 **Human Owner**（通常是提交 PR 的人）。AI 只是 Writer，人是 Owner。

1. **变更触发器 (Triggers)**：

- **需求变更**：改代码前，**必须**先改 `Requirement Spec`。

- **代码重构**：改逻辑前，**必须**先更新 `Implementation Spec`。
- **线上 Bug**：执行 LAFR 流程修复后，**必须**回填 `Test Spec`（补录 Case）。

---

# 7. 风险防范：给 AI 戴上镣铐

没有约束的 AI 也是一种灾难。作为架构师，你必须划定红线。

## 7.1 数据安全分级 (Data Privacy)

参考按密级划分的数据安全标准，建立严格的模型使用纪律：

- **高压红线级 (高敏感/核心代码)**：如支付核心、用户隐私数据（在这个场景下，此方案变得尤其好用）。
- **红线**：**严禁**把敏感信息喂给外部大模型。
- **SOP**：使用私有化部署模型（如企业内网大模型）生成脱敏后的 Spec 文档，让外部大模型阅读修改脱敏后的文档，最后让内部大模型还原文档和实施代码。
- **普通级 (通用逻辑/工具)**：如前端 UI、工具类、单元测试。
- **策略**：大胆使用最先进的外部模型（GPT-5.2/Claude 4.5），追求最高效率。

## 7.2 幻觉识别 (Anti-Hallucination)

大模型最擅长“一本正经地胡说八道”。

- **不仅要看它写了什么，还要看它引用了什么**。
  - 如果 AI 调用了一个你没见过的库函数，**90% 是幻觉**。
- **对策**：在 **RIPER 流程** 的 **Step 5 (Review)** 阶段，强制 AI 提供代码的出处或官方文档链接。
- **如果你看不懂 AI 写的代码，就不要用**。
- SDD 的原则是：你必须有能力为 AI 的产出兜底。看不懂的代码就是埋在项目里的地雷。

## 7.3 责任归属 (Accountability)

- **基本法**：**谁 Sign-off 文档，谁 Sign-off 代码，谁就对 Bug 负责。**
- 不要试图甩锅给“是 AI 写的”。AI 是你的笔，字写错了是人的问题。

---

# 8. 常见问题（Q&A）

## Q1：新项目冷启动，怎么让大模型“快速上手”？

你本来就会让模型先做一次 research（读 README/架构/依赖/目录结构/关键约束），区别在于：**不要让 research 只停留在对话里**。

一个很实用的习惯：每次让模型做完 research，顺手补一句——

- **“把你刚才的结论总结成规整文档，输出到** `**docs/**`**（并给出建议的目录结构/后续要写的 01/02/03/04）。”**

这样新项目的“上下文载体”就建立了：后续你 new chat、换模型、换人，都能从 `docs/` 直接恢复状态，而不是靠人肉复述。

## Q2：老项目冷启动（存量），没有文档怎么办？

存量项目迟早都要做文档；区别只是**被动补救**还是**增量沉淀**。

建议不要试图“一次性补齐全量文档”，而是从你下一次要做的变更开始增量补：

1. 选一个真实的 feature/bugfix，当场写一套最小 Spec（01/02/03/04）。

2. 让模型基于代码现状生成 `03_implementation.md` 骨架（改哪里、边界在哪、风险在哪）。

3. 每次合并 PR 时强制更新：`docs/decisions/AI_CHANGELOG.md`（为什么这么改），并回填测试用例（防复发）。

这样文档会自然“长出来”，而不是变成一个永远排不上期的“大重构”任务。

## Q3：老项目已经有文档，怎么用才不浪费？

- 直接把现有文档作为上下文喂给模型，让模型**补齐缺失的验收标准/边界/错误码**，并重排成统一的 `01/02/03/04` 结构。
- 把最关键的“历史取舍/坑位”抽出来沉淀进 `AI_CHANGELOG.md` 与 `SKILL.md`，让后续迭代不需要靠“口口相传”。

## Q4：这会不会变成“写文档负担”？

关键不在“写更多”，而在“写对地方”：

- 文档只写到能驱动实现与验收的程度（Spec 是指令集，不是长作文）。
- 让 AI 起草，你只做 Review/Sign-off；把文档写作成本压到“可接受的固定开销”。
- 用门禁保证文档不死：需求变更先改 01，重构先改 03，线上问题必须回填 04 + SKILL。

## Q5：后续维护是不是都“基于文档”，不直接改代码？

理想状态是：**人尽量不直接改代码，而是先改/补 Spec，再让 AI 按 Spec 改代码**（然后由人做 Review/Sign-off）。

原因很简单：当你把编码执行交给模型之后，最大风险来自 `new chat` 的上下文缺失——同一个需求、同一段代码，换会话/换模型就可能出现理解偏差。Spec 作为“唯一事实来源”，能让后续的 feature/bugfix 复用同一套上下文与约束，避免每次都靠聊天重建。

现实落地时可以这么做（低摩擦）：

- **小改动**：允许直接让 AI 出补丁，但必须同步更新对应的 Spec/Changelog（避免 Spec Drift）。
- **复杂改动/反复迭代的模块**：强制“先文档后代码”，把新需求与旧实施/决策文档一起喂给模型，先对齐再执行。

## Q6：现在是不是所有代码变更都走这套方法论？大概有多少真实代码实践？

不必教条化到“100% 的改动都写全套 Spec”。更现实的做法是：

- **主流程/复杂特性/高风险变更**：强烈建议走完整链路（至少 01/02/03/04 + Changelog），收益最大。
- **小 bugfix/小需求**：可以走**最小锚点**（单 Spec + 简短留痕，甚至直接让 AI 出补丁），但至少要留一份最小存档（例如更新 `AI_CHANGELOG.md` 或补一段简短的实施/测试记录），避免后续无法复盘。

至于“真实实践量”，更有意义的指标不是行数本身，而是：是否覆盖了“新功能上线 + 多轮优化 + 多次 bugfix + 需求增量”的完整生命周期；只要能在多次 `new chat` 下依然稳定复用上下文，说明方法论已经在真实场景里跑通。

## Q7：别人还在写 Spec，我已经上线了，会不会被流程拖慢？

如果 Spec 变成“写完一套长作文才允许动手”，当然会拖慢；SDD 追求的是**把最小必要的对齐与验收前置**，让执行可以更快、更稳。

建议的节奏是：

- **先写最小 01/02（范围 + 契约）**，让并行与执行立刻启动。
- `03/04` 可以在实现过程中增量补齐，但必须在合并/上线前达到门禁。
- 对于小改动，允许**最小锚点**甚至“先修再补留痕”，但要保证不会形成长期 Spec Drift。

## Q8：有没有办法把“文档成本”再降一些？是不是要等 DeepWiki 之类的能力成熟？

文档能力当然会被工具持续增强（例如自动索引、统一检索、知识库/DeepWiki、MCP 接入等），但这不是 SDD 成败的前提。**SDD 的重点是“上下文有载体 + 可验收 + 可追溯”**，形态很灵活：

- **轻量玩法（马上能用）**：让大模型在 research/实现后顺手把结论输出成文档，落到 repo 的 `docs/` 里；你只做 Review/Sign-off。
- **重度玩法（组织化建设）**：统一建设各项目的 Wiki/文档体系，配合索引与权限治理；再接入 MCP/统一查询，把“找信息”这件事变成基础设施能力。

换句话说：工具越强，成本越低；但即使没有 DeepWiki，你也可以从“顺手落 `docs/`”开始，把上下文沉淀起来，先跑通闭环。

## Q9：有人觉得写 Spec 太重，不够 Vibe Coding？

这是一个误区。**没有 Spec 的 Vibe Coding 不是“快”，而是“赌”。** Vibe Coding 提倡 **"If fixing takes too long, regenerate"**。但如果没有 Spec 文档作为基准，你每次 Regenerate 都是在碰运气（幻觉漂移）。**SDD 实际上是 Vibe Coding 的“安全带”**——它极轻（最小锚点），但能让你在高速飙车（Reroll）时，始终不偏离轨道。

## Q10：既然有 OpenSpec 这种工具，我为什么要手写文档？

**因为工具会过时，但“文本”永存。**

- **反脆弱**：使用专门的工具框架（OpenSpec/Spec-Kit）意味着你绑定了它的生态。如果有一天它不维护了，或者不支持最新的模型了，你的工作流就断了。
- **原生感**：Manual SDD 是 **LLM Native** 的。它利用的是大模型最原始的阅读能力（Markdown），这意味着无论你是用 Cursor、Windsurf、还是未来的 GPT-6，这套方法论永远通用，不需要等工具适配。

## Q11：文档维护会不会很麻烦？特别是开发期变动频繁时

**不会。采用“松耦合”策略，区分“个人工作台”与“团队知识库”。**

正如你提到的，现代开发通常是\*\*“一人负责一个模块”\*\*：

- **开发期（热数据）**：Spec 文档就在你的本地或 Feature 分支里。它是你的**私人草稿本**，随改随用，不需要实时同步给所有人，也不会影响主干。
- **归档期（冷数据）**：等到月度或季度复盘时，再将这些经过代码验证的 Spec **精简**后，上传到部门知识库（Wiki）。

**这样，既享受了 SDD 的开发便利，又自然而然地完成了团队的知识沉淀，还可以给知识库持续“造血”。**

---

## 附录A：进阶实践与工程护栏（从觉醒篇迁移）

### A.1 提示词工程：个人 Prompt 模板

大模型的“聪明程度”一半来自模型本身，另一半来自你给的提示词（Prompt）。对于经常使用的模型，建议为每个模型准备一份**固定提示词文件**，例如 `claude.md`、`gpt.md`、`gemini.md`，并在会话开始时整体贴入。

一个实用的个人 Prompt 模板通常包含这些部分：

- **引用文档**：不要在 Prompt 里口述复杂逻辑，请直接引用 URL 或文件路径（`@docs/spec.md`），让 AI 以文档为准。
- **角色定义**：你希望模型扮演什么角色（结对工程师 / 架构师 / 文档助手等）
- **目标与范围**：这次对话主要解决什么问题，允许/不允许碰哪些模块
- **工作方式**：先问再改、先给方案再写代码、必须生成测试等
- **禁止事项**：不允许拍脑袋造接口、不允许一次改太多文件、不允许忽略安全规则等
- **输出格式**：需要列表、代码块、Diff、还是分步骤说明
- **项目特定习惯**：日志前缀风格、错误码规范、测试框架等

现在因为大模型能力的增强，已经不需要再写以前那种很长的、人设般的提示词了，但**约束型与步骤型**仍然很好用，比如：

中大型功能：

- [《RIPER-5》](../protocols/RIPER-5.md)
- [《SDD-RIPER-ONE》](../protocols/SDD-RIPER-ONE.md)

网上也有很多很优秀的模版，比如：

- [https://cursor.directory/: https://cursor.directory/](https://cursor.directory/)
- [https://github.com/f/awesome-chatgpt-prompts: https://github.com/f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)

在这里也科普一下提示词的基础原理：

- [https://ata.atatech.org/articles/12020498410?utm\_source=mail&utm\_medium=dailyRecommend&utm\_campaign=headline: https://ata.atatech.org/articles/12020498410?utm\_source=mail&utm\_medium=dailyRecommend&utm\_campaign=headline](https://ata.atatech.org/articles/12020498410?utm_source=mail&utm_medium=dailyRecommend&utm_campaign=headline)

### A.2 进阶技巧：构建“会自我进化”的 SOP (Real-Time RL Lite)

在深入这个技巧之前，我们需要先对齐一个工程概念，**这不仅关乎提示词，更关乎工具链的集成**：

> 💡 核心概念补齐：什么是 Claude Skill？
> Claude Skill 是一个将“大模型的思考逻辑”（Prompt/SKILL.md）与“传统代码的执行能力”（Scripts）打包在一起的“能力插件”，旨在让通用的 AI 瞬间变成能精准执行特定复杂任务的垂直专家。
> 在高阶 AI 编程中，一个成熟的 Skill 通常不止是提示词，而是一个**“能力包”**，包含两个核心部分：
> **1. 大脑 (**`**SKILL.md**`**)**
>
> - 这是 AI 的决策指南。它定义了“什么时候用这个技能”以及“怎么分析结果”。
> - _例如_：“当用户要求代码审查时，请先运行下方的 Python 脚本，然后根据输出结果给出建议。”
>
> **2. 手脚 (Scripts/Tools)**
>
> - 这是具体的执行脚本（Python/Bash/Node.js 等）。
> - _例如_：`check_coverage.py`（查覆盖率）、`format_json.py`（格式化数据）。
>
> **结构示例：**
>
```text
my-code-review-skill/
├── SKILL.md          # 告诉 AI：先跑脚本，再根据日志写评语
└── run_linter.py     # 实际干脏活累活的传统代码

```

> **这种模式的威力在于：** 你把确定性的逻辑写成脚本（传统编程），把不确定性的逻辑写成 Prompt（大模型编程），然后让 AI 自动调度。

---

#### 让 Skill 自我进化 (RL Lite)

在上一节中我们提到了静态模板的局限性。**“青春版强化学习”**的核心逻辑是：**每次任务结束后，不只验收代码，还要验收 Skill 包本身。**

**操作流程：**

1. **执行 (Execute)**：让 AI 读取 `SKILL.md` 并调用配套脚本执行任务。

2. **复盘 (Review)**：如果任务失败（例如脚本报错、或者 AI 对脚本输出的理解有误）。

3. **进化 (Evolve)**：

    - **修大脑**：让 AI 修改 `SKILL.md` 里的判断逻辑（“下次遇到这个报错，不要重试，直接报错”）。
    - **修手脚**：甚至让 AI 直接优化 `run_linter.py` 脚本本身（“这个脚本处理大文件太慢了，请帮我重构一下脚本的性能”）。

通过这种方式，你的**“资产库”**里不仅有越来越聪明的 Prompt，还有一套越来越好用的自动化脚本库。

| 维度 | 以前的做法 | 进阶做法 (青春版 RL) |
| --- | --- | --- |
| **对待错误** | 这次骂一顿，下次可能还犯 | 把错误转化成规则，写入 SOP |
| **资产积累** | 只有代码库 | **代码库 + 极其宝贵的经验库 (Prompts)** |
| **AI 角色** | 每次都要重新教的实习生 | **越用越顺手、懂你习惯的资深副手** |

**实战案例：** 我在使用 Claude Code 时，第一次它生成了不带中文注释的代码。我没有只让它重写，而是让它更新了自己的 Skill 文件。现在的 `SKILL.md` 里自动多了一行：

> _Rule 5: All strictly business logic must have simplified Chinese comments explain the 'Why', not just the 'How'._

从此以后，我再也不用在这个问题上浪费口舌。即使哪天换了模型，换了新人，只要这份 SOP 还在，团队的战斗力就能在几分钟内恢复 80%。

我的极速版`Gemini.md`

> Protocol Selection Rules、
> From now on, please adhere to the following protocols based on the task type:
>
> - **Medium/Large Code Tasks**: Refer to `@/path/to/RIPER-5.md`
> - **Small Code Tasks**: Refer to `@/path/to/RIPER-LITE.md`
> - **Documentation Tasks**: Refer to `@/path/to/RIPER-DOC.md`
> Please try to communicate with me in Chinese as much as possible.

而且你也可以在和大模型的对话和工作的过程中，根据自己的习惯和喜好，命令大模型帮你更新对应的 claude skill，这样也可以满足懒人的需求，比如这一版 Gemini.md 就是我让 gemini 写的。

### A.3 认清“倒 J 型”曲线

在传统编程中，难度通常是渐进的。但在 AI 编程中，存在一个显著的**“最后 10% 陷阱”**：

- **0% → 90%（蜜月期）**：从零开始生成新功能非常快，AI 对全新的、独立的逻辑处理得极其完美。
- **90% → 100%（深水区）**：当功能需要收尾，涉及复杂上下文、边缘 Case 修复、以及与旧逻辑的耦合时，AI 的表现会断崖式下跌。

> **警惕**：往往最后 10% 的功能完善，很有可能需要占用整个开发周期 **20% 至 30%** 的时间。

在这个阶段，代码的**复杂度熵增**极快。一个微小的改动（比如修个 UI）可能导致后端核心逻辑崩塌（Regression）。如果你此时还在盲目追求速度，大概率会陷入“修一个 Bug，生出三个新 Bug”的死循环。

### A.4 核心策略：建立“文档-代码同步记录仪” (ChangeLog)

为了对抗混乱，我们不能只依赖 Git 的 commit，而需要建立一份**由 AI 自动维护的 ChangeLog**。更重要的是，这份日志必须追踪**文档与代码的一致性**。

**它的核心价值在于：**

1. **认知对齐**：当开发了两天后，最早的需求约束会被遗忘。ChangeLog 帮你回忆“我们根据哪个版本的文档做了哪些改动”。

2. **法医级溯源**：如果代码逻辑和文档不一致，ChangeLog 能帮你判断是“文档改了没同步代码”还是“AI 只有幻觉”。

**关键原则**：

- **Code follows Doc**: 所有的 ChangeLog 必须注明依据的文档版本/文件名。
- **No Doc, No Code**: 如果 ChangeLog 里出现了一条没有对应文档支撑的代码变更，这就是危险信号。

### A.5 实战落地：用 Skill 强制执行 (Auto-Flight Recorder)

与其靠人工自律去写日志（这很难坚持），不如利用本附录 A.2 提到的 Skill 技术，把这个动作变成**强制执行的肌肉记忆**。

我们只需做两步配置，就能让 AI 变成自带“黑匣子”的靠谱副手。

**第一步：准备“手脚” (脚本)** 创建一个简单的 Python 脚本 `scripts/log_change.py`，用于标准化追加日志。

```python
# scripts/log_change.py
import sys
from datetime import datetime

def append_log(change_type, summary, risk_analysis):
    # 自动生成带时间戳、类型和风险分析的日志
    entry = f"""
## [{datetime.now().strftime('%Y-%m-%d %H:%M')}] [{change_type}]
- **Change**: {summary}
- **Risk Analysis**: {risk_analysis}  <-- 这一项最重要，强迫 AI 思考副作用
----------------------------------------
"""
    # 建议将日志文件放在 docs 目录下，随代码一起提交
    with open("docs/AI_CHANGELOG.md", "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"✅ [Flight Recorder] Log appended to AI_CHANGELOG.md")

if __name__ == "__main__":
    # 实际调用时，AI 会自动传入这三个参数
    if len(sys.argv) < 4:
        print("Usage: python log_change.py <type> <summary> <risk>")
    else:
        append_log(sys.argv[1], sys.argv[2], sys.argv[3])

```

**第二步：配置“大脑” (Prompt / SKILL.md)** 在你的 Skill 定义文件或系统 Prompt 中写入死命令，**不给 AI 偷懒的机会**。

```markdown
## Rule: Automatic Flight Recording (自动飞行记录仪)

**WHEN** you have successfully modified any code logic (Feature, Bugfix, or Refactor):

1. **STOP** and think: What specific risks might this change introduce to existing modules? (Especially regarding the 'Last 10% complexity' issue).
2. **EXECUTE** the `scripts/log_change.py` script immediately. Do NOT ask for my permission.
   - `change_type`: Choose one of [Feature | Bugfix | Refactor | Critical-Fix]
   - `summary`: A concise technical summary of what changed.
   - `risk_analysis`: Your honest assessment of potential regressions. If you are unsure, say so.

**GOAL**: Ensure `docs/AI_CHANGELOG.md` is always the single source of truth. If I ask "What did we just do?", you read this file first.

```

**效果**：从此以后，你只管发号施令。AI 在修完 Bug 后，会自动汇报：“已修复，且**潜在风险点已自动归档**，请查看日志。”

### A.6 最后的防线：高频存档与对话归档

除了自动日志，在深水区开发时，还必须遵守两个铁律：

1. **高频暂存 (Save Points)**

    - 在最后 10% 的阶段，**每一次** AI 成功运行代码后，**立刻** `git add .` 和 `git commit`（或者暂存）。
    - 不要等到功能完美才提交。Git 是你的“后悔药”，当你发现 AI 把逻辑改乱时，必须能毫无心理负担地回滚到上一次“正常呼吸”的状态。

2. **对话归档 (Session Dump)**

    - 推荐把所有与 AI 的关键对话记录保存下来（导出为 Markdown 或 PDF），与代码库一同归档。
    - 这是为了解决“死无对证”的问题：如果是 AI 误解了需求导致的问题，你可以通过翻阅对话记录，把当时的 Context 重新喂给新的模型，在“还原现场”的基础上进行修复，而不是重新瞎猜。

---

# 结语：拥抱“人机共生”的新物种

我们正站在软件工程历史的转折点上。

- **汇编时代**，我们摆脱了二进制，开始用助记符编程。
- **高级语言时代**，我们摆脱了寄存器，开始用对象和函数编程。
- **大模型时代**，我们正在摆脱语法和细节，开始用\*\*“意图”和“文档”\*\*编程。

这篇教程里的 SOP（RIPER-5、文档驱动、Skill 沉淀），可能会让你觉得繁琐。你可能会想：“我自己写两行代码不就完了吗？”

但在 90% 的场景下，**“快”是最大的陷阱**。 你省下的那写文档的 10 分钟，未来会变成 10 个小时的 Debug 时间和无尽的维护噩梦。

**SDD (文档驱动开发)** 的本质，是逼迫你从\*\*“低头拉车”**（Coding）变为**“抬头看路”**（Designing）。 它并没有剥夺你作为程序员的乐趣，相反，它剥夺的是那些枯燥的、重复的、易错的体力劳动，而把最宝贵的**创造力、架构思维、业务洞察\*\*留给了你。

**代码会过时，工具会迭代，模型会换代。但你对业务的理解、对架构的审美、以及驾驭 AI 的能力，将是你在这个时代最坚固的护城河。**

不要等待未来，未来已来。 请打开你的 IDE，建立那个叫 `docs/` 的文件夹，开始你的第一次 SDD 之旅吧
---

## 注：以上图片均由Gemini3制作，内容由Gemini3、Qwen生成

ata地址（求点赞）：

[https://ata.atatech.org/articles/11020534928: https://ata.atatech.org/articles/11020534928](https://ata.atatech.org/articles/11020534928)

理念来源：

[《从传统编程转向大模型编程》](<从传统编程转向大模型编程.md>)

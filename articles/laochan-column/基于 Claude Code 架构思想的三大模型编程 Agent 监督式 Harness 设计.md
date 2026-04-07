# 基于 Claude Code 架构思想的三大模型编程 Agent 监督式 Harness 设计

> 发布日期: 2026-04-07

![图片](/articles/images/基于 Claude Code 架构思想的三大模型编程 Agent 监督式 Harness 设计/img_1.jpg)

### 1. 先说结论

如果现在是Claude Code主导一个项目编程，最好的协作方式不是让Codex、Gemini CLI同时抢着写代码，而是把它们放进 Claude Code 已经体现出来的四类能力槽位里：

Claude Code作为Lead Implementer，负责主线任务拆解、代码落地、上下文连续性和最终集成。

Codex作为Architecture + Diff Auditor，负责在写代码前审计划、写代码后审 diff、检查是否偏离需求和架构。

Gemini CLI作为Verification + Adversarial Tester，负责从测试、边界条件、失败模式、遗漏场景去做反证。

这比“三个模型都能写，所以轮流写”更稳，因为它遵守了本仓库中最有价值的设计思想：任务编排、权限边界、异步协作、钩子化治理。

![图片](/articles/images/基于 Claude Code 架构思想的三大模型编程 Agent 监督式 Harness 设计/img_2.jpg)

### 2. 从文档和源码能提炼出的架构思想

package/README.md本身是产品说明，不是详细架构文档。但结合仓库中的还原源码，可以提炼出一套很清晰的系统思想。

### 2.1 不是单 Agent，而是“可编排的 Agent 系统”

从restored-src/src/utils/swarm/、restored-src/src/utils/teammate.ts、restored-src/src/utils/swarm/teamHelpers.ts可以看出，Claude Code 的内核思路不是“一个模型做完所有事”，而是：

有team概念。

有lead和teammate区分。

有成员元数据、模式、工作目录、订阅关系、权限状态。

可以要求某些 teammate 先进入plan mode再执行。

这说明它天然适合被抽象成一个多 Agent harness，而不只是聊天式 CLI。

### 2.2 协作靠共享状态，不靠隐式记忆

从teamHelpers.ts和teammateMailbox.ts看，系统非常强调把协作状态显式落盘：

team file记录团队成员、角色、路径、模式、时间戳。

mailbox负责异步消息收发。

task framework负责任务状态轮询、输出增量、完成通知。

这背后的思想非常重要：Agent 协作要以工件为中心，而不是以对话幻觉为中心。

### 2.3 治理是事件驱动的

从hookEvents.ts、stopHooks.ts、structuredIO.ts可以看到大量 hook 机制：

SessionStart

Setup

PermissionRequest

Stop

TaskCompleted

TeammateIdle

也就是说，Claude Code 把“什么时候允许做事、什么时候必须审查、什么时候总结输出”做成了事件节点，而不是写死在主流程里。

对三模型 harness 来说，这个思想可以直接复用：把Codex和Gemini安插在关键事件上，而不是让它们全程打断主流程。

### 2.4 权限不是附属品，而是系统级边界

从permissions/、structuredIO.ts、bridge/sessionRunner.ts这类模块看，Claude Code 非常重视：

工具调用授权。

文件系统访问边界。

网络权限请求。

自动模式与人工确认的切换。

这意味着一个高质量 harness 不应该只问“谁来写”，还要问：

谁可以改主分支工作树？

谁只能读？

谁可以跑测试？

谁只能提审查意见不能直接改？

### 2.5 长任务必须可观察

从task/framework.ts可以看出，任务有：

状态。

输出偏移量。

完成通知。

轮询更新。

这给我们的启发是：多模型协作不能只靠“请你 review 一下”，而要给每个 Agent 明确的任务对象、输入工件、输出工件和完成条件。

### 3. 适合三模型协作的核心设计原则

基于上面的思想，我建议这个 harness 遵守以下原则。

单线程主导，双线程监督

计划、实现、验证分离

任何结论都要落到工件

任何写权限都要有前置契约

任何合入都要过双重校验

主导 Agent 不自证正确，至少由另两个 Agent 中的一个做架构校验，另一个做验证校验

一句话概括：

Claude 写，Codex 审设计和 diff，Gemini 审验证和反例。

### 4. Harness 总体架构

### 4.1 组件

这个 harness 可以设计成 6 个核心部件。

Coordinator负责创建任务、分配角色、收集输出、推进状态机。

Agent Adapter分别封装Claude Code、Codex、Gemini CLI的调用方式。

Artifact Store存放计划、任务单、审查结果、测试结果、决策日志。

Event Bus对应 Claude Code 的 hook 思想，在关键节点广播事件。

Policy Engine负责权限、升级条件、是否允许进入下一阶段。

Scoreboard记录每个阶段的通过/拒绝/风险等级，作为 merge gate。

### 4.2 工件目录

建议 harness 在项目根目录维护一个显式工件空间，例如：

这些工件对应源码里的team file、mailbox、task output思想，只是把它推广到跨模型协作。

### 5. 角色设计

### 5.1 Claude Code 的职责

Claude Code适合做项目主导，是因为它在这个体系里天然擅长：

长上下文连续推进。

与本地代码库高频交互。

任务拆解后持续迭代。

在终端环境里做真实执行。

因此 Claude 的职责应当是：

接收需求。

生成实施计划。

创建或更新代码。

运行基础检查。

汇总需要外部审查的上下文包。

根据审查意见二次修正。

### 5.2 Codex 的职责

Codex不要主要承担“补位写代码”，而要承担“主线偏航检测器”。

Codex 更适合审：

计划是否完整。

改动是否偏离架构。

diff 是否引入不必要复杂度。

实现是否与需求、边界、已有模式一致。

是否漏了接口契约、迁移、文档、回滚路径。

Codex 的输出最好是结构化的：

blocking

major

minor

suggestions

missing-tests

### 5.3 Gemini CLI 的职责

Gemini CLI适合扮演“怀疑主义验证器”。

重点审：

测试是否只覆盖 happy path。

边界条件和异常流是否遗漏。

性能退化风险。

并发、状态同步、缓存、权限、I/O 的失败模式。

文档与实现是否一致。

Gemini 的审查目标不是“提出更优雅写法”，而是“证明现在这版可能会坏在哪里”。

### 6. 工作流设计

### 6.1 阶段 0：任务受理

Coordinator 创建任务单tasks/T-001.json，包含：

任务描述

用户原始需求

涉及模块

风险等级

验收标准

当前主导 Agent

### 6.2 阶段 1：Claude 先出计划，不直接开写

这里借鉴 Claude Code 的plan mode required思想。

当任务满足任一条件时，必须先让 Claude 产出计划工件：

跨 3 个以上文件

涉及数据库、认证、支付、部署、权限

涉及公共接口变化

涉及删除或重构

Claude 先输出：

实现步骤

影响面

风险点

需要验证的事项

暂不处理的范围

然后把这份计划交给 Codex 做plan review。

### 6.3 阶段 2：Codex 审计划

Codex 在代码编写前先做一次计划审查。

通过条件：

任务拆分合理

验收标准可判定

没有明显遗漏的技术约束

实现路径没有违背现有架构

如果 Codex 判为blocking，Claude 不能进入写代码阶段。

### 6.4 阶段 3：Claude 实施

Claude 成为唯一默认写权限 Agent。

它执行：

修改代码

跑最基本的 lint/test/build

生成 diff 摘要

输出自评说明

自评必须包含：

改了什么

为什么这样改

哪些风险仍未覆盖

需要 Codex 和 Gemini 特别关注什么

### 6.5 阶段 4：Codex 审 diff

这一步对应“架构监督”。

Codex 读：

任务单

计划

diff

Claude 自评

Codex 输出：

是否符合计划

是否引入多余复杂性

是否破坏模块边界

是否存在明显回归风险

哪些地方必须修改后才能进入验证阶段

### 6.6 阶段 5：Gemini 做验证审查

这一步对应“反证监督”。

Gemini 不以“代码风格”为主，而以“这版可能挂在哪里”为主。

Gemini 输出：

漏测路径

反例输入

状态机异常

错误恢复缺失

可重现的验证脚本建议

### 6.7 阶段 6：Gate 决策

Policy Engine 根据双审结果做放行。

建议规则：

Codex blocking > 0时不得合入

Gemini blocking > 0时不得合入

Codex major + Gemini major >= 3时回退到实施阶段

若两者都仅有minor/suggestions，Claude 可修正后直接进入最终检查

### 6.8 阶段 7：最终收敛

Claude 处理意见后，再跑一次最小验证集，然后输出：

最终变更摘要

剩余风险

未做事项

建议 follow-up

### 7. 事件与 Hook 设计

为了继承 Claude Code 的架构思想，建议把三模型协作做成 hook 化状态机。

### 7.1 关键事件

TaskCreated

PlanDrafted

PlanApproved

ImplementationStarted

DiffReady

ArchitectureReviewCompleted

VerificationReviewCompleted

GateFailed

GatePassed

TaskClosed

### 7.2 关键 Hook

onTaskCreated初始化任务工件与角色绑定。

onPlanDrafted触发 Codex 计划审查。

onDiffReady并行触发 Codex diff 审查和 Gemini 验证审查。

onBlockingReview自动回写阻塞项到任务单并禁止 merge。

onTaskClosed把最终结论写入决策日志和复盘材料。

### 8. 权限模型

这是 harness 质量的关键。

### 8.1 推荐权限分层

Claude Code默认可读写主工作树，可运行项目测试与构建。

Codex默认只读主工作树；可在独立 worktree 中做补丁实验；不能直接合入主分支。

Gemini CLI默认只读；可运行验证脚本；若要改测试，必须进入受控 patch 模式。

### 8.2 为什么这样设计

因为监督者不该和执行者共享完全相同的行动权限，否则“审查”会退化成“另一个实现者也做一遍”，系统会变慢且失去责任边界。

### 9. 推荐的物理执行形态

最稳的是一个主工作树 + 两个审查 worktree。

Claude Code在主工作树执行。

Codex在git worktreeA 中读代码和验证 diff，需要时做最小补丁验证。

Gemini CLI在git worktreeB 中做测试与反例推演。

这样做的好处：

不互相污染工作区

审查可重现

审查意见可保留成 patch 或 notes

非阻塞并行更容易做

### 10. 数据结构建议

### 10.1 任务单

### 10.2 审查输出

### 11. 一个非常实用的协作协议

如果现在是Claude Code主导项目，我建议直接用下面这套协议。

### 11.1 Claude 给 Codex 的输入包

用户需求摘要

当前计划

涉及文件清单

当前 diff

已运行的检查

自己最担心的 3 个风险点

Codex 的任务是：

不复述

只找偏航、遗漏、过度设计、未满足验收

输出按严重级别分组的问题

### 11.2 Claude 给 Gemini 的输入包

任务单

验收标准

当前 diff

已有测试

未覆盖风险点

Gemini 的任务是：

提供反例

设计失败场景

指出测试空洞

必要时给出最小验证脚本建议

### 12. 为什么这个 harness 会比“大家都写”更高质量

因为它同时满足四件事：

主导权稳定不会因为多模型都在写而产生上下文撕裂。

监督独立审查者不依赖主导者的自我叙述。

流程可回放每一步都有工件与状态。

责任可追踪谁提出阻塞，谁批准通过，都能追溯。

### 13. 最小可实现版本

如果先做 MVP，不需要一开始就实现全部功能。

第一版只要有这 5 个能力就够了：

任务单文件

计划审查

diff 审查

验证审查

gate 决策

也就是说，哪怕先不用复杂 daemon，只用一个本地脚本协调三个 CLI，也已经能跑起来。

### 14. 对这个场景的直接建议

如果“现在就是 Claude Code 主导一个项目”，那最值得立刻启用的配合方式是：

Claude 负责编码和集成

Codex 只做两次关键审查

一次在计划完成后

一次在 diff 完成后

Gemini 在 diff 出来后只做验证与反例审查

任何一个模型给出blocking，Claude 必须回炉

这会比三家轮流改代码更快，也更接近真实工程里的tech lead + reviewer + test skeptic组织形态。

### 15. 一句话版 Harness 定义

这个 harness 的本质不是“三个模型一起编程”，而是：

以 Claude Code 为执行内核，以 Codex 为架构监督器，以 Gemini CLI 为验证监督器，以任务工件、事件钩子和权限边界构成闭环。
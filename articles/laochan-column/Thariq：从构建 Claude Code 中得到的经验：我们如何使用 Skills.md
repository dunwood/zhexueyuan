# Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills

> 发布日期: 2026-04-07

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_1.jpg)

Skills 已经成为 Claude Code 中使用最频繁的扩展点之一。它们灵活、易于制作，也便于分发。

但这种灵活性也使得人们很难知道，究竟什么做法效果最好。什么类型的 skill 值得去做？写一个好 skill 的秘诀是什么？又该在什么时候把它分享给别人？

在 Anthropic 内部，我们已经在 Claude Code 中广泛使用 skills，目前活跃使用中的已有数百个。这些就是我们在使用 skills 来加速开发过程中学到的经验。

**什么是 Skills？**

如果你刚接触 skills，我建议你先去读我们的文档，或者看看我们在新的 Skilljar 上关于 Agent Skills 的最新课程。本文会假定你已经对 skills 有一些基本了解。

关于 skills，一个常见误解是它们“不过就是 markdown 文件”，但 skills 最有意思的地方恰恰在于：它们并不只是文本文件。它们是文件夹，里面可以包含脚本、资源文件、数据等等，agent 可以发现、探索并操作这些内容。

在 Claude Code 中，skills 还拥有非常丰富的配置选项，包括注册动态 hooks。

我们发现，Claude Code 中一些最有意思的 skills，正是创造性地利用了这些配置选项和文件夹结构。

**Skills 的类型**

在把我们所有的 skills 归类整理之后，我们发现它们会聚集到几个反复出现的类别中。最好的 skill 往往能清晰地归入其中某一类；而那些更让人困惑的，通常横跨了好几类。这并不是一个最终版清单，但它是一个很好的思考框架，可以帮助你判断你的组织内部是否缺了某类 skill。

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_2.jpg)

**1. 库与 API 参考**

这类 skill 用来解释如何正确使用某个库、CLI 或 SDK。它们既可以针对内部库，也可以针对 Claude Code 有时不太擅长处理的常见库。这类 skill 通常会包含一个参考代码片段文件夹，以及一份 Claude 在写脚本时应避免的坑点清单。

**示例：**billing-lib —— 你的内部计费库：边界情况、易踩坑点等。internal-platform-cli —— 你的内部 CLI 包装器的每个子命令，以及何时使用它们的示例。frontend-design —— 让 Claude 更擅长你的设计系统。

**2. 产品验证**

这类 skill 描述如何测试或验证你的代码是否正常工作。它们通常会和外部工具配合使用，比如 playwright、tmux 等，来执行验证过程。

验证类 skills 对于确保 Claude 输出正确非常有用。甚至值得让一位工程师花上一整周时间，只为了把你的验证类 skills 打磨到非常出色。

可以考虑一些技巧，比如让 Claude 录制自己输出结果的视频，这样你就能准确看到它测试了什么；或者在每一步都强制执行程序化断言来验证状态。这些通常是通过在 skill 中包含多种脚本来实现的。

**示例：**signup-flow-driver —— 在无头浏览器中跑完注册 → 邮箱验证 → onboarding 流程，并带有各步骤状态断言 hooks。checkout-verifier —— 使用 Stripe 测试卡驱动结账界面，并验证发票是否确实进入正确状态。tmux-cli-driver —— 用于交互式 CLI 测试，适合你要验证的对象需要一个 TTY 的情况。

**3. 数据获取与分析**

这类 skill 会连接到你的数据和监控栈。它们可能会包含用于带凭证拉取数据的库、特定 dashboard 的 id，以及常见工作流或获取数据的方法说明。

**示例：**funnel-query —— “要看 signup → activation → paid，需要 join 哪些事件”，以及真正包含规范 user_id 的那张表。cohort-compare —— 比较两个 cohort 的留存或转化，标出统计上显著的差异，并链接到 segment 定义。grafana —— 数据源 UID、集群名称、问题 → dashboard 对照表。

**4. 业务流程与团队自动化**

这类 skill 把重复性的工作流自动化为一个命令。它们通常只是相对简单的说明，但也可能依赖其他更复杂的 skills 或 MCP。对于这类 skill，把之前的结果保存在日志文件里，有助于模型保持一致性，并能回顾此前对该工作流的执行情况。

**示例：**standup-post —— 聚合你的工单追踪器、GitHub 活动和先前的 Slack 内容，输出格式化的 standup，只包含变化部分。create--ticket —— 强制执行 schema（合法枚举值、必填字段），以及创建后的后续流程（提醒 reviewer、在 Slack 中贴链接）。weekly-recap —— 已合并 PR + 已关闭工单 + 部署记录 → 格式化的周总结帖。

**5. 代码脚手架与模板**

这类 skill 用于为代码库中的特定功能生成框架样板。你可以把这些 skill 与可组合的脚本结合使用。当你的脚手架里包含一些无法仅通过代码覆盖的自然语言需求时，它们尤其有用。

**示例：**new--workflow —— 为新的 service/workflow/handler 生成带有你注释风格的脚手架。new-migration —— 你的 migration 文件模板，以及常见坑点。create-app —— 一个新的内部 app，预先接好了认证、日志和部署配置。

**6. 代码质量与评审**

这类 skill 用来在你的组织内部执行代码质量规范，并帮助做代码评审。它们可以包含确定性的脚本或工具，以保证尽可能高的稳健性。你可能会希望把这些 skill 自动运行起来，比如作为 hooks 的一部分，或者放在 GitHub Action 中执行。

adversarial-review —— 启动一个“新鲜眼光”的子 agent 来挑错，实施修复，不断迭代，直到问题只剩吹毛求疵的小毛病。code-style —— 执行代码风格规范，尤其是 Claude 默认做得不太好的那些风格。testing-practices —— 关于如何写测试以及测试什么的说明。

**7. CI/CD 与部署**

这类 skill 帮助你在代码库中获取、推送和部署代码。这些 skill 可能会引用其他 skill 来收集数据。

**示例：**babysit-pr —— 监控一个 PR → 重试不稳定的 CI → 解决合并冲突 → 启用自动合并。deploy- —— 构建 → smoke test → 逐步放量 → 对比错误率 → 回归时自动回滚。cherry-pick-prod —— 隔离 worktree → cherry-pick → 冲突解决 → 按模板发起 PR。

**8. Runbooks（运维手册类）**

这类 skill 接收一个症状（例如 Slack 线程、告警或错误签名），通过多工具调查流程进行排查，并产出结构化报告。

**示例：**-debugging —— 为你的高流量服务建立“症状 → 工具 → 查询模式”的映射。oncall-runner —— 拉取告警 → 检查常见嫌疑项 → 格式化输出调查结论。log-correlator —— 给定一个 request ID，拉取所有可能处理过它的系统中的匹配日志。

**9. 基础设施运维操作**

这类 skill 执行例行维护和运维流程——其中有些操作具有破坏性，因此会受益于额外的防护措施。它们能让工程师更容易在关键操作中遵循最佳实践。

**示例：**-orphans —— 找出孤儿 pods/volumes → 发到 Slack → 等待观察期 → 用户确认 → 级联清理。dependency-management —— 你们组织内部的依赖审批流程。cost-investigation —— “为什么我们的存储/出口流量账单暴涨了”，附带具体 bucket 和查询模式。

**制作 Skills 的技巧**

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_3.jpg)

一旦你决定好了要做什么 skill，接下来该怎么写？以下是我们发现的一些最佳实践、技巧和窍门。

我们最近也发布了 Skill Creator，让你在 Claude Code 中更容易创建 skills。

**不要陈述显而易见的东西**

Claude Code 对你的代码库已经知道很多，而 Claude 对编程也知道很多，包括许多默认偏好。如果你发布的 skill 主要是知识型的，那就尽量专注于那些能把 Claude 从它常规思路中“拉出来”的信息。

frontend design skill 就是一个很好的例子——它是 Anthropic 的一位工程师通过与客户反复迭代、不断提升 Claude 设计品味而构建出来的，目的是避开诸如 Inter 字体和紫色渐变这些经典套路。

**建立一个 Gotchas（坑点）章节**

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_4.jpg)

任何 skill 中信号密度最高的内容，就是 Gotchas 章节。这些章节应当建立在 Claude 使用你的 skill 时经常会遇到的失败点之上。理想情况下，你会随着时间持续更新 skill，把这些 gotchas 不断积累进去。

**使用文件系统与渐进式披露**

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_5.jpg)

就像前面说的，skill 是一个文件夹，而不只是一个 markdown 文件。你应该把整个文件系统都当成一种上下文工程和渐进式披露的手段。告诉 Claude 你的 skill 中有哪些文件，它会在合适的时候去读取它们。

最简单的渐进式披露形式，就是指向其他 markdown 文件供 Claude 使用。比如，你可以把详细的函数签名和用法示例拆分到 references/api.md 中。

再比如，如果你的最终输出是一个 markdown 文件，你可以在 assets/ 中放一个模板文件，供它复制和使用。

你可以有 references、scripts、examples 等各种文件夹，这些都会帮助 Claude 更有效地工作。

**不要把 Claude 限死在轨道上**

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_6.jpg)

Claude 通常会尽量遵循你的指令，而因为 Skills 是高度可复用的，所以你要小心，不要把说明写得过于具体。给 Claude 它所需要的信息，但也要给它适应具体情境的灵活性。比如：

**认真考虑 Setup（初始化配置）**

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_7.jpg)

有些 skill 可能需要先根据用户提供的上下文做初始化。例如，如果你做的是一个把 standup 发到 Slack 的 skill，你可能希望 Claude 先问一下该发到哪个 Slack channel。

实现这种模式的一个好办法，是把这些初始化信息存到 skill 目录里的 config.json 文件中，就像上面的例子那样。如果配置尚未完成，agent 就可以向用户询问信息。

如果你想让 agent 以结构化、多选题的形式向用户提问，你可以指示 Claude 使用 AskUserQuestion 工具。

**Description 字段是写给模型看的**

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_8.jpg)

当 Claude Code 开始一个 session 时，它会建立一份所有可用 skill 及其 description 的列表。Claude 会扫描这份列表，来决定“这个请求有没有对应的 skill？”这意味着，description 字段不是摘要——它实际上是在描述，什么时候应该触发这个 PR。

**记忆与数据存储**

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_9.jpg)

有些 skill 可以通过在其内部存储数据来拥有一种“记忆”能力。你可以把数据存成很简单的追加式文本日志文件或 JSON 文件，也可以做得复杂一些，比如用 SQLite 数据库。

例如，一个 standup-post skill 可能会保留一个 standups.log，里面存着它写过的每一次 standup。这样，下次你再运行它时，Claude 会读取它自己的历史记录，并能告诉你从昨天到今天发生了哪些变化。

存储在 skill 目录中的数据，在你升级 skill 时可能会被删除，因此你应该把这些内容存到一个稳定目录中。到目前为止，我们提供了${CLAUDE_PLUGIN_DATA}，作为每个 plugin 的稳定存储目录。

**存放脚本并生成代码**

你能给 Claude 的最强大工具之一，就是代码。给 Claude 提供脚本和库，可以让 Claude 把它的轮次花在组合与决策“下一步该做什么”上，而不是重复重建那些样板代码。

比如，在你的数据科学 skill 中，你可以放一个函数库，用于从事件源获取数据。为了让 Claude 能做复杂分析，你可以给它一组辅助函数，像这样：

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_10.jpg)

Claude 接着就可以临时生成脚本，把这些功能组合起来，去完成更高级的分析，例如回答“周二到底发生了什么？”这样的提示。

![图片](/articles/images/Thariq：从构建 Claude Code 中得到的经验：我们如何使用 Skills/img_11.jpg)

**按需 Hooks**

Skills 可以包含 hooks，并且这些 hooks 只有在 skill 被调用时才会激活，并持续整个 session。你可以把它用在那些更有主张的 hooks 上——它们不适合一直运行，但在某些情况下极其有用。

例如：

/careful —— 通过 Bash 上的 PreToolUse matcher 阻止 rm -rf、DROP TABLE、force-push、kubectl delete。只有当你知道自己在碰生产环境时才想开启它——如果一直开着，简直会把你逼疯。/freeze —— 阻止任何不在某个特定目录中的 Edit/Write 操作。当你在 debug 时它非常有用：“我只是想加点日志，但我总是不小心‘顺手修复’了其他无关的东西。”

**分发 Skills**

Skills 最大的好处之一，就是你可以把它们分享给团队中的其他人。

你有两种方式可以把 skill 分享给别人：

把 skills 提交进你的 repo（放在./.claude/skills下面）做成一个 plugin，并建立 Claude Code Plugin marketplace，让用户可以上传和安装 plugins（更多内容请查看文档）

对于那些在相对较少 repo 之间协作的小团队来说，把 skills 直接提交进 repo 往往效果很好。但每一个被提交进去的 skill，也都会给模型上下文增加一点负担。随着规模扩大，内部 plugin marketplace 则允许你分发 skills，并让团队成员自己决定安装哪些。

**管理 Marketplace**

你怎么决定哪些 skill 应该进入 marketplace？人们又该如何提交它们？

我们并没有一个中央团队来统一决定；相反，我们会尝试自然地找出那些最有用的 skill。如果你有一个想让别人试用的 skill，你可以先把它上传到 GitHub 里的 sandbox 文件夹中，然后在 Slack 或其他论坛中告诉大家去试。

一旦某个 skill 获得了足够的 traction（至于算不算足够，由 skill 的 owner 自己决定），他们就可以提一个 PR，把它移入 marketplace。

需要提醒一点：创建糟糕或冗余的 skill 是很容易的，所以在正式发布之前，确保你有某种策展或筛选机制是很重要的。

**组合 Skills**

你可能会希望某些 skill 彼此依赖。例如，你可能有一个文件上传 skill，负责上传文件；还有一个 CSV 生成 skill，负责生成 CSV 并上传。这种依赖管理目前在 marketplace 或 skills 中还没有原生支持，但你可以直接通过名字引用其他 skill，而模型如果已经安装了它们，就会调用它们。

**衡量 Skills**

为了了解一个 skill 的表现，我们会使用一个 PreToolUse hook，在公司内部记录 skill 的使用情况（示例代码见这里）。这意味着，我们可以找出哪些 skill 很受欢迎，或者哪些 skill 的触发频率低于我们的预期。

**结论**

对于 agents 来说，Skills 是极其强大而灵活的工具，但这件事仍然很早期，我们所有人都还在摸索怎样最好地使用它们。

与其把这篇文章看成一份权威指南，不如把它当成一包实用技巧：这些都是我们观察到确实有效的做法。理解 skills 的最好方式，就是直接开始、动手实验，看看什么对你有效。我们的大多数 skill 一开始都只是几行内容和一个 gotcha，后来之所以变得更好，是因为随着 Claude 遇到新的边界情况，人们不断往里面补充内容。

希望这篇文章对你有帮助。如果你有任何问题，欢迎告诉我。
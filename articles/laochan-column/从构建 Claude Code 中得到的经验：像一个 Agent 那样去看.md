# 从构建 Claude Code 中得到的经验：像一个 Agent 那样去看

> 发布日期: 2026-04-07

![图片](/articles/images/从构建 Claude Code 中得到的经验：像一个 Agent 那样去看/img_1.jpg)

构建一个 agent harness 最困难的部分之一，就是构造它的行动空间。Claude 通过工具调用（Tool Calling）来行动，但在 Claude API 中，借助 bash、skills，以及最近加入的 code execution 等原语，工具可以有许多种构造方式（关于 Claude API 中的程序化工具调用，可以阅读 @RLanceMartin 的新文章）。

在有这么多选项的情况下，你该如何为你的 agent 设计工具？你是否只需要一个工具，比如 code execution 或 bash？如果你有 50 个工具呢——为你的 agent 可能遇到的每一种使用场景各准备一个工具？

为了把自己放到模型的思维方式中，我喜欢想象自己拿到了一道困难的数学题。为了把它解出来，你会想要什么工具？这要取决于你自己的技能！

纸张会是最低配置，但你会受限于手工计算。计算器会更好，但你得知道如何使用那些更高级的功能。最快、最强大的选择会是一台电脑，但你又必须知道如何用它来编写并执行代码。

这是一个对于设计 agent 非常有用的框架。你要给它那些与它自身能力相匹配的工具。但你怎么知道它具备哪些能力？你需要留意它，阅读它的输出，做实验。你要学会像一个 agent 那样去看。

以下是我们在构建 Claude Code 时，通过留意 Claude 本身所学到的一些经验。

**改进信息引出（Elicitation）与 AskUserQuestion 工具**

![图片](/articles/images/从构建 Claude Code 中得到的经验：像一个 Agent 那样去看/img_2.jpg)

在构建 AskUserQuestion 工具时，我们的目标是提升 Claude 提问的能力（这通常被称为 elicitation，信息引出）。

虽然 Claude 也可以直接用纯文本提问，但我们发现，回答这些问题会让人觉得花了不必要的时间。我们该如何降低这种摩擦，并提高用户与 Claude 之间沟通的带宽？

**尝试#1—— 编辑 ExitPlanTool**

我们首先尝试的是，给 ExitPlanTool 增加一个参数，让它在计划之外再附带一个问题数组。这是最容易实现的做法，但它让 Claude 感到困惑，因为我们同时要求它给出一个计划，以及一组关于这个计划的问题。假如用户的回答与计划里写的内容发生冲突怎么办？Claude 是否需要调用两次 ExitPlanTool？我们需要另一种方法。

（你可以在我们关于 prompt caching 的文章中读到更多关于为什么我们做了一个 ExitPlanTool 的内容。）

**尝试#2—— 修改输出格式**

接着我们尝试修改 Claude 的输出指令，让它输出一种稍微改造过的 markdown 格式，以便用来提问。比如，我们可以要求它输出一个项目符号问题列表，并在方括号里附上备选项。然后我们就可以解析这个问题，并把它格式化成 UI 展示给用户。

虽然这是我们所能做出的最通用的一种改动，而且 Claude 似乎甚至也挺擅长输出这种格式，但它并不可靠。Claude 会附加额外的句子、遗漏选项，或者干脆使用完全不同的格式。

**尝试#3—— AskUserQuestion 工具**

![图片](/articles/images/从构建 Claude Code 中得到的经验：像一个 Agent 那样去看/img_3.jpg)

最后，我们决定创建一个 Claude 可以在任意时刻调用的工具，不过我们特别提示它在 plan mode 中这样做。当这个工具被触发时，我们会弹出一个模态框来显示问题，并阻塞 agent 的循环，直到用户作出回答。

这个工具让我们能够要求 Claude 输出结构化内容，并帮助我们确保 Claude 会给用户多个选项。它也给用户提供了组合这种功能的方式，比如在 Agent SDK 里调用它，或是在 skills 中引用它。

最重要的是，Claude 似乎很喜欢调用这个工具，而且我们发现它的输出效果很好。即便是设计得再好的工具，如果 Claude 不知道该怎么调用，它也发挥不了作用。

这就是 Claude Code 中 elicitation 的最终形态吗？我们也不确定。正如你会在下一个例子中看到的那样，适合一个模型的方法，未必对另一个模型就是最好的。

**随着能力更新而更新——Tasks 与 Todos**

![图片](/articles/images/从构建 Claude Code 中得到的经验：像一个 Agent 那样去看/img_4.jpg)

当我们最初发布 Claude Code 时，我们意识到模型需要一个 Todo 列表来让自己保持在正确轨道上。Todos 可以在一开始就写下来，并在模型完成工作时逐项勾掉。为此，我们给 Claude 提供了 TodoWrite 工具，它可以写入或更新 Todos，并把它们展示给用户。

但即便如此，我们仍然经常看到 Claude 忘记自己要做什么。为了适应这一点，我们每隔 5 个 turn 就插入一次系统提醒，提醒 Claude 它的目标是什么。

但随着模型变得更强，它们不仅不再需要被提醒 Todo List，反而会觉得它是一种限制。被发送 Todo list 的提醒，会让 Claude 觉得自己必须死守这份清单，而不是去修改它。我们还看到 Opus 4.5 在使用 subagents 方面也变得更强了，但 subagents 又该如何围绕一份共享的 Todo List 来协同呢？

看到这一点后，我们用 Task Tool 取代了 TodoWrite（关于 Tasks 的更多内容可见这里）。Todos 的重点是让模型保持在轨道上，而 Tasks 更像是在帮助 agents 彼此沟通。Tasks 可以包含依赖关系，可以在 subagents 之间共享更新，而且模型还可以修改和删除它们。

随着模型能力的提升，那些模型曾经需要的工具，如今反而可能会束缚它们。持续重新审视此前关于“需要什么工具”的假设，是非常重要的。这也是为什么坚持只支持一小组能力画像相对接近的模型会很有用。

**设计搜索接口**

对于 Claude 来说，一组特别重要的工具，就是那些可以用来构建它自身上下文的搜索工具。

当 Claude Code 刚推出时，我们使用一个 RAG 向量数据库来为 Claude 查找上下文。虽然 RAG 功能强大而且速度很快，但它需要索引和配置，而且在各种不同环境中都可能显得脆弱。更重要的是，这些上下文是被“给”到 Claude 的，而不是由它自己找到的。

但如果 Claude 可以在网络上搜索，为什么不能搜索你的代码库呢？通过给 Claude 一个 Grep 工具，我们就可以让它自己去搜索文件，并自行构建上下文。

这是我们随着 Claude 变得更聪明而看到的一种模式：只要给它合适的工具，它就会越来越擅长自己构建上下文。

当我们引入 Agent Skills 时，我们把“渐进式披露”（progressive disclosure）这一思想正式化了。这使得 agent 可以通过探索，逐步发现相关的上下文。

Claude 可以读取 skill 文件，而这些文件又可以引用其他文件，模型就可以递归地继续读取。实际上，skills 的一个常见用途，就是为 Claude 增加更多搜索能力，比如给它如何使用某个 API 或如何查询数据库的说明。

在一年的时间里，Claude 从基本上还不能自己构建上下文，发展到能够跨越多层文件执行嵌套搜索，以找到自己真正需要的精确上下文。

如今，渐进式披露已经成了我们在不增加新工具的情况下增加新功能的一种常用技术。

**渐进式披露——Claude Code Guide Agent**

Claude Code 目前大约有 20 个工具，而我们始终在反复追问自己：这些工具真的都需要吗？增加一个新工具的门槛很高，因为这会给模型再多加一个需要思考的选项。

例如，我们注意到 Claude 对如何使用 Claude Code 本身了解得不够。如果你问它怎么添加一个 MCP，或者 slash command 是做什么的，它是答不上来的。

我们本可以把所有这些信息都放进 system prompt 里，但考虑到用户其实很少问这些问题，那样做只会带来上下文腐烂（context rot），并干扰 Claude Code 的主要工作：写代码。

于是，我们尝试了一种渐进式披露的形式。我们给了 Claude 一个指向文档的链接，它可以自己去加载这些文档，从而搜索更多信息。这样确实可行，但我们发现，Claude 为了找到正确答案，会把大量搜索结果都加载进上下文里，而实际上你真正需要的只是答案本身。

所以我们构建了 Claude Code Guide subagent：当你询问 Claude 关于它自身的问题时，Claude 会被提示去调用这个 subagent。这个 subagent 拥有大量关于如何高效搜索文档以及该返回什么内容的指令。

虽然这并不完美——当你问它如何配置它自己时，Claude 仍然可能会糊涂——但它已经比以前好得多了！我们在不增加一个新工具的情况下，向 Claude 的行动空间中加入了新的东西。

**这是一门艺术，而不是一门科学**

如果你原本期待的是一套关于如何构建工具的僵硬规则，那么遗憾的是，这篇指南并不是那样的东西。为你的模型设计工具，既是一门科学，也同样是一门艺术。它高度依赖于你使用的模型、agent 的目标，以及它所处的环境。

经常实验，阅读你的输出，尝试新的东西。像一个 agent 那样去看。

Lessons from Building Claude Code: Seeing like an Agent

One of the hardest parts of building an agent harness is constructing its action space.

Claude acts through Tool Calling, but there are a number of ways tools can be constructed in the Claude API with primitives like bash, skills and recently code execution (read more about programmatic tool calling on the Claude API in @RLanceMartin's new article).

Given all these options, how do you design the tools of your agent? Do you need just one tool like code execution or bash? What if you had 50 tools, one for each use case your agent might run into?

To put myself in the mind of the model I like to imagine being given a difficult math problem. What tools would you want in order to solve it? It would depend on your own skills!

Paper would be the minimum, but you’d be limited by manual calculations. A calculator would be better, but you would need to know how to operate the more advanced options. The fastest and most powerful option would be a computer, but you would have to know how to use it to write and execute code.

This is a useful framework for designing your agent. You want to give it tools that are shaped to its own abilities. But how do you know what those abilities are? You pay attention, read its outputs, experiment. You learn to see like an agent.

Here are some lessons we’ve learned from paying attention to Claude while building Claude Code.

Improving Elicitation & the AskUserQuestion tool

When building the AskUserQuestion tool, our goal was to improve Claude’s ability to ask questions (often called elicitation).

While Claude could just ask questions in plain text, we found answering those questions felt like they took an unnecessary amount of time. How could we lower this friction and increase the bandwidth of communication between the user and Claude?

Attempt#1- Editing the ExitPlanTool

The first thing we tried was adding a parameter to the ExitPlanTool to have an array of questions alongside the plan. This was the easiest thing to implement, but it confused Claude because we were simultaneously asking for a plan and a set of questions about the plan. What if the user’s answers conflicted with what the plan said? Would Claude need to call the ExitPlanTool twice? We needed another approach.

(you can read more about why we made an ExitPlanTool in our post on prompt caching)

Attempt#2- Changing Output Format

Next we tried modifying Claude’s output instructions to serve a slightly modified markdown format that it could use to ask questions. For example, we could ask it to output a list of bullet point questions with alternatives in brackets. We could then parse and format that question as UI for the user.

While this was the most general change we could make and Claude even seemed to be okay at outputting this, it was not guaranteed. Claude would append extra sentences, omit options, or use a different format altogether.

Attempt#3- The AskUserQuestion Tool

Finally, we landed on creating a tool that Claude could call at any point, but it was particularly prompted to do so during plan mode. When the tool triggered we would show a modal to display the questions and block the agent's loop until the user answered.

This tool allowed us to prompt Claude for a structured output and it helped us ensure that Claude gave the user multiple options. It also gave users ways to compose this functionality, for example calling it in the Agent SDK or using referring to it in skills.

Most importantly, Claude seemed to like calling this tool and we found its outputs worked well. Even the best designed tool doesn’t work if Claude doesn’t understand how to call it.

Is this the final form of elicitation in Claude Code? We’re not sure. As you’ll see in the next example, what works for one model may not be the best for another.

Updating with Capabilities - Tasks & Todos

When we first launched Claude Code, we realized that the model needed a Todo list to keep it on track. Todos could be written at the start and checked off as the model did work. To do this we gave Claude the TodoWrite tool, which would write or update Todos and display them to the user.

But even then we often saw Claude forgetting what it had to do. To adapt, we inserted system reminders every 5 turns that reminded Claude of its goal.

But as models improved, they not only did not need to be reminded of the Todo List but could find it limiting. Being sent reminders of the todo list made Claude think that it had to stick to the list instead of modifying it. We also saw Opus 4.5 also get much better at using subagents, but how could subagents coordinate on a shared Todo List?

Seeing this, we replaced TodoWrite with the Task Tool (read more on Tasks here). Whereas Todos were about keeping the model on track, Tasks were more about helping agents communicate with each other. Tasks could include dependencies, share updates across subagents and the model could alter and delete them.

As model capabilities increase, the tools that your models once needed might now be constraining them. It’s important to constantly revisit previous assumptions on what tools are needed. This is also why it's useful to stick to a small set of models to support that have a fairly similar capabilities profile.

Designing a Search Interface

A particularly important set of tools for Claude are the search tools that can be used to build its own context.

When Claude Code first came out, we used a RAG vector database to find context for Claude. While RAG was powerful and fast it required indexing and setup and could be fragile across a host of different environments. More importantly, Claude was given this context instead of finding the context itself.

But if Claude could search on the web, why not search your codebase? By giving Claude a Grep tool, we could let it search for files and build context itself.

This is a pattern we’ve seen as Claude gets smarter, it becomes increasingly good at building its context if it’s given the right tools.

When we introduced Agent Skills we formalized the idea of progressive disclosure, which allows agents to incrementally discover relevant context through exploration.

Claude could read skill files and those files could then reference other files that the model could read recursively. In fact, a common use of skills is to add more search capabilities to Claude like giving it instructions on how to use an API or query a database.

Over the course of a year Claude went from not really being able to build its own context, to being able to do nested search across several layers of files to find the exact context it needed.

Progressive disclosure is now a common technique we use to add new functionality without adding a tool.

Progressive Disclosure - The Claude Code Guide Agent

Claude Code currently has ~20 tools, and we are constantly asking ourselves if we need all of them. The bar to add a new tool is high, because this gives the model one more option to think about.

For example, we noticed that Claude did not know enough about how to use Claude Code. If you asked it how to add a MCP or what a slash command did, it would not be able to reply.

We could have put all of this information in the system prompt, but given that users rarely asked about this, it would have added context rot and interfered with Claude Code’s main job: writing code.

Instead, we tried a form of progressive disclosure. We gave Claude a link to its docs which it could then load to search for more information. This worked but we found that Claude would load a lot of results into context to find the right answer when really all you needed was the answer.

So we built the Claude Code Guide subagent which Claude is prompted to call when you ask about itself, the subagent has extensive instructions on how to search docs well and what to return.

While this isn’t perfect, Claude can still get confused when you ask it about how to set itself up, it is much better than it used to be! We were able to add things to Claude's action space without adding a tool.

An Art, not a Science

If you were hoping for a set of rigid rules on how to build your tools, unfortunately that is not this guide. Designing the tools for your models is as much an art as it is a science. It depends heavily on the model you're using, the goal of the agent and the environment it’s operating in.

Experiment often, read your outputs, try new things. See like an agent.
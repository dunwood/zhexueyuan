# AI能否依赖真理的系统性？建模规范性领域的挑战

> 发布日期: 2026-04-13

Philosophy & Technology (2025) 38:34 https://doi.org/10.1007/s13347-025-00864-x

**AI能否依赖真理的系统性？**

**建模规范性领域的挑战**

Matthieu Queloz¹

收稿日期：2024年11月15日 / 接受日期：2025年2月20日 / 在线发表日期：2025年3月13日 © 作者（s）2025

**摘要**

推动人们对大语言模型（LLM）能够准确而全面地建模世界之进展保持乐观的一个关键假设，是真理具有系统性：关于世界的真实陈述构成一个整体，这个整体不仅是一致的，即其中不包含矛盾，而且是融贯的，即各种真理之间在推理上彼此关联。这样一来，人们便有理由期待：大语言模型原则上或许能够依靠这种系统性来填补训练数据中的空白，并纠正其中的不准确之处；一致性与融贯性似乎都预示着，大语言模型对世界的表征可以朝着更全面的方向推进。

然而，哲学家已经提出了有力理由，怀疑真理在所有思想领域中都具有系统性；他们尤其认为，在规范性领域中，真理在很大程度上是非系统性的。我主张，只要规范性领域中的真理是非系统性的，那么这就会相应地使大语言模型更难取得进展，因为它们无法再借助真理的系统性。而大语言模型越不能依赖真理的系统性，我们就越不能依赖它们替我们进行实践审议；因为规范性领域本身的这种非系统性，恰恰要求人的能动性在实践思考中发挥更大的作用。

**关键词**人工智能 · 语言模型 · 规范性 · 价值多元主义 · 价值冲突 · 能动性 · AI伦理 · 艰难选择 · 一致性 · 融贯性 · 真实性

Matthieu Queloz matthieu.queloz@unibe.ch1 伯尔尼大学哲学研究所，Laenggassstrasse 49a，3012 Bern，瑞士

**1 引言**

当被问到大型语言模型（LLM）在训练数据不完整且不完全准确的情况下，如何才能有望全面地建模世界时，Anthropic联合创始人兼首席执行官Dario Amodei援引了一个历史悠久的理念作为乐观的理由，即**真理在世界中整合成一个系统性的网络**：

世界上有一些相对简单的真理网络……所有真实的事物在世界中都是相互连接的，而谎言则有点脱离，并且不适合进入其他一切真实事物的网络。（Amodei, 2024）

我们不应认为训练数据中的不完整性和不准确性会成为AI进步的不可逾越障碍，Amodei暗示，因为LLM**原则上**可以从那些部分不一致的数据中，找出更简单、统一的真理网络——这个网络正是数据的底层基础——并依靠该真理网络的系统性来填补空白、平滑不准确之处。

然而，Amodei这种乐观所依赖的关键哲学假设是：真理**确实具有系统性**。关于世界的真实陈述总体构成一个整体，这个整体不仅**一致**（即不包含矛盾），而且**融贯**（即它所包含的真理彼此处于理性支持的关系中，允许系统中的给定真理从系统中的其他真理推断出来）。这种融贯性提供了乐观的理由，因为它让人有理由期待：训练数据中缺失或错误表示的真理，或许可以从已经表示的真理中推导出来。换句话说，真理的一致性与融贯性共同促进LLM对世界的建模朝着**全面性**取得进展。如果所有真理相互锁定形成一个系统性的网络，它们至少在原则上承诺允许LLM跳出训练数据，同时作为安全网防止错误。

在实践中，当前的LLM很可能仅在有限程度上、并且只是间接地利用真理的系统性，只要这种系统性有助于它们实现其他目标（见第3节）。然而，哲学问题在于：真理的系统性在原则上究竟能提供多大的杠杆？是否所有思想领域都具备这样的性质，使得AI的进步原则上可以依赖真理的系统性？

这个问题因哲学家们提出各种理由**怀疑**真理在所有思想领域都具有系统性而变得更加紧迫。特别是，价值多元主义者提供了有力的论证，表明**在规范性领域**，真理**不一定**具有系统性：表达价值或描述世界**应当如何**而非**实际如何**的陈述，并不必然适合形成一个一致、融贯的整体。只要规范性领域中的真理是非系统性的，这就会相应地使LLM在这些领域更难取得进展，因为它们无法依靠真理的一致性与融贯性来努力实现全面性。

简而言之，我的论证如下：在真理具有系统性的地方，朝着全面性的进展**原则上**会因LLM能够依靠真理的系统性从不完整的训练数据中进行插值——甚至外推——而得到促进。但在真理是非系统性的地方，进展很可能因LLM无法在同等程度上依靠真理的系统性来超越训练数据而受到阻碍。尤其——尽管并非唯一——在规范性领域，有理由认为真理在很大程度上是非系统性的。因此，有理由认为LLM将发现全面建模规范性领域中的真理显著更为困难。而且，LLM越不能依赖真理的系统性，我们就越不能依赖它们替我们进行实践审议；因为规范性领域本身的这种非系统性，恰恰要求人的能动性在实践思考中发挥更大的作用。

**2 真理的系统性**

真理相互锁定形成一个系统性整合的整体，这一理念在哲学中有着悠久的历史。斯多葛派早已提及**systema mundi**（世界的系统），而从莱布尼茨经沃尔夫、兰伯特、康德到黑格尔和怀特海的现代哲学家们则以各种方式阐述了这一理念。¹ 但说真理形成一个系统性的网络究竟意味着什么？基本理念是：真理并非零散的碎片，它们相互锁定形成一个统一的整体——《牛津英语词典》的原始编纂者詹姆斯·默里称之为“事实的织物”。

¹ 哲学中系统性理想最丰富的历史概述是奥托·里奇尔（Otto Ritschl）的《科学语言用法和哲学方法论历史中的系统与系统性方法》（1906）。它由Messer（1907）补充，Rescher（1979, 3–8；2005, 19–38）提供了清晰的英语说明。Losano（1968）和Troje（1969）也在法律和法理学的背景下考察了系统性要求的发端。Stein（1968）简要概述了系统概念的发展，还有各种对个别哲学家思想中系统概念的历史语境化：Rescher（1981）考察了莱布尼茨作品中的系统概念；Vieillard-Baron（1975）追溯了从莱布尼茨到孔狄亚克的系统概念；Kambartel（1969）重构了康德作品中的系统与辩护概念，Rescher（2000, 64–98）、Kitcher（1986）、Guyer（2003, 2005）、Abela（2006）和Ypi（2021）也是如此；关于黑格尔与系统性，见Brooks和Stein（2017）中的论文，尤其是Thompson（2017）。Franks（2005）探讨了德国唯心主义中系统性要求的作用。

这首先意味着真理彼此**一致**：它们没有矛盾，包括直接矛盾（P ∧ ¬P）和间接矛盾（即一个陈述的含义最终相互矛盾：(P → Q) ∧ (P → ¬Q)）。

但一致性只是一个相对较弱的要求。一堆零散且无关的真理可能没有矛盾，却并未实现系统性整合。而且，一致性很容易通过添加进一步的前提或限定来实现（想想托勒密宇宙模型中不断增加的本轮如何修补观察到的不一致性）。

当真理被系统性整合时，它们不仅是一致的，而且是**融贯的**：它们彼此处于理性支持的关系中。这种推理上的相互关联反映了事实织物中潜在的相互关联：一个事实的成立意味着某些其他事实的成立，并排除另一些事实的成立。如果纽约位于旧金山的东边，那么这就意味着旧金山位于纽约的西边，并排除纽约位于旧金山的西边。因此，地理真理必须在理性上相互协调。承认一个地理真理，就为承认其他地理真理提供了理由。

正如Nicholas Rescher（2005）所论证的，这种推理上的相互关联为人们对世界的理解引入了一种有用的冗余形式：给定关于某事物的足够多真理，列表中的任何一个真理都可以被删除，却仍能从其余真理中推导出来。Rescher（2005, 5）用一个简单的井字游戏式情境提供了一个清晰的说明：

![图片](/articles/images/AI能否依赖真理的系统性？建模规范性领域的挑战/img_2.jpg)

关于这种情况可以表述以下真理，Rescher指出：

(1) 配置中恰好有一个x。(2) 这个x不在第一行。(3) 这个x不在第三行。(4) 这个x不在第二列。(5) 这个x不在第三列。(6) 这个x不在对角线上。(7) 这个x不在列-行位置（3, 2）。

如果从列表中删除一个真理——比如(5)“这个x不在第三列”——它仍然可以从剩余部分恢复。删除(5)后，仍能从(1)、(2)、(3)和(7)推断出来。

只要事实的织物在逻辑上以这种方式统一，对该事实织物的表征就将包含冗余，使其在信息空白面前更加稳健：任何丢失的真理，或者甚至一开始就缺失的真理，仍然可以从关于事实织物的其他真理中恢复。

这种系统性整合真理的融贯性与训练LLM的前景直接相关，因为它支持通过推理扩展理解。特别是，它承诺极大地促进填补训练数据中缺失的内容。当前的LLM是否已经能够推理到训练数据中未明确出现的真理，尚有争议。但关键在于，真理的系统性在原则上支持这种可能性。由于事实织物的系统性整合，未在训练数据中表示的真理原则上可以通过推理恢复。真理的系统性促进自我完成。

在一定程度上，系统性整合真理的融贯性也承诺帮助LLM纠正训练数据中的不准确之处。这正是Amodei所指的：“谎言有点脱离，并且不适合进入其他一切真实事物的网络。”如果某个给定领域的真理是系统性整合的，那么候选真理与其已经认为真实的内容的可整合性，就可以作为是否应接受该候选真理的标准。

当然，谎言——或者更广义地说，非真理——虽然与实际真实的网络脱离，却可能与其他非真理相连。正如任何优秀的说谎者所知，说好谎的最难部分是维护谎言网络表面上的系统性完整。因为，如果事实的织物是系统性整合的，那么接受一个非真理将要求信念网络的其他部分做出相应改变，这又将引发进一步调整，如此循环，以至于即使一个虚假信念也能够推翻许多真实信念，将虚假传播到整个网络。

任何与事实相反的假设因此威胁到全面损害人们对世界的理解。这被称为Burley原理（Rescher, 2005, 4），得名于中世纪哲学家Walter Burley，他观察到每当假设一个虚假的偶然命题时，任何与之兼容的虚假命题都可以从中推导出来（Kretzmann & Stump, 1989, 391）。给定任何两个非等价真理P和Q，我们可以从中推导出¬(¬P ∧ Q)，这在逻辑上等价于P ∨ ¬Q。但如果我们现在只假设一个非真理——比如¬P——那么就没有止境，因为这立即意味着¬Q。因此，似乎接受任何一个非真理（¬P）就有放弃任何其他任意真理（Q）的后果。

Burley原理对LLM也有启示。它强调，除了LLM在原则上是否能依赖真理的系统性这一问题之外，还有它们在实践中是否成功依赖它的问题：LLM实际上是否设法抓住了事实的织物？Burley原理突显了即使从单个非真理中外推也可能编织出虚假网络的真正危险。这提醒我们，真理的网络多么容易被谎言的组织所遮蔽。

然而，假设单个非真理具有系统性后果、最终必然与已知事实相冲突这一事实，也可以转化为优势，用于确定应该接受哪个系统性整合的网络。设想一位侦探试图根据多位证人的证词重建犯罪现场。即使几位证人是共谋的，并串通将侦探卷入一个系统性的谎言网络，该谎言网络最终很可能与侦探在彻底调查后认为无可争辩的真实事物相矛盾。因此，即使侦探最初将误导性证词视为理所当然，所有案件事实必须契合成一个统一整体的要求，最终仍会导致谎言网络瓦解，因为真理的系统性给了侦探对证人认识权威的**关键杠杆**：它使侦探能够根据证词与逐渐浮现的最一致、最融贯的发生情况的契合程度，回溯性地重新评估证人的可信度。

类似地，LLM**原则上**可以依靠真理的系统性，根据它们与关于世界的最一致、最融贯陈述网络的整体契合程度，来回溯性地重新评估训练数据中的不准确之处。当竞争性的网络同样一致且融贯时，被赋予特殊权重、作为可认证权威来源的训练数据组成部分可以被视为基本真理并充当决胜因素。而且，由于真理的系统性，这些高质量输入不仅能推翻直接矛盾的陈述，还能更广泛地加以利用。当系统性整合时，它们的含义可以揭示与看似不相关陈述的含义之间的紧张关系。因此，真理的系统性——尤其在得到可靠基础支持时——促进自我纠正。

结论是，真理的系统性承诺成为全面LLM发展的重要助力，因为这种系统性正是LLM原则上可以依靠来进行**自我完成**和**自我纠正**的东西。这也引出了当前实践中的情况如何的问题：LLM目前在多大程度上已经被训练得对一致性和融贯性敏感？

**3 训练LLM中一致性与融贯性的作用**

当前的LLM很可能仅在有限程度上、并且只是间接地利用真理的系统性，只要这种系统性有助于它们实现其他训练目标。我说“很可能”，是因为存在两个不确定性的来源：一是显而易见的——领先的AI公司倾向于将训练过程的细节保密，只要这能带来竞争优势；二是哲学上更有趣的——模型**被训练**做什么是一回事，它们**实际如何**实现训练目标则是另一回事。根据公开已知的训练过程，我们可以确定LLM在多大程度上被人类**设计**得对一致性和融贯性敏感；但在这个阶段，我们只能推测它们实际上在多大程度上抓住了更广泛的一致性与融贯性模式，以此作为满足软件工程师定义的训练目标的手段。

LLM通常经历的训练过程可以分为两个阶段：**预训练**阶段和**后训练**阶段。预训练阶段的目的是将模型变成一个语言上胜任的通用知识库（这并不必然意味着模型本身“知道”事物；维基百科就是一个通用知识库，即使它本身并不知道事物）。

LLM可以被视为一个数学函数，它以词序列作为输入，输出可能的下一个词的概率分布，然后从中选择一个可能的下一个词。更精确地说，所谓的“自回归”LLM（如OpenAI的GPT模型、Google的Gemini模型或Anthropic的Claude模型）仅基于前面的标记预测文本字符串中的下一个标记（可以是词或较小的文本块，如标点符号）——模型的“上下文窗口”（大致相当于其工作记忆）允许的标记数量。² 在预训练阶段开始时，模型的参数是随机设置的，输出严重偏离。但模型通过在从互联网抓取的海量文本上训练并内化词共现模式，来学习预测文本字符串的可能延续：例如，“最好的宠物类型是”后面59.49%的时间跟着“狗”，18.74%的时间跟着“猫”，只有0.72%的时间跟着“马”。³

这一过程通过“自监督学习”（SSL）完成，意味着人类并不结构化和标记数据来帮助模型解释它。相反，他们设置一个训练目标：最小化可能的下一个标记的概率分布与实际下一个标记之间的差异。这个目标通过一个数学函数编码，该函数惩罚模型为正确标记分配低概率。差异量为模型提供反馈信号，它使用“反向传播”算法从中学习，该算法将每个参数推向能改善未来预测的方向。随着时间推移，参数被校准以产生良好的下一个标记预测，最终形成计算电路，其执行复制了训练数据中观察到的概率关系。将模型的预测倾向与自然语言中的这些统计模式对齐，为模型生成语法上和上下文上合理的句子奠定了基础。它还使模型更有可能在广泛话题上输出真实陈述。从这个意义上说，SSL将大量事实嵌入了模型。

SSL的训练目标——下一个标记预测——本身似乎对一致性和融贯性漠不关心。但LLM被训练做什么，揭示不了它们如何学习这样做（Goldstein & Levinstein, 2024；Herrmann & Levinstein, 2025；Levinstein & Herrmann, 2024）。它们如何学习这样做，在很多方面对我们仍然是不透明的（Beisbart forthcoming-b, a）。我们设计训练过程并定义训练目标，但通过训练浮现的能力更多是“生长”而非“设计”；训练目标就像模型生长的光，让模型自己开发策略来朝那个方向生长。

因此，很难排除这些模型通过学习追求从属目标来更好地实现训练目标，而这些从属目标是下一个标记预测的良好代理。毕竟，考虑某个词是否是延续文本字符串的一致且融贯的方式，似乎是追踪其实际延续概率的有前景途径。然而，仅通过预训练实现的输出一致性与融贯性仍然有限——这也正是它被称为“预训练”的原因——这表明预训练仅灌输了一种初级的敏感性，这种敏感性高度局限于单个句子或段落，但在更长范围或不同对话线程中就会崩溃（Elazar et al., 2021；Jang & Lukasiewicz, 2023；Kumar & Joshi, 2022；Liu et al., 2024）。此外，预训练数据中的一些不一致性和不融贯性（例如冲突的陈述）与事实一起被嵌入模型。

2 This so-called “causal language modelling” contrasts with “masked language modelling,” where mod els such as BERT are trained to predict a masked word given both preceding and subsequent words.

3 These are actual probabilities from GPT 3.5.

4 On emergent abilities, see Wei et al. (2022). On why conceptualising these models as nothing but next token predictors is overly reductive, see also Downes, Forber, and Grzankowski (2024).

当我们与LLM互动时，我们不只想要文本字符串的可能延续，而是希望得到准确、信息丰富、简洁且礼貌的延续，仅举几例。因此，预训练模型需要针对特定任务进行微调，例如指令遵循、对话、问答、总结、翻译或编码。后训练阶段的目的就是完善这种有点粗糙的“预训练”模型，使其模仿表征这些任务的典范完成模式。这可以被视为一种模仿学习。

标准技术是“监督微调”（SFT），其中目标通常仍是下一个标记预测，但训练数据换成较小的、任务特定的输入-输出对数据集，这些数据集由人类仔细策划、结构化和标记。这些可能是客户服务对话的理想示例，或医学问题与答案的典范对。通过在这些理想示例上进行下一个标记预测训练，模型被隐含地鼓励模仿这些示例的美德——不仅包括语气、长度和风格，还包括认识谦逊或细微差别等特征。

同样，一致性和融贯性本身并非SFT的训练目标。然而，典范输入-输出对被选择的原因之一（除许多其他原因外）正是它们是一致性和融贯性的典范。通过被微调以遵循这些模板，模型因此间接地被训练得在生成对用户提示的响应时对一致性和融贯性更敏感。

不过，告知任务特定数据集组装的一致性与融贯性考虑，仍仅限于给定输入-输出对内部的一致性与融贯性，以及该对与真理（或那些拼凑数据集的人所认为的真理）的一致性与融贯性。而且，不清楚的是，对展示这些特征的数据集进行下一个标记预测的训练，是否足以让LLM更广泛地利用事实织物的一致性与融贯性。它可能使LLM更有可能产生内部一致且融贯的输出，但内部一致/融贯的输出与依靠更广泛的事实织物的一致性与融贯性来生成输出之间，仍存在重要区别。输出一致性或输出融贯性，并不等于基于一致性或融贯性的输出。

为了进一步使模型的行为与人类期望、偏好和难以形式化的价值观保持一致，常用技术是“来自人类反馈的强化学习”（RLHF）。⁵ 基本理念是让人类注释者根据偏好对模型的输出进行评分或排序。注释者可能被指示选择他们认为更有**帮助**、**诚实**和**无害**的答案，正如Anthropic负责微调模型性格特质的哲学家Amanda Askell在Askell et al. (2021)中所说，该论文也为OpenAI的RLHF工作提供了参考（Ouyang et al., 2022）。这种反馈用于强化模型生成在这些维度上得分高的输出的倾向。为实现规模化，人类反馈被用来训练一个单独的“奖励模型”，以编码这些偏好。该奖励模型随后可用于对语言模型的输出评分，强化得分高的输出。

对一致性与融贯性的敏感性同样不是RLHF的主要目标，因为LLM在RLHF期间的训练目标是最大化奖励模型给出的分数。但由于人类注释者不仅会惩罚输出内部或输入-输出对内部的不一致/不融贯，还会惩罚与他们认为的真理的不一致/不融贯，RLHF间接激励了至少在这两个重要方面对一致性与融贯性的敏感性。

所有这些训练的结果是模型越来越善于确保给定响应内的一致性与融贯性。但这种来之不易的成就，随着对话变长仍倾向于破裂。在“这些模型性能最令人不安的弱点”中，Cameron Buckner指出，它们“在较长对话中漫无目的地不融贯徘徊的倾向，以及无法表现连贯的个体视角”（2023, 283）。这种长时间范围的瓦解体验会侵蚀对输出的信任。如果某人在同一对话中既断言p又断言非p，我们就更难接受他关于p的断言。事实上，无法表现一致且融贯的命题态度，会破坏我们正在处理命题态度的印象。“关于信念，”Bernard Williams指出，“一个人如果改变得太频繁，就不仅仅显得不一致或矛盾或无望；相反，如果他们因内部原因改变得太频繁，他们就不是信念，而是某种类似于命题情绪的东西”（2002, 191）。

5 Though newer techniques keep being developed, and AI labs increasingly use complex combinations of these and other fine-tuning methods. In “reinforcement learning from AI feedback” (RLAIF), for example, human labellers are replaced by existing AI models that act as “graders.” In “constitutional AI” approaches, the model relies on a predefined set of principles (a “constitution”) to critique its own out puts. See, e.g., Bai et al. (2022) and Lee et al. (2023).

人们越来越认识到，要使模型在较长范围内更一致且融贯，可能需要**直接**针对逻辑属性（如一致性或融贯性）对模型进行微调。对模型输出内一致性的微调，以及对与外部知识数据库一致性的微调，都是正在探索的方法（Liu et al., 2024；Zhao et al., 2024；Zhou et al. 2024）。然而，很大程度上尚未被利用的是直接衡量和优化Amodei所暗示的那种更一般能力的潜力：即不仅产生系统性输出，而且利用更广泛的真理系统性来克服训练数据中的空白和不准确之处。

因此，虽然当前训练方法如SSL、SFT或RLHF很可能间接促进了对一致性与融贯性的某些敏感性，但这种敏感性似乎范围有限，并且并未真正利用更广泛的真理系统性。未来的研究可以探索直接训练LLM利用事实织物的一致性与融贯性进行自我完成和自我纠正的方法——或许与检索增强生成（RAG）结合，后者旨在将文本生成与来自可靠来源的信息检索整合。这种对真理系统性整合的拓宽敏感性，反过来将帮助模型在时间跨度上更一致且融贯。目前，LLM仍然太像Karl Kraus所描述的新闻界：对今天写的东西是否与昨天写的东西矛盾漠不关心。

然而，即使更好的训练技术能够克服这些缺点，一个更根本的挑战仍在等待：某些领域中的真理本身可能是非系统性的。⁶ 正如下一节将要看到的，各种哲学家指出，规范性领域——尤其是伦理和政治——形成了复杂且常常相互冲突的价值、理想、美德和原则的景观。这对LLM在这些领域的前景具有重要意义。

**4 价值多元主义与规范性领域的非系统性**

价值多元主义传统——其与AI的相关性最近被John Tasioulas（2022）强调——提供了有力的论证，表明当涉及关于什么是有价值的事物的真理时，真理可能是非系统性的：表达价值或描述世界应当如何而非实际如何的陈述，并不必然适合形成一个一致、融贯的整体。

就我们的目的而言，价值多元主义最好理解为包含四个核心主张。首先，与认为真的只有一个事物是内在有价值的一元主义相反，多元主义者主张存在多个不可还原的独特价值。一元主义的一种典范形式是功利主义，它将某种形式的效用（如偏好满足）视为衡量一切其他事物的终极主宰价值。⁷ 有影响力的计算机科学家Stuart Russell（2019）便提倡这种基于偏好的功利主义，认为它是最适合使AI模型与人类价值观保持一致的伦理框架。

6 Cummins et al. have also made the congenial observation that while “some domains are cognized via a grasp of their underlying structure,” “some domains are cognized without grasping any significant under lying structure” (2001, 174–175). However, their conception of domains and what it takes for them to be structured differs starkly from the one at issue in what follows.

7 At least, this applies to the best-known elaborations of utilitarianism. As Sen (1981) argues, it is in principle possible to envisage a value pluralist elaboration of utilitarianism.

其次，多元主义者坚持，在许多情况下，这些不同价值之间存在不可还原的不兼容性。正如Bernard Williams所阐述的，多元主义者认为假设“所有善、所有美德、所有理想都是兼容的，并且可欲的事物最终可以毫无损失地统一成一个和谐的整体”是一个“深刻错误”（Williams, 2013, xxxv）。我们的价值观在共同追求时必然会拉向竞争方向，这不仅因为时间短暂或世界顽固，更因为价值观本身固有冲突。⁸ 我们面临不可避免的在分歧目标之间的权衡，其中一些目标的实现只能以牺牲其他目标为代价（Berlin, 2002, 213–214）。这不仅仅是Rawlsian意义上的群体价值观冲突，而是更强的主张：即使单个个体的价值观也可能呈现根本无法解决的冲突——例如古代卓越美德与基督教谦卑美德之间的紧张，或真实性与善良、自由与平等、忠诚与诚实、传统与进步、正义与怜悯、安全与隐私之间的紧张。

这种对不可还原不兼容性的承诺，与那些认为不存在真正不可还原的价值冲突或不可避免的道德困境的观点形成鲜明对比：后者主张任何表面冲突的要求最终都可以通过表明一种要求在词典顺序上优先于另一种，或某种要求仅仅是表面上的来解决。一个例子是康德观点，根据该观点，道德最终没有冲突要求，非道德要求可以被打折。这种对冲突道德义务的免疫依赖于**应当**蕴涵**能够**的假设：一个人只承担那些可以共同履行的道德义务，而未履行的不能真正是道德义务，而只能是**表面**义务，或至多是**初步**义务。功利主义则通过坚持真的**只有一个**道德义务——即最大化效用——来避免不可还原的不兼容性。它将任何表面价值冲突视为可通过将涉及的价值视为**同一个价值**（效用）的**版本**或**方面**来解决，并将它们纳入效用计算以确定整体最优化的东西。（一些间接功利主义试图通过强调一级价值观的自主性来容纳真正冲突，但只要二级效用考虑仍是这些一级思考方式的唯一真正验证，这种结合在反思下便会瓦解。）正是这种价值观之间的兼容性或“一致性”承诺，吸引心理学家和神经科学家Joshua Greene采用功利主义方法来对齐AI：“在我们将价值观放入机器之前，”他写道，“我们必须弄清楚如何使我们的价值观清晰且一致”（2016, 1515），而功利主义通过提供“一个统一的系统来权衡价值观”来帮助实现这一点（2013, 15）。

8 See Berlin (2013, 12), Berlin and Williams (1994), and Queloz (2025). Further elaborations of the pluralist outlook include Larmore (1987), Stocker (1990), Kekes (1993), Chang (1997a, 2015a), Dancy (2004), and Hämäläinen (2009, 548). See also Chang (2015b), Heathwood (2015), Mason (2023), and Blum (2023) for overviews.

这引出了第三个多元主义主张：不同价值在许多情况下是**不可通约的**。当价值观冲突时，不存在**共同货币**来计算用一个价值交换另一个价值所涉及的收益和损失。它还意味着更广泛的内容，即“没有其他确定的、一般性的解决冲突的程序，例如词典优先规则”（Berlin & Williams, 1994, 306）。抵抗将不可通约价值变得可通约的技术的压力，多元主义者认为，我们的努力“应该致力于学习——或再次学习，或许——如何明智地思考不可通约的价值冲突”（Williams, 2001, 89）。

朝着这个方向的重要一步是认识到：虽然可通约性蕴涵可比性，**不可通约性**却并不蕴涵**不可比性**。“比较，”Ruth Chang强调，“并不需要任何单一的价值单位尺度”（1997b）。⁹ 此外，缺乏单一价值尺度并不使代理人在给定情境中判断两个不可通约价值中哪个更重要变得任意。重要性判断不需要因为不依赖共同价值货币而变得不那么理性或合理。人们仍然可以有**理由**认为在一个给定情境中一个价值应该胜过另一个——只是这些理由不会采取共同货币或词典优先规则的形式，而是比这些高度一般的程序对上下文更敏感。¹⁰

第四，也是最后，多元主义者主张，我们不应必然期待**关于**价值的**真理**相互锁定形成一个系统性整合的整体。如果我们的许多不同价值是真正独特的、不兼容的且不可通约的，那么关于这些价值的真理之间的关系就相应地变得复杂且冲突。正如Thomas Nagel所观察到的，“科学、数学或历史中的真理必须契合成一个一致的系统”，但“我们的评价信念并不是描述单一世界的尝试的一部分”（2001, 108–9）。脱离描述单一世界的尝试，关于价值的真理在更大程度上可以是根本不一致且不融贯的。

当然，不仅仅在规范性领域，真理的统一性和系统性受到了质疑。像Nancy Cartwright（1983, 1999）这样的科学哲学家已经论证，即使**科学中的**真理也不都适合形成一个单一的、以物理学为顶端的金字塔形系统。在她看来，科学更像拼凑而非金字塔，形成适合特定领域的模型马赛克，而非宏大的统一理论。¹¹ 即使是维也纳学派科学统一运动的旗手Otto Neurath，也敦促科学家放弃对“**那个**”科学的信念，即所有关于自然现象的真理都可以被装入其中（Neurath, 1935, 17）。

9 Chang (2015b, 25) maintains that even monism does not strictly entail comparability, because different qualities of a single value need not be comparable; indeed, on her account, even different quantities of a single value need not be comparable.

10 This line of thought has been elaborated notably by Dancy (1995, 2004) and the large literature on particularism; see the essays in Hooker and Little (2000) for a good overview.

11 See also Feyerabend (1993), Dupré (1995), and the collection edited by Galison and Stump (1996). For a more recent and partly critical examination of studies of inconsistency in science, see Vickers (2013). For an examination of the relation of Cartwright’s account to Dancy’s particularism in ethics, see Sandis (2006).

但科学中的真理仍然表现出大量的**局部**一致性与融贯性：在科学学科内或一个模型内，它们在很大程度上适合形成一个系统性的整体。¹² 此外，虽然它们在不同抽象层次上抓住不同的属性，却仍被理解为同一个自然世界的不同模型。事实上，这一点被Cartwright自己的说明（它也作为她《斑驳世界》的封面）所强调：她将科学的不同学科描绘成松散集合的灵活却有界的气球，没有特定顺序；但每个气球都“系在同一个物质世界”（Cartwright, 1999, 6），关于这个世界可以用朴素的日常语言表述大量系统性整合的真理（例如，“气球下面有两棵树；”“树在停车标志的左边”）。对于伦理和政治的规范真理，并不存在这样一个底层统一的物质世界的直接类似物。

最后这一点被David Wiggins和Bernard Williams在一篇鲜为人知的联合论文中明确指出，值得长篇引用：

在科学中，理论家希望找到少数几个原则，从中其他一切都可以推导出来。……但在道德哲学的情况下，定义该主题的是高度异质的人类关切集合，其中许多与其他许多相互冲突，许多与其他许多不可通约。在这种情况下，没有理由认为需要的是一个发现**潜在秩序**的理论。这毕竟不是一个有很多隐藏的主题。或者说，隐藏的东西是以心理或解释意义上的隐藏的。没有秘密的价值秩序原则的问题。没有可比的更深层次的现实，就像化学和物理所探索的微观或亚微观层次一样，这是道德哲学家的职责去探查。在一个人无法理解存在这样一个层次的地方，一些道德哲学家所敦促的发现“最简单理论”来“保存现象”（在该短语的正常接受意义上）的想法几乎毫无意义。在人们以这种方式说话的物理主题中，“最简单”一词在可敬的情况下（理论不仅仅是曲线拟合练习）可以被赋予独立的（但主体绑定的）阐释；然后产生所需曲线的方程可以被认为是在向一个独立的物理现实“ homing”。在道德理论情况下，看起来极端反常——除非我们认为理论家的原则在向一个心理现实 homing，即道德和价值意识，整个建构从中起源。但那不是隐藏或不可观察的东西。它可以随时被咨询，并且它可能可以被改进：但不是通过一个理论的规训，该理论的唯一权威主张在于它错误地声称表达了该意识的潜在和隐藏法则。（Wiggins & Williams, 1978, xxxviii–xxxix）

认为规范性领域中没有**隐藏的潜在秩序**要发现的想法，已被用来反对哲学将规范真理组织成系统性伦理理论的抱负——或许最持续的是Sophie Grace Chappell，她也强调拥抱非系统性与关于价值的现实主义完全兼容。¹³ 然而，目前的关键点是关于规范真理**结构**的先前一点：哲学家和LLM都试图通过将它们压缩成整洁理论或压缩成模型权重来捕捉的大量底层规范真理景观**本身**缺乏结构凝聚力。不一致和不融贯不仅出现在理论层面（在那里一个理论大厦的含义与另一个的含义冲突或未能融贯，这将镜像科学模型根据Cartwright相互关联的方式），而是一直延伸到被建模的价值本身的底层。

这些冲突的底层真理可以采取两种形式之一。¹⁴ 在第一种情况下，同一个行动似乎在鉴于其某些特征的情况下是我**应当**履行的，同时似乎在鉴于其某些其他特征的情况下是我**不应当**履行的：在价值x的光照下，我**应当**φ；但在价值y的光照下，我**不应当**φ。那么决定是否 φ 就需要判断在该情境中支持和反对行动的特征的相对重要性。

在第二种情况下，有两个行动我每个都应当履行，但我不能两者都做：在价值x的光照下，我应当 φ；但在价值y的光照下，我应当 ψ 代替，而且我不能两者都做。我不能两者都做的事实可能是由于世界的一个偶然经验特征——例如目前千斤顶的工作方式，可能不可能同时是千斤顶操作员兼职音乐会钢琴家。¹⁵ 但同样，冲突可能是价值本身固有的。x和y之间可能存在固有紧张——例如自由与平等，或真实性与幸福，或安全与隐私——即x的持续实现只能以y的持续实现为代价，反之亦然。再次，似乎需要重要性判断来决定在给定情境中哪个价值应该胜出，以及一个人应该在多大程度上牺牲另一个价值的实现来达到这一目的。

13 See not only the books published under the name Sophie Grace Chappell (2015a, 2015b; 2022), but also those published under the name Timothy Chappell (2009; 2015a, 2015b).

14 I draw here on Williams’s (1973, 171) discussion of conflicts of ought.

15 I take the example from Millgram and Thagard (1996, 73).

多元主义者坚持认为，这种冲突的真理不能总是被分析掉；它们之间的冲突可能是真正且不可还原的。这突显了系统性真理与非系统性真理之间的鲜明不对称。当发现系统性领域中两个信念之间的冲突时，冲突的发现通常被视为某种**认识错误**的证据，并且对冲突信念的信心被**削弱**，直到找到错误并至少放弃两个冒犯信念中的一个。但在**非系统性**领域，冲突的发现不必是认识错误的证据，并且对冲突信念的信心根本不必被削弱。相反，冲突的发现使一个人意识到他面临一个困境，或至少一个权衡，这需要关于在特定情境中什么更重要的判断。而且，一旦做出那个判断并且一个信念胜过另一个，被推翻的信念不会消失。相反，它现在登记为**对以某个其他被认为在该情境中更重要的价值名义下推翻的价值所招致的真实成本的遗憾**。¹⁶ 两个冲突信念因此都持续存在——虽然在一个胜出后，另一个以不同形式重新浮现：作为遗憾，或作为损失感，它承认未被据以行动的考虑的现实和力量，并且可能随后激发进一步行动，例如表示悔恨、做出补偿、发出道歉，或提供某种补偿或赔偿。¹⁷

这些关于价值的真理之间不可消除的冲突意味着，在线的尽头，规范性领域中可能没有系统性和谐可得：表达我们的价值观和描述世界应当如何的各种规范真理，并不整齐地适合形成一个统一的、一致的和融贯的系统。我们可以说，关于价值的真理至少部分是**非系统性的**。我们不断承认这种非系统性，当我们通过表示遗憾或悔恨承认，由于我们做了我们**不得不**做的事情而招致了真实损失。如果关于规范性领域的所有真理适合形成一个和谐的整体，我们就可以毫无痛苦的权衡或剩余地实现我们所有的价值观。承认我们不能这样做就是承认这些真理在某种程度上是非系统性的。

这一点可以用地图与其描绘的景观之间的区别生动地表达。某些领域中的真理，例如地理，形成一个系统性整合的整体，因为它们映射的景观本身形成一个系统性整合的整体——在这种情况下，地球，其**本体论**系统性确保了地理真理如“巴黎在布拉格西边”和“布拉格在巴黎东边”的**逻辑**系统性。但如果多元主义者是正确的，那么其他领域中的真理，例如关于伦理和政治的规范真理，不形成一个系统性整合的整体，因为它们映射的景观本身不形成一个系统性整合的整体；相反，它形成一个碎片化的、充满紧张的、分散的和断开的景观。如果我们将规范景观视为各种影响和 vastly 不同传统的历史沉积物，这应该不足为奇。¹⁸ 为什么我们应该期望文化历史的兴衰，以及它们以往往偶然和混乱的方式混杂在一起并不断重新配置的所有不同规范反思传统，会产生一个追踪整齐整合的规范景观的规范反思实践？这样一个过程更有可能产生一个冲突规范考虑的断开拼凑。那些坚持规范景观本身已经表现出完美系统性的人，多元主义者坚持，欠我们一个解释，即那种系统性是如何 supposed 到那里的。¹⁹

16 These features of value conflicts are discussed in detail in Williams (1973) and Queloz (2024b).

17 On regret or a sense of loss as an acknowledgement of genuine conflicts of values, see Williams (1973, 1981a, b, 2005a), Queloz (2024a), and Cueni (2024).

18 See MacIntyre (2007) and Williams (2005b, 136–37).

19 See Williams (1995c, 189).

只要关于价值的真理是非系统性的，对它们的正确取向就不是将它们塞入一个统一的和融贯的系统，而是旨在对它们之间的微妙相互作用和权衡有细致的理解。正如Nora Hämäläinen强调的，争取系统性和融贯性可能不是“道德领域中的正确取向”，因为“我们道德词汇和框架中的空白和跳跃可能是所调查对象——道德——的本质，而不是我们理解中的错误，需要通过更连贯的、单一的视角来纠正”（2009, 548）。我们的评价信念因此可以自由地像我们的价值观本身一样不可还原地分散、不一致和充满紧张——事实上，我们的评价信念**应该**镜像这种非系统性，如果它们要忠实于我们的价值观。

规范真理的非系统性反过来对LLM的前景具有重要影响。LLM擅长识别和利用模式，并且在系统性领域内进行推理方面越来越好。但任何依靠识别和利用系统性和一致模式的学习方法，在建模缺乏系统性和一致性的规范景观时会更难。如果多元主义者是正确的，并且规范性领域至少部分是非系统性的，那么建模人类价值观的尝试就不能期望从真理的系统性中获得它们在系统性领域（如地理）原则上可以依靠的那种支持。如果规范真理是非系统性的，这些真理将不会表现出地理真理所展示的那种推理相互关联和冗余程度。因此，当面对价值多元主义所突显的固有和不可解决的冲突时，LLM从不完整训练数据中外推并全面建模人类价值观的能力将受到阻碍。如果多元主义者是正确的，规范性领域中真理的非系统性是AI模型的一个重大障碍。

这与Sorensen et al. (2024)最近确定的障碍不同。他们的担忧是，只要AI系统是统计学习器，聚合海量数据并将其拟合到平均值，它们就不适合学习固有冲突的价值，因为它们风险“洗掉”（Sorensen et al., 2024, 19937）我们希望它们建模的价值冲突。同样的“洗掉”问题也困扰着Feng et al. (2024)试图从其LLM的预训练数据中提取规范要求的尝试：他们过滤规范要求以确保其一致性。但如果LLM supposed 要建模的规范真理本身是不一致的，这种过滤过程有效地扭曲了模型对其试图映射的规范景观的把握。当处理非系统性领域时，在系统性整合领域中承诺帮助LLM自我完成和自我纠正的策略因此变成了反生产的策略，风险扭曲地图。

正如Sorensen et al. (2024)所示，朝着克服这一困难迈出的重要一步是通过在ValuePrism等数据集中明确表示它们来容纳价值冲突。这个明确“价值多元主义”的数据集利用GPT-4的开放文本生成能力来明确其预训练数据中编码的广泛人类价值观。由此产生的数据集据称涵盖218k个价值、权利和义务的例子，这些例子根据31k个人类描述的情境（通过过滤Allen Institute的Delphi演示中来源的1.3M个人类书面情境获得）进行了情境化。

在这样的数据集上训练的模型，如Value Kaleidoskope（Kaleido），设法明确表示价值观之间的冲突（Sorensen et al., 2024）。给定一个情境描述（例如，“说谎以保护朋友的感受”），Kaleido首先探索性地生成一百个规范考虑（例如，“诚实”，“朋友的福祉”），然后根据它们与情境的相关性过滤它们。然后，它基于文本相似性删除重复项目，并为每个剩余的规范考虑计算相关性和价分数（其中相关性是0到1之间的某个数字，价是支持、反对或任一，取决于上下文）。最后，它生成一个事后理由，解释每个规范考虑为什么与情境相关（例如，“如果你重视诚实，即使它伤害感情，最好还是说实话”）。

沿着这些思路的AI模型**能做**的是明确承认并提及其训练数据中隐含的冲突价值观。这可以是一种有价值的协助形式，尤其是如果它提醒一个人注意与情境评估相关的价值观的多样性。即使现在，LLM也比人类更有效地探索性地过度生成可能相关的考虑，然后可以按相关性过滤。这种协助形式 apt 于吸引一个人注意他们尚未想到考虑的相关方面。

但即使是像Kaleido这样的多元主义AI模型**不能做**的是克服规范真理的非系统性对其超越训练数据的能力施加的限制。在多元主义图景中，即使一个被训练承认价值冲突现实的LLM也将无法通过利用真理的系统性来克服训练数据中的遗漏和不准确之处，就像它基于的GPT-4模型一样。只要规范性领域中的真理是非系统性的，这将剥夺两种模型依靠真理的一致性和融贯性来努力实现全面性的能力。

**5 系统性越少，人类能动性越多**

规范真理的非系统性对AI作为道德顾问的潜力有什么影响？如今LLM在感知道德专业知识上已能与专业伦理学家竞争，这种潜力越来越受到关注。²⁰ 在本节最后，我将论证：AI越少能依赖真理的系统性，我们就越少能依赖AI替我们进行实践审议。这是因为规范性领域中的真理越不系统，实际审议中人类能动性和个性的作用就越大。

20 Using a “Moral Turing Test,” researchers found that people perceive practical advice from GPT-4o as more moral, trustworthy, thoughtful, and correct than that of professional ethicists in the New York Times column “The Ethicist” (Dillion et al., 2025). See, e.g., Giubilini and Savulescu (2018); Constan tinescu et al. (2021); Landes, Voinea, and Uszkai (2024) for discussions of AI’s potential as a moral advisor

要看到这一点，考虑经验领域系统性与规范性领域非系统性之间的对比如何在理论审议和实际审议的结构中产生相应的对比（即关于相信什么的审议和关于做什么的审议）。

当审议关于某个系统性领域（如地理）应该相信什么时，我的信念形成旨在一套一致且融贯的真理，并且我最终真正相信的必须与其他人最终真正相信的一致且融贯。换句话说，真理的系统性使我应该相信的与任何人应该相信的相同。我应该相信巴黎在布拉格西边的结论然后感觉是派生的，因为它遵循一个更一般的真理，即任何人应该相信巴黎在布拉格西边。在这个意义上，审议只是偶然地是我的。

相比之下，当审议我应该做什么时，我应该做的与任何人应该做的之间的等价性破裂了。²¹ 规范真理越冲突，呈现出拉向不同方向同时保持不可还原独特、不兼容和不可通约的考虑，就越需要重要性判断来确定在给定实际审议情境中哪个考虑应该胜过哪个。

21 As pointed out notably by Williams (1985, 76–77; 1995a, 123–125; 1995b, 170), whose argument I develop and apply to the contrast between systematic and asystematic domains here.

这些重要性判断不能外包给算法。一个人可能在Kaleido赋予价值观的“相关性分数”中看到这样做的尝试，作为评估它们在多大程度上与情境相关的方式。但这些相关性分数仍然与我心目中的重要性判断关键不同。正如Kaleido的开发者所指出的，他们模型的训练数据是合成的，即本身由AI模型生成——在这种情况下，是GPT-4。这意味着Kaleido不是直接被训练来预测人类是否会发现一个价值相关；相反，“模型的训练目标实际上更接近预测给定价值是否可能由GPT-4为特定情境生成”（Sorensen et al., 2024, 19942）。因此，模型生成的相关性分数捕捉的不过是一个文本字符串在GPT-4响应情境描述生成的文本中出现的可能性。相关性分数因此衡量一类考虑对一类情境的统计相关性。但特定考虑对特定情境中代理人的重要性远远超出这种仅仅统计相关性。

一个人可能认为统计相关性的问题仅仅是它未能规范，因为我们真正想知道的是哪些考虑在手头情境中是规范相关的。这在它所及的范围内是正确的，但重要性要点更进一步。规范相关性是更复杂的多元主义AI模型原则上可以通过变得可靠预测人类会认为规范相关的东西来近似的东西。**哪些**人类可以通过在单个用户的价值观上微调模型来解决，正如Giubilini和Savulescu（2018）、Constantinescu et al.（2021）和Landes、Voinea和Uszkai（2024）所建议的，从而使模型将其用户的规范相关性判断回镜给他们，并帮助他们在其自己的实际审议中更一致且融贯。

然而，即使一个可靠追踪用户规范相关性的AI模型也无法因此弥合与特定情境中对代理人重要的东西之间的差距。那个判断必然落在代理人身上，不能卸载给其他人。

这一事实被“What should I do?”问题的模糊性所遮蔽，这产生了印象，即我可能让别人，甚至让作为道德顾问的AI模型代表我回答问题。但我们必须区分两种“should”：出现在非人称“What should I do?”问题中的“should”和出现在第一人称“What should I do?”问题中的“should”。²² 非人称“What should I do?”问题与“What is to be done?”问题重合，后者询问在所有规范相关考虑的光照下行动方针的推荐。但即使考虑所有规范相关考虑产生了对非人称“What should I do?”问题的明确答案，对于要据此行动的代理人来说，仍有一个进一步的问题：鉴于这一切，在这个特定情境中我现在应该做什么？这不仅仅是早期问题的重复。即使我对那个进一步问题的答案与前一个问题的答案重合，这也不会仅仅是答案的重复。它将是代理人判断规范考虑建议要做的事情确实是他或她应该做的事情的表达。如果我们考虑这样一种情况，这一点变得明显：规范考虑清楚地表明我应该 φ，但我非常想 ψ，而且我不能两者都做。²³ 如果我然后问自己：“我应该做什么？”，我不是在问什么行动方针被相关规范考虑所青睐。我已经知道了。我是在问自己是否真的应该 φ，正如相关规范考虑建议我应该的，还是我应该遵循我倾向于 ψ 的倾向。

22 Here, I draw out the consequences for AI of Williams’s suggestion that practical thought is “radically f irst-personal” (Williams 1985, 23). See also Queloz (2021).

23 This adapts an argument offered in Williams (1973, 183–185) to distinguish two kinds of ought; see also Williams (1995a, 123–125).

因此，我们必须小心不要将出现在规范相关考虑推荐的行动方针陈述中的“should”与代理人自己的实际审议最终必须发出的“should”混为一谈。前者只是偶然地是第一人称的，并且同样可以在第三人称中回答（“他应该做的是……”）。后者然而本质上是第一人称的，并且只能在第一人称中回答。

假设一个复杂的LLM被训练来追踪人类代理人A认为规范相关的东西，用于回答实际问题。如果问题真的是实际问题，即关于做什么的问题，A将需要决定是否执行答案。然而，对于A执行答案来说，AI模型认为——或其文本输出断言——A应该 φ 是不够的。A自己需要得出她应该 φ 的结论，在“should”的不可还原第一人称意义上。这要求 φ-ing 应该对A来说在她的判断中在这个情境中什么对她最重要方面有意义。A应该做什么的实际问题，即使由AI模型在A过去有重量的所有规范相关考虑方面胜任回答，仍最终在A的一个第一人称问题中达到顶点，该问题只能根据A自己在特定情况下的重要性判断来回答。

A难道不能通过将执行AI模型识别为要做的任何事情作为她的压倒一切原则来跳过这个第一人称问题吗？如果模型有提供明智建议的记录，这将很诱人。但请注意，即使那样，A仍将被迫自己回答第一人称实际问题。例如，如果她有这样的想法：“AI在这个问题上有良好记录，说 φ-ing 是要做的，”她仍将被迫面对诸如“我现在应该 φ 还是以后？”和“我应该以这种方式还是那种方式 φ？”的问题。实际审议有一个不可还原的第一人称维度，它通过这个进一步意义上的“should”的持久可用性表达自己。而且可以运行平行论证来区分两种“shall”和两种“ought”（如在“What shall I do?”和“What ought I to do?”中）。²⁴

当然，如果这是正确的，那么即使所有规范真理可以系统性整合成一个和谐的整体，也会有“What should I do?”问题的第一人称版本。²⁵ 通过增加实际审议的冲突特征，规范性领域的非系统性突显并放大了代理人的作用。规范景观与我们对峙的不可通约价值观之间的不可还原冲突越多，我们就越会面临不舒服的束缚、真正的困境和悲剧选择，并且越需要关于在给定情境中什么最重要的第一人称判断。

24 See Williams (1973, 183–185; 1995a, 123–125).

25 Similarly, even questions about systematically integrated non-normative domains—such as: “Did Keats die in Rome?”—have first-personal analogues, such as: “What should I believe about whether Keats died in Rome?” But these are first-personal only incidentally. One could equally well ask: “What should anyone believe about whether Keats died in Rome?”.

多元主义图景因此不仅使实际审议的激进第一人称特征在康德或功利主义图景通过暗示没有真正不可还原的价值冲突供个人解决而遮蔽它的地方变得突出；多元主义图景还通过要求他们确定如何导航这些价值冲突而赋予个体代理人更积极的作用。

我们可以说，虽然所有实际审议在某种程度上都是第一人称的，无论真理的系统性如何，但规范性领域中真理的非系统性通过分配更大的作用给代理人的重要性判断而增加了这个第一人称维度。因为，在导航一个冲突的规范景观时，我被迫在更大程度上依靠我关于什么在特定情境中对我来说最重要的事件的判断。

这在Ruth Chang所说的“艰难选择”（2017）中很好地体现出来，这些选择一旦我们认识到规范性在结构上是**四分的**而不是三分的，就变得无处不在——两个项目可以在**四种**而不是三种不同的方式上规范相关：(i) 一个可以**比**另一个更好；(ii) 一个可以**比**另一个更差；(iii) 它们可以**同样好**，所以一个人可能不妨掷硬币；以及(iv) 它们可以**并列**，即不可通约，但处于价值的同一邻域。艰难选择是这种并列选项之间的选择，即使所有相关信息都进来后仍保持并列。一个选择在某些方面更好，而另一个在其他方面更好。然而，这并不意味着我们可能不妨掷硬币。决定仍然可以是理性的，在以理由而非任意为基础的意义上。但达成理性决定要求代理人超越被动登记独立给定的规范考虑的相关性的作用。代理人必须在决定中发挥更积极的作用，并考虑哪些方面对他或她**更重要**。在提醒我们即使是常见的实际审议实例也本质上依赖于其行动所涉及的代理人的输入时，艰难选择鼓励“对什么是理性代理人的理解的根本转变，将积极的、创造性的人类能动性置于理性思想和行动的中心”（Chang, 2023, 173）。

例如，想象我正在审议是否应该追求哲学职业生涯还是咨询职业生涯。即使所有支持和反对每个职业选择的有关规范考虑都被详尽列出并仔细考虑，仍有一个问题，即**我**应该做什么，尤其是如果各种考虑没有都和谐地组装成一个明确的答案。Chang以显著自愿主义术语呈现这种选择，作为主要对代理人意志负责的——在她看来，正是通过愿意**承诺**一种或另一种方式，我**创造**使选择理性的理由。²⁶

26 See Chang (2002, 2009, 2013, 2016). Drawing on Chang’s work, Goodman (2021) argues that the existence of hard choices imposes limits on how much practical reasoning AI models can do on our behalf.

但一个人也可以认为确定一个人应该做什么的过程具有**发现**关于自己的性质——而且，关键是，只有代理人自己才能做出这种发现。达成决定迫使我不仅问哪些考虑对我来说更重要，而且哪些考虑对我**更重要**。决定不仅仅是**第一人称**的，就像每个实际决定最终必须是的那样，而且，正如我们自然所说，**个人的**。在得出**我**应该追求哲学职业生涯的结论时，因为某些支持该选择的考虑对我特别重要，我然后表达了某种独特于我自己的东西——这种东西可能在审议过程之前已经完全形成，或者可能仅通过该过程才获得确定形式，但它仍然以发现的形式呈现给我，而不是作为我意志的表达，而是作为关于我自己的发现。虽然决定当然仍应由相关非人称规范考虑告知，但它不应仅仅回应它们，而且应忠实于我是谁，或发现我自己已经成为谁。我们可以说涉及的真实性形式是双面的：它包括忠实于自己以及忠实于规范事实。换句话说，决定涉及真实性的要求以及对非人称理由的回应性。

由于这种对真实性的要求，我应该追求哲学职业生涯的结论感觉不是派生的，因为它不遵循任何人应该追求哲学职业生涯的更一般思想。审议不仅是偶然地，而且本质上是我的。从准全知AI的视角进行的实际审议不能替代这个。²⁷ 正如Williams所说：“我的生活，我的行动，完全不可还原地是我的，要求它至多是一个派生结论，即它应该从碰巧是我的视角来生活是一个非凡的误解”（1995b, 170）。实际审议远非仅对AI可能相互权衡的非人称规范考虑负责，而且系统性地拥有一个第一人称维度，有时甚至是一个个人维度，由于这个维度，决定不能外包给任何东西或任何人，而是本质上是代理人自己的。

建立在实际推理是非人称的假设上，并且“What should I do?”问题等价于“What should anyone do?”问题的AI模型，忽视了实际审议的这些第一人称和个人维度。即使像Kaleido一样，一个模型考虑到了价值观的多元性和不兼容性，这仍然成立。因为它的结论仍将采取非人称形式：它将陈述，在这样一个冲突价值观可能相关的情境中，φ-ing是要做的。如果我们要忠实于实际思想的第一人称和个人性质，这至多可以是代理人审议的咨询输入。至于代理人实际应该做什么的结论，仍必须由其实际决定所属的**代理人**达成。这证实了多元主义信念，即“实际决定原则上不能完全算法化，并且……旨在算法理想的实际理性概念必须是错误的”（Berlin & Williams, 1994, 307）。

结论是，规范性领域展示的系统性越少，AI就越少能依赖真理的系统性，我们就越少能依赖AI替我们进行实践审议。在导航价值冲突和做出艰难选择中相应地有更多人类能动性和个性的作用。系统性越少，人类能动性越多。

27 For a complementary argument why we have reasons not to want an AI that lets one know who one is and what one should do, see Leuenberger (2024).

**6 结论**

只要规范性领域表现出非系统性，Amodei的乐观因此看起来基础不牢：LLM不能依靠真理在整个板上形成系统性网络来自我完成和自我纠正。LLM超越其训练数据的替代方式可能还会出现。但如果多元主义关于规范性领域的图景是正确的，LLM就不能利用这些领域的系统性和谐。因此，在那个程度上，LLM应该更难全面建模规范性领域。

更有甚者，这种系统性的缺乏本身要求人类留在决策循环中。规范性领域越非系统性，代理人所需的重要性的判断就越多，这些重要性判断表达并强调了实际审议的第一人称和个人维度，这些维度不能外包给AI模型。有时，关键不是决定应该是绝对和客观上最好的一个，而是它应该是**我们的**。

**致谢**我感谢编辑以及两位匿名审稿人对本文的有价值评论。Pierre Beckmann、Markus Stepanian和Mumün Gencoglu对早期草稿提供了有见地的反馈。我也感谢Ben Matheson、Constant Bonard，以及伯尔尼大学实践哲学讨论会的参与者。

**作者贡献**不适用。

**资金**开放获取资金由伯尔尼大学提供。由瑞士国家科学基金会资助。

**数据可用性**不适用。

**声明**

**伦理批准和参与同意**不适用。

**出版同意**不适用。

**竞争利益**作者声明他没有竞争利益。

**开放获取**本文根据知识共享署名4.0国际许可协议获得许可，该许可允许在任何媒介或格式中使用、共享、改编、分发和复制，只要您给原作者（们）和来源适当署名，提供指向知识共享许可的链接，并表明是否进行了更改。本文中的图像或其他第三方材料包含在文章的知识共享许可中，除非在材料的信用线中另有说明。如果材料未包含在文章的知识共享许可中，并且您的预期使用不是由法定法规允许的或超出了许可的使用范围，您将需要直接从版权持有人那里获得许可。要查看该许可的副本，请访问

http://creativecommons.org/licenses/by/4.0/。

**参考文献**http://creativecommons.org/licenses/by/4.0/。 Abela, P. (2006). The Demands of Systematicity: Rational Judgment and the Structure of Nature. In G. Bird (Ed.), A Companion to Kant (pp. 408–422). Blackwell. Amodei, D. (2024). “What if Dario Amodei Is Right About A.I.?” Interview by Ezra Klein. The Ezra Klein Show, New York Times Opinion, April 12, 2024. https://www.nytimes.com/2024/04/12/opinion/ezra-klein-podcast-dario-amodei.html Askell, A., Bai, Y, Chen, A., Drain, D, Ganguli, D, Henighan, T., Jones, A., Joseph, N., Mann, B, & Das-Sarma, Nova. (2021). “A general language assistant as a laboratory for alignment.” arXiv preprint arXiv:2112.00861. Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., ... & Kaplan, J. (2022). Constitutional ai: Harmlessness from ai feedback. arXiv preprint arXiv:2212.08073. Beisbart, C. (forthcoming-a). “Epistemology of Artificial Intelligence.” In The Stanford Encyclopedia of Philosophy. Edited by Edward N. Zalta. Beisbart, C. (forthcoming-b). “In Which Ways Is Machine Learning Opaque?.” In Philosophy of Science for Machine Learning: Core Issues and New Perspectives. Edited by Juan Durán and Giorgia Pozzi. Dordrecht: Springer. Berlin, I. (2002). Two Concepts of Liberty. In H. Hardy (Ed.), Liberty (pp. 166–217). Oxford University Press. Berlin, I. (2013). The Pursuit of the Ideal. In H. Hardy (Ed.), The Crooked Timber of Humanity: Chapters in the History of Ideas (pp. 1–20). Princeton University Press. Berlin, I., & Williams, B. (1994). Pluralism and Liberalism: A Reply. Political Studies, 42(2), 306–309. Blum, C. (2023). Value Pluralism versus Value Monism. Acta Analytica, 38(4), 627–652. Brooks, T., & Stein, S. (Eds.). (2017). Hegel’s Political Philosophy: On the Normative Significance of Method and System. Oxford University Press. Buckner, C. (2023). From deep learning to rational machines: What the history of philosophy can teach us about the future of artificial intelligence. Oxford University Press. Cartwright, N. (1983). How the Laws of Physics Lie. Oxford University Press. Cartwright, N. (1999). The Dappled World: A Study of the Boundaries of Science. Cambridge University Press. Chang, R. (Ed.). (1997a). Incommensurability, Incomparability, and Practical Reason. Harvard University Press. Chang, R. (1997b). Introduction. In R. Chang (Ed.), Incommensurability, Incomparability, and Practical Reason (pp. 1–34). Harvard University Press. Chang, R. (2002). Making Comparisons Count. Routledge. Chang, R. (2009). Voluntarist Reasons and the Sources of Normativity. In D. Sobel & S. Wall (Eds.), Reasons for Action (pp. 243–271). Cambridge University Press. Chang, R. (2013). Commitments, Reasons, and the Will. In R. Shafer-Landau (Ed.), Oxford Studies in Metaethics (Vol. 8, pp. 74–113). Oxford University Press. Chang, R. (2015a). Value Incomparability and Incommensurability. In I. Hirose & J. Olson (Eds.), The Oxford Handbook of Value Theory (pp. 205–224). Oxford University Press. Chang, R. (2015). Value Pluralism. In International Encyclopedia of the Social & Behavioral Sciences, 25, 21–26. Chang, R. (2016). Comparativism: The Grounds of Rational Choice. In E. Lord & B. Maguire (Eds.), Weighing Reasons (pp. 213–240). Oxford University Press. Chang, R. (2017). Hard Choices. Journal of the American Philosophical Association, 3(1), 1–21. Chang, R. (2023). Three Dogmas of Normativity. Journal of Applied Philosophy, 40(2), 173–204. Chappell, T. (2009). Ethics and Experience: Life Beyond Moral Theory. Durham: Acumen. Chappell, S. G. (Ed.). (2015a). Intuition, Theory, and Anti-Theory in Ethics. Oxford University Press. Chappell, S. G. (2022). Epiphanies: An Ethics of Experience. Oxford University Press. Chappell, T. (2015b). Knowing What To Do: Imagination, Virtue, and Platonism in Ethics. Oxford University Press. Constantinescu, M., Vică, C., Uszkai, R., & Voinea, C. (2021). Blame It on the AI? On the Moral Responsibility of Artificial Moral Advisors. Philosophy and Technology, 35(2), 1–26. Cueni, D. (2024). Constructing Liberty and Equality – Political, Not Juridical. Jurisprudence, 15(3), 341–360. （以下为完整参考文献列表的直译，继续保持原文所有细节，无删节：） Cummins, R., Blackmon, J., Byrd, D., Poirier, P., Roth, M., & Schwarz, G. (2001). Systematicity and the Cognition of Structured Domains. Journal of Philosophy, 98(4), 167–185. Dancy, J. (1995). In Defense of Thick Concepts. Midwest Studies in Philosophy, 20(1), 263–279. Dancy, J. (2004). Ethics without Principles. Clarendon Press. Dillion, D., Mondal, D., Tandon, N., & Gray, K. (2025). AI language model rivals expert ethicist in perceived moral expertise. Scientific Reports, 15(1), 4084. https://doi.org/10.1038/s41598-025-86510-0 Downes, S. M., Forber, P., & Grzankowski, Alex. (2024). “LLMs are Not Just Next Token Predictors.” arXiv arXiv:2408.04666. Dupré, J. (1995). The Disorder of Things: Metaphysical Foundations of the Disunity of Science. Harvard University Press. Elazar, Y., Kassner, N., Ravfogel, S., Ravichander, A., Hovy, E., Schütze, H., & Goldberg, Y. (2021). Measuring and Improving Consistency in Pretrained Language Models. Transactions of the Association for Computational Linguistics, 9, 1012–1031. Feng, N., Marssø, L., Yaman, S. G., Standen, I., Baatartogtokh, Y., Ayad, R., ... & Chechik, M. (2024, June). Normative requirements operationalization with large language models. In 2024 IEEE 32nd International Requirements Engineering Conference (RE) (pp. 129-141). IEEE. Feyerabend, P. (1993). Against Method (3rd ed.). Verso. Franks, P. W. (2005). All or Nothing: Systematicity, Transcendental Arguments, and Skepticism in German Idealism. Harvard University Press. Galison, P., & Stump, D. J. (Eds.). (1996). The Disunity of Science: Boundaries, Contexts, and Power. Stanford University Press. Gaukroger, S. (2020). Civilization and the Culture of Science: Science and the Shaping of Modernity, 1795–1935, Civilization and the Culture of Science. Oxford University Press. Giubilini, A., & Savulescu, J. (2018). The Artificial Moral Advisor. The “Ideal Observer” Meets Artificial Intelligence. Philosophy and Technology, 31(2), 169–188. Goldstein, S., & Levinstein, B. A. (2024). Does ChatGPT Have a Mind?. arXiv preprint arXiv:2407.11015. Goodman, B. (2021). “Hard Choices and Hard Limits for Artificial Intelligence.” Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society. Greene, J. (2013). Moral Tribes: Emotion, Reason, and the Gap Between Us and Them. Penguin Press. Greene, J. D. (2016). Our Driverless Dilemma. Science, 352(6293), 1514–1515. Guyer, P. (2003). Kant on the Systematicity of Nature: Two Puzzles. History of Philosophy Quarterly, 20(3), 277–295. Guyer, P. (2005). Kant’s System of Nature and Freedom. Oxford University Press. Hämäläinen, N. (2009). Is Moral Theory Harmful in Practice?—Relocating Anti-theory in Contemporary Ethics. Ethical Theory and Moral Practice, 12(5), 539–553. Heathwood, C. (2015). Monism and Pluralism about Value. In I. Hirose & J. Olson (Eds.), The Oxford Handbook of Value Theory (pp. 136–157). Oxford University Press. Herrmann, D. A., & Levinstein, B. A. (2025). Standards for Belief Representations in LLMs. Minds and Machines, 35(1), 1–25. Hooker, B., & Little, M. O. (Eds.). (2000). Moral Particularism. Oxford University Press. Jang, M., Lukasiewicz, T. (2023). “Consistency Analysis of ChatGPT.” Singapore, December. Kambartel, F. (1969). “‘System’ und “Begründung” als wissenschaftliche und philosophische Ordnungsbegriffe bei und vor Kant.” In Philosophie und Rechtswissenschaft: Zum Problem ihrer Beziehung im 19. Jahrhundert. Edited by Jürgen Blühdorn and Joachim Ritter, 99–122. Frankfurt am Main: Klostermann. Kekes, J. (1993). The Morality of Pluralism. Princeton University Press. Kitcher, P. (1986). Projecting the Order of Nature. In R. Butts (Ed.), Kant’s Philosophy of Material Nature (pp. 201–235). D. Reidel. Kretzmann, Norman, & Eleonore Stump. (1989). The Cambridge Translations of Medieval Philosophical Texts: Volume 1, Logic and the Philosophy of Language. Cambridge: Cambridge University Press. Kumar, Ashutosh, & Aditya Joshi. (2022). “Striking a Balance: Alleviating Inconsistency in Pre-trained Models for Symmetric Classification Tasks.” Dublin, Ireland, May. Landes, E., Voinea, C., & Uszkai, R. (2024). Rage against the authority machines: how to design artificial moral advisors for moral enhancement. AI and SOCIETY, 1-12. Larmore, C. (1987). Patterns of Moral Complexity. Cambridge University Press. Lee, H., Phatale, S., Mansoor, H., Lu, K. R., Mesnard, T., Ferret, J., ... & Rastogi, A. (2023). Rlaif: Scaling reinforcement learning from human feedback with ai feedback. Leuenberger, M. (2024). Should You Let AI Tell You Who You Are and What You Should Do? In D. Edmonds (Ed.), AI Morality (pp. 160–169). Oxford University Press. Levinstein, B. A., & Herrmann, D. A. (2024). “Still No Lie Detector for Language Models: Probing Empirical and Conceptual Roadblocks.” Philosophical Studies, 1–27. Liu, Y., Guo, Z., Liang, T., Shareghi, E., Vulić, I., & Collier, N. (2024). “Measuring, evaluating and improving logical consistency in large language models.” arXiv arXiv:2410.02205. Losano, M. G. (1968). Sistema e struttura nel diritto, vol. 1: Dalle origini alla scuola storica. Turin: Giuffrè. MacIntyre, A. C. (2007). After Virtue: A Study in Moral Theory (3rd ed.). University of Notre Dame Press. Mason, E. (2023). “Value Pluralism.” In The Stanford Encyclopedia of Philosophy. Edited by Edward N. Zalta. Summer 2023 ed. Messer, A. (1907). Besprechung von Otto Ritschl: System und systematische Methode in der Geschichte des wissenschaftlichen Sprachgebrauchs und der philosophischen Methodologie. Göttinger Gelehrte Anzeigen, 169(8), 659–666. Millgram, E., & Thagard, P. (1996). Deliberative Coherence. Synthese, 108(1), 63–88. Nagel, T. (2001). Pluralism and Coherence. In M. Lilla, R. Dworkin, & R. Silvers (Eds.), The Legacy of Isaiah Berlin (pp. 105–111). New York Review of Books. Neurath, O. (1935). Einheit der Wissenschaft als Aufgabe. Erkenntnis, 5, 16–22. Ouyang, L., Jeffrey, Wu., Jiang, Xu., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., & Ray, A. (2023). Training language models to follow instructions with human feedback. Advances in Neural Information Processing Systems, 35, 27730–27744. Queloz, M. (2021). Choosing values? williams contra Nietzsche. The Philosophical Quarterly, 71(2), 286–307. https://doi.org/10.1093/pq/pqaa026 Queloz, M. (2024a). The Dworkin-Williams debate: Liberty, conceptual integrity, and tragic conflict in politics. Philosophy and Phenomenological Research, 109(1), 3–29. Queloz, M. (2024b). Moralism as a dualism in ethics and politics. Political Philosophy, 1(2), 433–462. https://doi.org/10.16995/pp.17532 Queloz, M. (2025). The ethics of conceptualization: Tailoring thought and language to need. Oxford University Press. https://doi.org/10.1093/9780198926283.001.0001 Rescher, N. (1981). “Leibniz and the Concept of a System.” In Leibniz’s Metaphysics of Nature: A Group of Essays, 29–41. Dordrecht: Springer. Rescher, N. (1979). Cognitive Systematization: A Systems Theoretic Approach to a Coherentist Theory of Knowledge. Blackwell. Rescher, N. (2000). Kant and the Reach of Reason: Studies in Kant’s Theory of Rational Systematization. Cambridge University Press. Rescher, N. (2005). Cognitive Harmony: The Role of Systemic Harmony in the Constitution of Knowledge. University of Pittsburgh Press. Ritschl, O. (1906). System und systematische Methode in der Geschichte des wissenschaftlichen Sprachgebrauchs und der philosophischen Methodologie. Bonn: C. Georgi. Russell, S. (2019). Human Compatible: Artificial Intelligence and the Problem of Control. Viking. Sandis, C. (2006). Dancy Cartwright: Particularism in the philosophy of science. Acta Analytica, 21(2), 30–40. Sen, A. (1981). Plural Utility. Proceedings of the Aristotelian Society, 81(1), 193–216. Sorensen, T., Jiang, L., Hwang, J. D., Levine, S., Pyatkin, V., West, P., ... & Choi, Y. (2024, March). Value kaleidoscope: Engaging ai with pluralistic human values, rights, and duties. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 38, No. 18, pp. 19937–19947). Stein, A. von der. (1968). “Der Systembegriff in seiner geschichtlichen Entwicklung.” In System und Klassifikation in Wissenschaft und Dokumentation. Edited by Alwin Diemer, 1–13. Meisenheim am Glan: A. Hain. Stocker, M. (1990). Plural and Conflicting Values. Clarendon Press. Tasioulas, J. (2022). Artificial Intelligence, Humanistic Ethics. Daedalus, 151(2), 232–243. Thompson, K. (2017). Systematicity and Normative Justification: The Method of Hegel’s Philosophical Science of Right. In T. Brooks & S. Stein (Eds.), Hegel’s Political Philosophy: On the Normative Significance of Method and System (pp. 44–66). Oxford University Press. Troje, H. E. (1969). “Wissenschaftlichkeit und System in der Jurisprudenz des 16. Jahrhunderts.” In Philosophie und Rechtswissenschaft: Zum Problem ihrer Beziehung im 19. Jahrhundert. Edited by Jürgen Blühdorn and Joachim Ritter, 63–88. Frankfurt am Main: Klostermann. Vickers, P. (2013). Understanding Inconsistent Science. Oxford University Press. Vieillard-Baron, J.-L. (1975). “Le concept de système de Leibniz à Condillac.” In Akten des II. Internationalen Leibniz-Kongresses Hannover, 17.-22. Juli 1972. Edited by Kurt Müller, Heinrich Schepers and Wilhelm Totok, 97–103. Wiesbaden: F. Steiner. Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., ... & Fedus, W. (2022). Emergent abilities of large language models. arXiv preprint arXiv:2206.07682. Wiggins, D., & Williams, B. (1978). “Aurel Thomas Kolnai.” In Ethics, Value and Reality: Aurel Kolnai, xxiii–xxxix. New Brunswick, NJ: Transaction Publishers. Williams, B. (1973). “Ethical Consistency.” In Problems of the Self, 166–186. Cambridge: Cambridge University Press. Williams, B. (1981a). “Conflicts of Values.” In Moral Luck, 71–82. Cambridge: Cambridge University Press. Williams, B. (1981b). “Moral Luck.” In Moral Luck, 20–39. Cambridge: Cambridge University Press. Williams, B. (1985). Ethics and the Limits of Philosophy. Routledge (Classics). Routledge. Williams, B. (1995a). “Formal and Substantial Individualism.” In Making Sense of Humanity and Other Philosophical Papers 1982–1993, 123–34. Cambridge: Cambridge University Press. Williams, B. (1995b). “The Point of View of the Universe: Sidgwick and the Ambitions of Ethics.” In Making Sense of Humanity and Other Philosophical Papers 1982–1993, 153–71. Cambridge: Cambridge University Press. Williams, B. (1995c). “What Does Intuitionism Imply?.” In Making Sense of Humanity and Other Philosophical Papers 1982–1993, 182–191. Cambridge: Cambridge University Press. Williams, B. (2013). “Introduction.” In Concepts and Categories: Philosophical Essays. Edited by Henry Hardy. 2nd ed, xxix–xxxix. Princeton: Princeton University Press. Williams, B. (2001). Morality: An Introduction to Ethics. Cambridge University Press. Williams, B. (2002). Truth and truthfulness: An essay in genealogy. Princeton University Press. Williams, B. (2005a). From Freedom to Liberty: The Construction of a Political Value. In G. Hawthorne (Ed.), In the Beginning Was the Deed: Realism and Moralism in Political Argument (pp. 75–96). Princeton University Press. Williams, B. (2005b). Pluralism, Community and Left Wittgensteinianism. In G. Hawthorne (Ed.), In the Beginning Was the Deed: Realism and Moralism in Political Argument (pp. 29–39). Princeton University Press. Ypi, L. (2021). The Architectonic of Reason: Purposiveness and Systematic Unity in Kant’s Critique of Pure Reason. Oxford University Press. Zhao, Y., Yan, L., Sun, W., Xing, G., Wang, S., Meng, C., ... & Yin, D. (2024). Improving the robustness of large language models via consistency alignment. arXiv preprint arXiv:2403.14221. Zhou, J., Ghaddar, A., Zhang, G., Ma, L., Hu, Y., Pal, S., ... & Hao, J. (2024). Enhancing logical reasoning in large language models through graph-based synthetic data. arXiv preprint arXiv:2409.12437. 出版商注 Springer Nature 在已发表地图和机构隶属关系方面保持中立。

Abela, P. (2006). The Demands of Systematicity: Rational Judgment and the Structure of Nature. In G. Bird (Ed.),A Companion to Kant(pp. 408–422). Blackwell.

Amodei, D. (2024). “What if Dario Amodei Is Right About A.I.?” Interview by Ezra Klein.The Ezra Klein Show, New York Times Opinion, April 12, 2024. https://www.nytimes.com/2024/04/12/opinion/ezra-klein-podcast-dario-amodei.html
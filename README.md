
## 本项目主要通过阅读源码，系统记录langchain的所有知识点
# langchain
## langchain生态介绍
langchain是一个用于开发以大模型作为底层能力支持的应用的框架，你如果要开发一个基于大模型的的应用，那么选择langchain会方便很多。 因为它为大模型应用产品提供了全生命周期管理方案。
1. 应用的全生命周期管理
   2. 应用开发：用langchain提供的组件进行项目开发，或者用langGraph提供有状态的应用开发
   3. 项目监控：用langsmith提供实时的调试、监控和评估，为项目的迭代提供依据
   4. 项目部署：使用LangServe或者langchain cloud部署项目，对外暴露REST API风格接口

上面所讲的langchain其实是一整个生态，包括了langchain模块、langsmith模块、langGraph模块、LangServe模块，以及langchain cloud，每个模块都提供了不一样的能力
而langchain是我们从无到有开发产品时要用到的开发框架，那下面就具体来说langchain模块

## langchain
langchain是提供大模型应用开发的开发框架，其主要有两个大块组成
1. langchain-core : langchain底层的抽象框架，以及为lagnchain自家标榜的LCEL表达语言提供支持
2. langchian-community：第三方的集成，其中诸如openai、google、阿里等等第三方公司的能力的集成，这个能力包括大模型能力、搜索能力、embedding能力等等，不局限于大模型的能力
还有一个需要注意的是，有些第三方的支持会被独立的抽取出来，提供更轻量化的支持，比如langchain-openai，langchain-anthropic

本质上来说，langchian-community只是继承了langchain-core，实现了底层定义的抽象，所以langchian的核心的核心都在langchain-core，
langchain-core既为第三方的扩展提供了标准，也为langchain自身设计奠定了基调，那langchain的设计基调是什么呢？是LCEL

## LCEL
LCEL是langchain所标榜的一个设计原则，它以一种以声明式的形式将langchain的各个组件链接起来，这里讲一下声明式，声明式意思就是说你只用关心输入和输出
关于模块本身的实现细节，并不需要你去关心，这样就有一个好处，在langchain中设计了很多的组件，只要一个组件的输出格式满足另一个组件的输入，就可以把
它串行起来。而这些关于LCEL的底层支持都来自于runnable，runnable是一个类，几乎在langchain中的所有组件都继承了这个类。

## runnable
runnable是langchain的一基类，而所有的组件都是runnable的子类，包括聊天模型、LLM、输出解析器、检索器、提示模板等，甚至你组成的chain也是
runnable的子类：RunnableSequence或者是RunnableParalle，总之，几乎所有的组件都是runnable的子类。

而runnable本身定义了一些标准的接口，用于子类去实现，其中比较重要的几个标准接口包括
invoke：提供单个输入，得到单个输出
batch：提供多个输入，得到多个输出
stream：提供单个输入，得到流式输出

ainvoke:invoke的异步
abatch：batch的异步
astream：stream的异步
# 前提回顾
前面已经讲了什么是prompt模板，以及什么是prompt和prompt value，并且用langchain来实现了一个中英翻译助手,下面是部分代码，如果要看完整代码，请看上一小节
[prompt第二讲-langchain实现中英翻译助手](prompt第二讲-langchain实现中英翻译助手.md)
```python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/8 9:44
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate
# 1. prompt模板定义
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
```
从上面可以看出，定义prompt模板用到的是PromptTemplate，所以下面就来讲讲PromptTemplate
# PromptTemplate
首先来讲讲prompt模板的定义，定义出了模板之后，就可以根据不同的变量来产出不同的prompt value，prompt value
就可以随时的转为字符串和message，字符串就是我们说的prompt，message最终底层也是转为字符串的，也是prompt。          
那在langchain中，prompt模板定义方法有很多种，而PromptTemplate是其中的一种
## prompt 模板定义
通过PromptTemplate的from_template方法来定义出一个PromptTemplate
### 以f-string渲染格式
```python
from langchain_core.prompts import PromptTemplate
# 1. prompt模板定义
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
print(prompt_template.template)
print(prompt_template.input_variables)
print(prompt_template.template_format)
print(prompt_template.input_types)
print(prompt_template.partial_variables)
```
**代码原理**
1. 传入一个具有一定格式的字符串，上面默认是python原生支持的f-string格式形式，变量要以{}的形式。
2. 传入到PromptTemplate的from_template方法后，会默认根据f-string的形式来解析这个字符串，提取出中括号里的变量
3. 根据解析出的内容实例化一个PromptTemplate对象，将传入的字符串放到template中，提取的变量放到input_variables中

### 以mustache渲染格式
上面是默认以f-string的格式识别和处理传入的模板，我们可以不显示的指定参数，但是如果以mustache形式渲染，则需要显示的指定，
mustache则是以{{}}的形式来定义变量
```python
from langchain_core.prompts import PromptTemplate
# 1. prompt模板定义
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{{user_input_words}}->answer：
""",
template_format="mustache")
print(prompt_template.template)
print(prompt_template.input_variables)
print(prompt_template.template_format)
print(prompt_template.input_types)
print(prompt_template.partial_variables)
```
### 以jinja2渲染格式
jinja2定义变量的形式和mustache是一样的，都是{{}}的形势
```python
from langchain_core.prompts import PromptTemplate
# 1. prompt模板定义
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{{user_input_words}}->answer：
""",
template_format="jinja2")
print(prompt_template.template)
print(prompt_template.input_variables)
print(prompt_template.template_format)
print(prompt_template.input_types)
print(prompt_template.partial_variables)
```
### 直接实例化PromptTemplate
在第一个以f-string那部分我进行了简单的代码讲解，我们发现其实本质上就是先解析我丢进去的模板，然后将解析的内容作为参数，来实例化一个PromptTemplate
既然最终都要实例化PromptTemplate对象，那为啥不直接就来实例化呢？下面我们就直接来实例化PromptTemplate，顺便也能看到langchain定义的这个模板内部
是什么结构。
```python
from langchain_core.prompts import PromptTemplate
prompt_template = PromptTemplate(template="""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{{user_input_words}}->answer：
""",
input_variables=['user_input_words'])
print(prompt_template.template)
print(prompt_template.input_variables)
print(prompt_template.template_format)
print(prompt_template.input_types)
print(prompt_template.partial_variables)
```
### PromptTemplate核心变量
从最后直接实例化方法和我添加的print打印的信息来看，我们先来看看PromptTemplate具有的几个最核心的字符串
1. template：用于存储字符串模板
2. input_variables：用于存储变量，这个变量可以是直接从字符串模板中解析出来，也可以是自己指定，只要是和模板中的变量一样就行
3. template_format：渲染的格式，这个格式指导着如何解析template
4. partial_variables：这是一个前置变量，可以被前置定义，这个我后面用到的时候会自然的引出

前三种方法和最后一种的差别只是在于，前三种帮我们自动提取了变量，而最后一种则是我们直接告诉PromptTemplate变量是谁

## prompt value生成
PromptTemplate因为继承了底层的runnable，所以关于prompt valu的生成都是遵守runnable的接口的（invoke ainvoke batch ...）
通过这些接口可以将用户传入的变量添加到prompt模板中生成1个或者多个prompt
### invoke
invoke实现了单输入单输出的关系，通常要求传入一个关于变量赋值的字典，生成prompt value。传入的字典中：
key为模板变量，value为具体的变量值
```python
from langchain_core.prompts import PromptTemplate
# 1. 以f-string格式渲染
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
# 1.1. invoke传入字典
prompt = prompt_template.invoke({"user_input_words":"你好"})
print(prompt)
```
但是如果模板中变量只有一个，可以直接传入值，而无需指定变量（出于规范考虑，不建议直接传入变量）
```python
from langchain_core.prompts import PromptTemplate
# 1. 以f-string格式渲染
prompt_template = PromptTemplate.from_template("""
你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
examples：
question：美丽->beautiful;
question：男孩->boy;
question：男人->man；
question：456->four hundred and fifty-six;
question：1->one;
question：34->thirty-four
question：{user_input_chinese}
""")
prompt = prompt_template.invoke("你好")
print(prompt)
```
下面根据源码讲解一下invoke的原理
**invoke原理**
1. 校验config
2. 校验输入变量         
   3. 输入变量如果不是一个字典，并且模板中只有一个变量的话，就会将input_variables中保存的变量名拿出来，组成一个字典        
   4. 如果传入的是一个字典，如果字典和保存在input_variables中有差异，则报错。          
   5. 返回校验后的输入字典         
3. 格式化模板（交给子类），生成prompt value
**注意**：最后的结果中，生成是一个prompt value，而不是一个prompt，前面也提到了，这和prompt的差别就在于prompt value提供了字符串到message的互转

#### format_prompt(不建议使用)
```python
from langchain_core.prompts import PromptTemplate
# 1. 以f-string格式渲染
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
prompt= prompt_template.format_prompt(user_input_words="你好")
print(prompt)
```
这个方法本质上就是直接完成invoke的第3步的工作，invoke第3步就是调用了这个方法，所以可以说这个方法和invoke的差别在于少了一些前置的校验。   
同时呢？考虑到和runnable的使用范式的统一，这个方法我个人是不建议使用。
#### format(不建议使用)
```python
from langchain_core.prompts import PromptTemplate
# 1. 以f-string格式渲染
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
prompt= prompt_template.format(user_input_words="你好")
print(prompt)
```
这个方法本质上就是是完成format_prompt的子任务，等于说format是直接生成了一个字符串的prompt，format_prompt进一步将其包装为prompt value
同样的，考虑到和runnable的使用范式的统一，这个方法我个人是不建议使用。

### batch
batch实现了多输入多输出的关系，传入多组变量字典，生成多个prompt value
```python
from langchain_core.prompts import PromptTemplate
# 1. 以f-string格式渲染
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
prompt = prompt_template.batch([{"user_input_words":"你好"},{"user_input_words":"你是谁？"}])
print(prompt)
```
batch的本质我已经在最开始就讲过，如果没有特殊情况，遵从的就是runnable的batch设计原理：[runnable底层原理](runnable底层原理.md)

### stream
batch实现了流式输出效果，流式输出prompt value
```python
from langchain_core.prompts import PromptTemplate
# 1. 以f-string格式渲染
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
for i in prompt_template.stream({"user_input_words":"Jinja2 是一个功能更加强大的 Python 模板引擎，常用于 Web 开发，尤其是 Flask 和 Django 框架中。它支持复杂的控制结构，如循环和条件语句"}):
    print(i)
```
这里其实是看不出流输出的感觉的，是因为prompt value本身就不支持挨个yield单个字词出来，关于它的原理，参考我之前讲的：：[runnable底层原理](runnable底层原理.md)
#### ainvoke
异步实现单输入单输出关系
```python
import asyncio
from langchain_core.prompts import PromptTemplate
# 1. 以f-string格式渲染
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
async def main():
    return await asyncio.gather(prompt_template.ainvoke({"user_input_words":"你好"}),prompt_template.ainvoke({"user_input_words":"我不好"}))

res = asyncio.run(main())
print(res)
```
ainvoke的本质我已经在最开始就讲过，如果没有特殊情况，遵从的就是runnable的ainvoke设计原理：[runnable底层原理](runnable底层原理.md)

其他的还有abatch、astream，道理是差不多的。

### PromptTemplate核心方法
前面总结了PromptTemplate的几个核心变量，现在总结一下PromptTemplate核心方法
1. invoke：单输入单输出关系，传递一组变量字典，得到一个prompt value        
   2. format_prompt:invoke的底层支持，生成prompt value      
   3. format:format_prompt的底层支持，生成字符串prompt         
2. batch：多输入多输出关系，传递多组变量字典，得到多个prompt value
3. stream：流式输出prompt value
4. ainvoke：异步invoke
5. abatch：异步batch
6. astream：异步stream

### partial变量
上面我们举了一个中文到英文的翻译助手    
现在我们可以做得更宽泛一些，可以做一个翻译助手，至于是翻译什么语言到什么语言，则交给用户自己去定义   
这里就用到了partital，它本质就是在生成真正的prompt前先固定一些变量，根据partital变量生成一个新的prompt模板
下面还是通过两种方法来讲解这个变量
#### partial方法
```python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/8 9:44
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate
# 4. 定义部分变量
prompt_template = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
lag2lag = input("你想我成为什么翻译助手(格式如：中文-英文)：")
source_language,dst_language = lag2lag.split('-')
new_prompt_template = prompt_template.partial(source_language=source_language,dst_language=dst_language)
print("助手初始化完毕，您的翻译助手上线！！！")
# 2. llm定义
from langchain_community.llms import Tongyi
from pydantic_settings import BaseSettings,SettingsConfigDict

"""
2,1 获取千问的key
我这么写的原因是因为方便我上传项目到github的同时，不暴露我的key，所以我把可以key保存到了最外部的一个.env文件中
这样我每一次同步到github的时候就不会把key也推出去，你们测试的时候，可以直接写成
qwen_key="sk-cc2209cec48c4bc966fb4acda169e",这样省事。
"""
class ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="../../../.env",env_file_encoding="utf-8")
    qwen_key:str
    deepseek_key:str
    deepseek_base_url:str

model_config = ModelConfig()
qwen_key = model_config.qwen_key
# 1. 读取配置信息,获取模型key
llm = Tongyi(dashscope_api_key=qwen_key)


while(True):
    user_input_word = input(f"请输入需要翻译的{source_language}：")
    if user_input_word.lower() =="quit":
        break
    else:
        prompt = new_prompt_template.invoke({"user_input_words":user_input_word})
        print(llm.invoke(prompt))
```
下面分析一下原理
**partial方法原理**
1. 传入变量并赋值到初始的prompt模板中，生成新的prompt模板
2. 传入的变量保存到partical_variables中
3. 从最开始模板中的input_variables中剔除partical_variables部分，
**也就是说，最开始所有的变量都属于input_variables，当你调用了partial方法之后，input_variables中的部分变量会被移动到partical_variables中**
#### 直接实例化指定partical_variables
```python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/8 9:44
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate
# 4. 定义部分变量
lag2lag = input("你想我成为什么翻译助手(格式如：中文-英文)：")
source_language,dst_language = lag2lag.split('-')

prompt_template = PromptTemplate(template="""
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
"""
,input_variables=["user_input_words"]
,partial_variables={'source_language':source_language,"dst_language":dst_language})

print("助手初始化完毕，您的翻译助手上线！！！")
# 2. llm定义
from langchain_community.llms import Tongyi
from pydantic_settings import BaseSettings,SettingsConfigDict

"""
2,1 获取千问的key
我这么写的原因是因为方便我上传项目到github的同时，不暴露我的key，所以我把可以key保存到了最外部的一个.env文件中
这样我每一次同步到github的时候就不会把key也推出去，你们测试的时候，可以直接写成
qwen_key="sk-cc2209cec48c4bc966fb4acda169e",这样省事。
"""
class ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="../../../.env",env_file_encoding="utf-8")
    qwen_key:str
    deepseek_key:str
    deepseek_base_url:str

model_config = ModelConfig()
qwen_key = model_config.qwen_key
# 1. 读取配置信息,获取模型key
llm = Tongyi(dashscope_api_key=qwen_key)


while(True):
    user_input_word = input(f"请输入需要翻译的{source_language}：")
    if user_input_word.lower() =="quit":
        break
    else:
        prompt = prompt_template.invoke({"user_input_words":user_input_word})
        print(llm.invoke(prompt))
```

### save保存
ok了，现在我们开发好了一个翻译助手了，核心就是设计了一个prompt模板，现在我想要发布到开源社区或者给别人
使用，我们可以保存这个模板，但是需要注意两点：
1. 如果你的模板里含有partial_variables，是无法保存的；
2. 只能保存为json格式或者是yml格式
所以综合这两种考虑，我们不能保存调用过partial方法后的prompt模板，也不能保存直接实例化时指定了partial_variables的模板，我们只能保存最初的模板，这也符合需求，因为你保存了调用
partial后的模板的话，这些前置变量的值都被填进去了，用户也没法自定义，也就失去了这个模板的意义，所以下面演示一下如何保存最初的prompt模板

**最重要：你可以观察一下保存后的文件，如果有中文，则只会显示16进制，但是现在的保存方法，是不支持传入编码参数的，如果你要让他正常显示中文和加载中文，需要到源码下的修改save方法，
在open的时候加入编码参数,这一点来看langchain还是不够国际化，垃圾**
```python
from langchain_core.prompts import PromptTemplate
# 5. 保存prompt模板
from langchain_core.prompts import PromptTemplate
# 5. 保存prompt模板
prompt_template_1 = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
prompt_template_1.save("./data/translate-lang2lang.yml")
```
### from_file加载
加载上一步保存的prompt模板文件，加载之后又可以正常使用partical了。
同样的，需要注意编码问题。
```python
from langchain_core.prompts import PromptTemplate
prompt_template = PromptTemplate.from_file("data/translate-lang2lang.yml")
lag2lag = input("你想我成为什么翻译助手(格式如：中文-英文)：")
source_language,dst_language = lag2lag.split('-')
new_prompt_template = prompt_template.partial(source_language=source_language,dst_language=dst_language)
print(new_prompt_template)
```
其他的还有一些方法和属性，下面简单的列举一下
### dict
将prompt模板转为字典
```python
from langchain_core.prompts import PromptTemplate
# 5. 保存prompt模板
prompt_template_1 = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")
print(prompt_template_1.dict())
```
#### __add__
实现了prompt模板之间的相加
```python
from langchain_core.prompts import PromptTemplate
# 5. 保存prompt模板
prompt_template_1 = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")

prompt_template_3 = PromptTemplate.from_template("""这是第二个prompt模板:{user_input_words_3}""")
new_prompt = prompt_template_1+"这是新的模板：{user_input_words_2}"+prompt_template_3
print(new_prompt)
```
从上面可以看出，相加的对象可以是多个PromptTemplate之间，也可以是PromptTemplate和字符串直接
本质上就是将模板统一，变量统一
#### from_examples
根据案例实例化一个PromptTemplate（不够优雅，不细讲了，后面会有更优雅的方法）

### 属性
```python
from langchain_core.prompts import PromptTemplate
# 5. 保存prompt模板
prompt_template_1 = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{user_input_words}->answer：
""")

print(prompt_template_1.InputType)
print(prompt_template_1.OutputType)
print(prompt_template_1.input_schema)
print(prompt_template_1.output_schema)
print(prompt_template_1.config_schema)
```
稍微总结一下：
1. InputType:获取输入类型
2. OutputType：获取输出类型
3. input_schema：获取输入schema
4. output_schema：获取输出schema
5. config_schema：获取config的schema

## 总结
基本上PromptTemplate也已将讲完了，下面做一个小总结
1. 变量       
   2. template：用于存储字符串模板      
   3. input_variables：用于存储变量，这个变量可以是直接从字符串模板中解析出来，也可以是自己指定，只要是和模板中的变量一样就行           
   4. template_format：渲染的格式，这个格式指导着如何解析template           
   5. partial_variables：这是一个前置变量，可以被前置定义           
2. 方法        
   1. invoke：单输入单输出关系，传递一组变量字典，得到一个prompt value        
      2. format_prompt:invoke的底层支持，生成prompt value       
      3. format:format_prompt的底层支持，生成字符串prompt         
   2. batch：多输入多输出关系，传递多组变量字典，得到多个prompt value           
   3. stream：流式输出prompt value         
   4. ainvoke：异步invoke        
   5. abatch：异步batch        
   6. astream：异步stream        
   7. dict：将prompt模板转为字典      
3. 属性        
   1. InputType:获取输入类型       
   2. OutputType：获取输出类型        
   3. input_schema：获取输入schema        
   4. output_schema：获取输出schema        
   5. config_schema：获取config的schema        

## 遗留问题
从案例来说，还有一个问题，就是当我们在做翻译助手的时候，当我们是中英文翻译助手的时候，案例是符合我们的标准的，但是当我们是其他的翻译助手
时，比如中德翻译时，案例就对不上了，这也是下一章我们要解决的问题。
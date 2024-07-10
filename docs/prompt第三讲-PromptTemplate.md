# 前提回顾
前面已经讲了什么是prompt模板，以及什么是prompt，并且用langchain来实现了一个中英翻译助手,下面是部分代码，如果要看完整代码，请看上一小节
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
首先来讲讲prompt模板的定义，定义出了模板之后，就可以根据不同的变量来产出不同的prompt。          
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
从最后直接实例化方法和我添加的print打印的信息来看，我们先来看看PromptTemplate具有的几个最核心的字符串
1. template：用于存储字符串模板
2. input_variables：用于存储变量，这个变量可以是直接从字符串模板中解析出来，也可以是自己指定，只要是和模板中的变量一样就行
3. template_format：渲染的格式，这个格式指导着如何解析template
4. partial_variables：这是一个前置变量，可以被前置定义，这个我后面用到的时候会自然的引出

前三种方法和最后一种的差别只是在于，前三种帮我们自动提取了变量，而最后一种则是我们直接告诉PromptTemplate变量是谁
**注意：不管是直接实例化，还是**
## prompt 生成
PromptTemplate因为继承了底层的runnable，所以关于prompt的生成都是遵守runnable的接口的（invoke ainvoke batch ...）
### invoke
invoke实现了单输入单输出的关系，通常要求传入一个关于变量赋值的字典key为变量，value为具体的值
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
**invoke原理**
1. 校验config
2. 校验输入变量 
   3. 输入变量如果不是一个字典，并且模板中只有一个变量的话，就会将input_variables中保存的变量名拿出来，组成一个字典   
   4. 如果传入的是一个字典，如果字典和保存在input_variables中有差异，则报错。  
   5. 返回校验后的输入字典
3. 格式化模板（交给子类），生成prompt value
**注意**：最后的结果中，生成是一个prompt value，而不是一个prompt，前面也提到了，这和prompt的差别就在于prompt value提供了字符串到message的互转

### format_prompt(不建议使用)
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
### format(不建议使用)
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
batch实现了多输入多输出的关系
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
batch实现了流式输出效果
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
这里其实是看不出流输出的感觉的，是因为prompt本身就不支持挨个yield单个字词出来，关于它的原理，参考我之前讲的：：[runnable底层原理](runnable底层原理.md)
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
****



### partial
上面我们举了一个中文到英文的翻译助手    
现在我们可以做得更宽泛一些，可以做一个翻译助手，至于是翻译什么语言到什么语言，则交给用户自己去定义   
这里就用到了partital，它本质就是在生成真正的prompt前先固定死一些变量。
```python
from langchain_core.prompts import PromptTemplate
prompt_template = PromptTemplate.from_template("""
你是一个{language2language}翻译助手，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
examples：
question：beautiful->美丽;
question：boy->男孩;
question：man->男人；
question：four hundred and fifty-six->456;
question：one->1;
question：thirty-four->34;
question：{user_input_chinese}->
""")
lag2lag = input("你想我成为什么语言到什么语言的助手：")
new_prompt_template = prompt_template.partial(language2language=lag2lag)
print("助手初始化完毕，可以开始使用助手！！！")

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
    model_config = SettingsConfigDict(env_file="../../.env",env_file_encoding="utf-8")
    qwen_key:str
    deepseek_key:str
    deepseek_base_url:str

model_config = ModelConfig()
qwen_key = model_config.qwen_key
# 1. 读取配置信息,获取模型key
llm = Tongyi(dashscope_api_key=qwen_key)


while(True):
    user_input_word = input("请输入需要翻译的中文：")
    if user_input_word.lower() =="quit":
        break
    else:
        prompt = new_prompt_template.invoke({"user_input_chinese":user_input_word})
        print(llm.invoke(prompt))
```
**partial原理**
1. 传入变量并赋值到初始的prompt模板中，生成新的prompt模板
2. 传入的变量保存到partical_variables中
2. 从最开始模板中的input_variables中剔除partical_variables部分


#### save保存
只能保存为json格式或者是yml格式
```python
from langchain_core.prompts import PromptTemplate
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
prompt_template.save("./data/chinese2english.yml")
```
#### from_file加载

```python
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_file("../scripts/prompt/data/chinese2english.yml")
print(prompt_template)
```
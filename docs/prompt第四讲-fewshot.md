## 前提回顾
前面已经实现了一个翻译助手了[prompt第三讲-PromptTemplate](prompt第三讲-PromptTemplate.md)，prompt模板设计中，有说明、案例、和实际的问题
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
## FewShotPromptTemplate
下面我们换一种更加优雅的方式来实现上面的prompt模板
```python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/9 9:44
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
example_prompt = PromptTemplate.from_template("question: {question}->answer:{answer}")
examples = [
    {'question':'美丽',"answer":'beautiful'},
    {'question':'男孩',"answer":'boy'},
    {'question':'男人',"answer":'man'},
    {'question':'456',"answer":'four'},
    {'question':'456',"answer":'four hundred and fifty-six'},
    {'question':'1',"answer":'one'},
    {'question':'34',"answer":'thirty-four'}
]
prefix = """
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：
## history examples:
"""
suffix = """
## user true task:
question：{user_input_words}->answer：
"""
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=['user_input_words','source_language','dst_language']
)

lag2lag = input("你想我成为什么翻译助手(格式如：中文-英文)：")
source_language,dst_language = lag2lag.split('-')
new_prompt_template = prompt_template.partial(source_language=source_language,dst_language=dst_language)


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
着重看一下FewShotPromptTemplate定义模板部分，他没有什么方式可以实例化对象，只支持直接实例化，而实例化
要传入的参数也不用咋说，格式一目了然
**参数讲解**
1. example_prompt：你想要案例遵守的prompt模板格式
2. examples一个案例列表，里面是多个字典，字典的key必须和example_prompt中定义的变量是统一的
3. prefix：你想要在案例前面插入的内容，如果是接着前面的翻译助手，那这里通常就是这个助手的能力说明
4. suffix:通常就是你想要最后插入的实际的问题的prompt模板
5. input_variables：变量说明，这个变量来自prefix和suffix

## foramt格式化
因为FewShotPromptTemplate也是继承自runnable的，所以他有的方法和变量基本和前面讲的PromptTemplate差不多，
变量可能会有些变化，但是方法基本是统一的，也是遵从（invoke，batch,stream那一套的），而invoke最底层是
调用了format，所以我只需要讲解一下format，其他的都懂了

format的原理如下：
1. 遍历examples列表，根据example_prompt模板格式，实例化出一个prompt列表，并且以空格的形式进行拼接成一个字符串
2. 将prefix添加到第一步得到prompt字符串前面，将suffix添加到prompt字符串后面
3. 将输入的变量填入新的模板中，得到格式化后的prompt


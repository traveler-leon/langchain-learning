# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/9 10:30
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate

example_prompt = PromptTemplate.from_template("{source_language}-{dst_language}任务 question: {question}->answer:{answer}")
examples = [
    {'source_language':'中文','dst_language':"英文",'question':'美丽',"answer":'beautiful'},
    {'source_language':'中文','dst_language':"英文",'question':'男孩',"answer":'boy'},
    {'source_language':'中文','dst_language':"英文",'question':'男人',"answer":'man'},
    {'source_language':'中文','dst_language':"英文",'question':'456',"answer":'four'},
    {'source_language':'中文','dst_language':"英文",'question':'456',"answer":'four hundred and fifty-six'},
    {'source_language':'中文','dst_language':"英文",'question':'1',"answer":'one'},
    {'source_language':'中文','dst_language':"英文",'question':'34',"answer":'thirty-four'},
    {'source_language':'英文','dst_language':"中文",'question': 'beautiful', "answer": '美丽'},
    {'source_language':'英文','dst_language':"中文",'question':'thirty-four',"answer":'34'},
    {'source_language':'英文','dst_language':"中文",'question':'man',"answer":'男人'},
    {'source_language':'中文','dst_language':"日文",'question': '你好', "answer": 'こんにちは'},
    {'source_language':'中文','dst_language':"日文",'question': '123', "answer": '百二十三'},
    {'source_language':'中文','dst_language':"日文",'question': '美丽', "answer": '美しい'},
]
prefix = """
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：
## history examples:
"""
suffix = """
## user true task:
{source_language}-{dst_language}任务 question：{user_input_words}->answer：
"""

from langchain_core.example_selectors.base import BaseExampleSelector
class CustomExampleSelector(BaseExampleSelector):
    def __init__(self, examples):
        self.examples = examples

    def add_example(self, example):
        self.examples.append(example)

    def select_examples(self, input_variables):
        # This assumes knowledge that part of the input will be a 'text' key
        source_language = input_variables['source_language']
        dst_language = input_variables['dst_language']
        task = '-'.join((source_language,dst_language))
        batch_example = list()
        for example in self.examples:
            if task=='-'.join((example["source_language"],example['dst_language'])):
                batch_example.append(example)
        batch_len = min(3,len(batch_example))
        return batch_example[:batch_len]

example_selector = CustomExampleSelector(examples)

prompt_template = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=['user_input_words','source_language','dst_language']
)

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


lag2lag = input("你想我成为什么翻译助手(格式如：中文-英文)：")
source_language,dst_language = lag2lag.split('-')

while(True):
    user_input_word = input(f"请输入需要翻译的{source_language}：")
    if user_input_word.lower() =="quit":
        break
    else:
        prompt = prompt_template.invoke({'source_language':source_language,'dst_language':dst_language,'user_input_words':user_input_word})
        print(llm.invoke(prompt))

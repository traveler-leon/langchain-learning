# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/9 10:30
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_chroma import Chroma
from langchain_core.example_selectors import (
    SemanticSimilarityExampleSelector,
    MaxMarginalRelevanceExampleSelector,
    LengthBasedExampleSelector)
from pydantic_settings import BaseSettings,SettingsConfigDict
from langchain_community.embeddings import DashScopeEmbeddings

example_prompt = PromptTemplate.from_template("question: {question}->answer:{answer}")
examples = [
    {'question':'美丽',"answer":'beautiful'},
    {'question':'男孩',"answer":'boy'},
    {'question':'男人',"answer":'man'},
    {'question':'456',"answer":'four'},
    {'question':'456',"answer":'four hundred and fifty-six'},
    {'question':'1',"answer":'one'},
    {'question':'34',"answer":'thirty-four'},
    {'question': 'beautiful', "answer": '美丽'},
    {'question':'thirty-four',"answer":'34'},
    {'question':'man',"answer":'男人'},
    {'question': '你好', "answer": 'こんにちは'},
    {'question': '123', "answer": '百二十三'},
    {'question': '美丽', "answer": '美しい'},
]
prefix = """
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：
## history examples:
"""
suffix = """
## user true task:
question：{user_input_words}->answer：
"""

class ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="../../../.env", env_file_encoding="utf-8")
    qwen_key:str
    deepseek_key:str
    deepseek_base_url:str

model_config = ModelConfig()
qwen_key = model_config.qwen_key
# 1. 引入embedding模型
embeddings = DashScopeEmbeddings(model="text-embedding-v1", dashscope_api_key=qwen_key)
# 2. 创建案例选择器
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    embeddings,
    Chroma,
    k=3
)
# 3. 创建fewshot模版
prompt_template = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=['user_input_words','source_language','dst_language']
)
lag2lag = input("你想我成为什么翻译助手(格式如：中文-英文)：")
source_language,dst_language = lag2lag.split('-')
new_prompt_template = prompt_template.partial(source_language=source_language,dst_language=dst_language)
prompt = new_prompt_template.invoke({'user_input_words':"hello"})
print(prompt.to_string())
#
# #支持保存，但是不支持加载

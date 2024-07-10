# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/9 10:30
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from pydantic_settings import BaseSettings,SettingsConfigDict
from langchain_community.embeddings import DashScopeEmbeddings
class ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="../../../.env", env_file_encoding="utf-8")
    qwen_key:str
    deepseek_key:str
    deepseek_base_url:str

model_config = ModelConfig()
qwen_key = model_config.qwen_key
embeddings = DashScopeEmbeddings(model="text-embedding-v1", dashscope_api_key=qwen_key)

example_selector = SemanticSimilarityExampleSelector.from_examples(

)

# example_prompt = PromptTemplate.from_template("question: {question}")
# examples = [
#     {'question':'美丽->beautiful'},
#     {'question':'男孩->boy'},
#     {'question':'男人->man'},
#     {'question':'456->four'},
#     {'question':'456->four hundred and fifty-six'},
#     {'question':'1->one'},
#     {'question':'34->thirty - four'}
# ]
#
# prompt_template = FewShotPromptTemplate(
#     examples=examples,
#     example_prompt=example_prompt,
#     prefix="你是一个{lag2lag}文翻译助手，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,",
#     suffix="true question:{input}",
#     input_variables=['input','lag2lag']
# )
#
# new_prompt_template = prompt_template.partial(lag2lag="中德")
#
# prompt = new_prompt_template.invoke({'input':"你好"})
# print(prompt.to_string())
#
# #支持保存，但是不支持加载

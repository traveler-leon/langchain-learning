# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/2 15:46
@Auth ： leon
"""
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda,RunnableGenerator
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Iterator
from pydantic_settings import BaseSettings,SettingsConfigDict
# 1. 读取配置信息,获取模型key
class ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="../../../.env", env_file_encoding="utf-8")
    qwen_key:str
    deepseek_key:str
    deepseek_base_url:str

model_config = ModelConfig()
qwen_key = model_config.qwen_key

model = ChatTongyi(dashscope_api_key=qwen_key)
promot = ChatPromptTemplate.from_messages("Give me a 3 word chant about {topic}")
chant_chain = model | model | StrOutputParser()


def character_generator(input: Iterator[str]) -> Iterator[str]:
    for token in input:
        if "," in token or "." in token:
            yield "👏" + token
        else:
            yield token
runnable = chant_chain | RunnableGenerator(character_generator)
for i in runnable.stream({"topic": "waste"}):
    print(i)
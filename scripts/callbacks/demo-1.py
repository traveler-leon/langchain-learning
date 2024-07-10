# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/2 9:16
@Auth ： leon
"""
from typing import Any, Dict, List
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.outputs import LLMResult
from langchain_core.prompts import ChatPromptTemplate
from pydantic_settings import BaseSettings,SettingsConfigDict
# 1. 读取配置信息,获取模型key
class ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="../../../.env", env_file_encoding="utf-8")
    qwen_key:str
    deepseek_key:str
    deepseek_base_url:str

model_config = ModelConfig()
qwen_key = model_config.qwen_key
class LoggingHandler(BaseCallbackHandler):
    def on_chat_model_start(
        self, serialized: Dict[str, Any], messages: List[List[BaseMessage]], **kwargs
    ) -> None:
        print("Chat model started")

    def on_llm_end(self, response: LLMResult, **kwargs) -> None:
        print(f"Chat model ended, response: {response}")

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs
    ) -> None:
        print(f"Chain {serialized.get('name')} started")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs) -> None:
        print(f"Chain ended, outputs: {outputs}")


callbacks = [LoggingHandler()]
llm = ChatTongyi(dashscope_api_key=qwen_key)
prompt = ChatPromptTemplate.from_template("What is 1 + {number}?")

chain = prompt | llm

res = chain.invoke({"number": "2"}, config={"callbacks": callbacks})
print(res)
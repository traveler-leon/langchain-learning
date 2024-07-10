# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 10:07
@Auth ： leon
"""
from pydantic_settings import BaseSettings,SettingsConfigDict
# 1. 读取配置信息,获取模型key
class ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="../../.env", env_file_encoding="utf-8")
    qwen_key:str
    deepseek_key:str
    deepseek_base_url:str

model_config = ModelConfig()
qwen_key = model_config.qwen_key
deepseek_key = model_config.deepseek_key
deepseek_base_url = model_config.deepseek_base_url
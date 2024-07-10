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
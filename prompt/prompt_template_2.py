# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/8 9:44
@Auth ： leon
"""
import asyncio
from langchain_core.prompts import PromptTemplate
# 1. 以f-string格式渲染
# prompt_template = PromptTemplate.from_template("""
# 你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
# examples：
# question：美丽->beautiful;
# question：男孩->boy;
# question：男人->man；
# question：456->four hundred and fifty-six;
# question：1->one;
# question：34->thirty-four
# question：{user_input_chinese}
# """)
# 1.1. invoke传入字典
# prompt = prompt_template.invoke({"user_input_chinese":"你好"})
# print(prompt)
# 1.2. 传入单变量
# prompt = prompt_template.invoke("你好")
# print(prompt)
#1.3 调用format_prompt
# prompt= prompt_template.format_prompt(user_input_chinese="你好")
# print(prompt)
#1.4 调用format
# prompt= prompt_template.format(user_input_chinese="你好")
# print(prompt)
# 2. batch传入多变量
# prompt = prompt_template.batch([{"user_input_chinese":"你好"},{"user_input_chinese":"你是谁？"}])
# print(prompt)
# 3. stream流输出
# for i in prompt_template.stream("Jinja2 是一个功能更加强大的 Python 模板引擎，常用于 Web 开发，尤其是 Flask 和 Django 框架中。它支持复杂的控制结构，如循环和条件语句"):
#     print(i)

# async def main():
#     return await asyncio.gather(prompt_template.ainvoke({"user_input_chinese":"你好"}),prompt_template.ainvoke({"user_input_chinese":"我不好"}))
#
# res = asyncio.run(main())
# print(res)

# 4. 定义部分变量
# prompt_template = PromptTemplate.from_template("""
# 你是一个{language2language}翻译助手，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
# examples：
# question：beautiful->美丽;
# question：boy->男孩;
# question：man->男人；
# question：four hundred and fifty-six->456;
# question：one->1;
# question：thirty-four->34;
# question：{user_input_chinese}->
# """)
# lag2lag = input("你想我成为什么语言到什么语言的助手：")
# new_prompt_template = prompt_template.partial(language2language=lag2lag)
# print("助手初始化完毕，可以开始使用助手！！！")
#
# # 2. llm定义
# from langchain_community.llms import Tongyi
# from pydantic_settings import BaseSettings,SettingsConfigDict
#
# """
# 2,1 获取千问的key
# 我这么写的原因是因为方便我上传项目到github的同时，不暴露我的key，所以我把可以key保存到了最外部的一个.env文件中
# 这样我每一次同步到github的时候就不会把key也推出去，你们测试的时候，可以直接写成
# qwen_key="sk-cc2209cec48c4bc966fb4acda169e",这样省事。
# """
# class ModelConfig(BaseSettings):
#     model_config = SettingsConfigDict(env_file="../../.env",env_file_encoding="utf-8")
#     qwen_key:str
#     deepseek_key:str
#     deepseek_base_url:str
#
# model_config = ModelConfig()
# qwen_key = model_config.qwen_key
# # 1. 读取配置信息,获取模型key
# llm = Tongyi(dashscope_api_key=qwen_key)
#
#
# while(True):
#     user_input_word = input("请输入需要翻译的中文：")
#     if user_input_word.lower() =="quit":
#         break
#     else:
#         prompt = new_prompt_template.invoke({"user_input_chinese":user_input_word})
#         print(llm.invoke(prompt))

# 5. 保存prompt模板
# prompt_template = PromptTemplate.from_template("""
# 你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
# examples：
# question：美丽->beautiful;
# question：男孩->boy;
# question：男人->man；
# question：456->four hundred and fifty-six;
# question：1->one;
# question：34->thirty-four
# question：{user_input_chinese}
# """)
# prompt_template.save("./data/chinese2english.yml")

# 6. 从保存的文件中加载
prompt_template = PromptTemplate.from_file("./data/chinese2english.yml")
print(prompt_template)
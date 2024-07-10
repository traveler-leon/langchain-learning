# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/8 9:44
@Auth ： leon
"""
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
# 1.1. invoke传入字典
# prompt = prompt_template.invoke({"user_input_words":"你好"})
# print(prompt)
# 1.2. 传入单变量
# prompt = prompt_template.invoke("你好")
# print(prompt)
#1.3 调用format_prompt
# prompt= prompt_template.format_prompt(user_input_words="你好")
# print(prompt)
#1.4 调用format
# prompt= prompt_template.format(user_input_words="你好")
# print(prompt)
# 2. batch传入多变量
# prompt = prompt_template.batch([{"user_input_words":"你好"},{"user_input_words":"你是谁？"}])
# print(prompt)
# 3. stream流输出
# for i in prompt_template.stream({"user_input_words":"Jinja2 是一个功能更加强大的 Python 模板引擎，常用于 Web 开发，尤其是 Flask 和 Django 框架中。它支持复杂的控制结构，如循环和条件语句"}):
#     print(i)

async def main():
    return await asyncio.gather(prompt_template.ainvoke({"user_input_words":"你好"}),prompt_template.ainvoke({"user_input_words":"我不好"}))

res = asyncio.run(main())
print(res)

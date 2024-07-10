# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/8 9:44
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate
# 1. 以f-string格式渲染
# prompt_template = PromptTemplate.from_template("""
# 你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：
#
# ## history examples:
# question:美丽->answer:beautiful;
# question:男孩->answer:boy;
# question:男人->answer:man;
# question:456->answer:four hundred and fifty-six;
# question:1->answer:one;
# question:34->answer:thirty-four;
#
# ## user true task:
# question：{user_input_words}->answer：
# """)
# print(prompt_template.template)
# print(prompt_template.input_variables)
# print(prompt_template.template_format)
# print(prompt_template.input_types)
# print(prompt_template.partial_variables)
# 2. 以mustache格式渲染
# prompt_template = PromptTemplate.from_template("""
# 你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：
#
# ## history examples:
# question:美丽->answer:beautiful;
# question:男孩->answer:boy;
# question:男人->answer:man;
# question:456->answer:four hundred and fifty-six;
# question:1->answer:one;
# question:34->answer:thirty-four;
#
# ## user true task:
# question：{{user_input_words}}->answer：
# """,
# template_format="mustache")
# print(prompt_template.template)
# print(prompt_template.input_variables)
# print(prompt_template.template_format)
# print(prompt_template.input_types)
# print(prompt_template.partial_variables)
# 3. 以jinja2格式渲染
# prompt_template = PromptTemplate.from_template("""
# 你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：
#
# ## history examples:
# question:美丽->answer:beautiful;
# question:男孩->answer:boy;
# question:男人->answer:man;
# question:456->answer:four hundred and fifty-six;
# question:1->answer:one;
# question:34->answer:thirty-four;
#
# ## user true task:
# question：{{user_input_words}}->answer：
# """,
# template_format="jinja2")
# print(prompt_template.template)
# print(prompt_template.input_variables)
# print(prompt_template.template_format)
# print(prompt_template.input_types)
# print(prompt_template.partial_variables)

# 4. 直接实例化
prompt_template = PromptTemplate(template="""
你是一个翻译助手，你擅长将中文翻译为英文，请将我发送给你的question的内容翻译为英文，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：

## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;

## user true task:
question：{{user_input_words}}->answer：
""",
input_variables=['user_input_words'])
print(prompt_template.template)
print(prompt_template.input_variables)
print(prompt_template.template_format)
print(prompt_template.input_types)
print(prompt_template.partial_variables)
print(prompt_template.invoke({"user_input_chinese":"你好"}))

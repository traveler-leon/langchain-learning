# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/8 9:44
@Auth ： leon
"""
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
# print(prompt_template.template)
# print(prompt_template.input_variables)
# print(prompt_template.template_format)
# print(prompt_template.input_types)
# print(prompt_template.partial_variables)
# 2. 以mustache格式渲染
# prompt_template = PromptTemplate.from_template(template="""
# 你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
# examples：
# question：美丽->beautiful;
# question：男孩->boy;
# question：男人->man；
# question：456->four hundred and fifty-six;
# question：1->one;
# question：34->thirty-four
# question：{{user_input_chinese}}
# """,
# template_format="mustache")
# print(prompt_template.template)
# print(prompt_template.input_variables)
# print(prompt_template.template_format)
# print(prompt_template.input_types)
# print(prompt_template.partial_variables)
# 3. 以jinja2格式渲染
# prompt_template = PromptTemplate.from_template(template="""
# 你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
# examples：
# question：美丽->beautiful;
# question：男孩->boy;
# question：男人->man；
# question：456->four hundred and fifty-six;
# question：1->one;
# question：34->thirty-four
# question：{{user_input_chinese}}
# """,
# template_format="jinja2")
# print(prompt_template.template)
# print(prompt_template.input_variables)
# print(prompt_template.template_format)
# print(prompt_template.input_types)
# print(prompt_template.partial_variables)

# 4. 直接实例化
prompt_template = PromptTemplate(template="""
你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
examples：
question：美丽->beautiful;
question：男孩->boy;
question：男人->man；
question：456->four hundred and fifty-six;
question：1->one;
question：34->thirty-four
question：{user_input_chinese}
""",
input_variables=['user_input_chinese'])
print(prompt_template.template)
print(prompt_template.input_variables)
print(prompt_template.template_format)
print(prompt_template.input_types)
print(prompt_template.partial_variables)
print(prompt_template.invoke({"user_input_chinese":"你好"}))

# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/8 9:44
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate
# 5. 保存prompt模板
prompt_template_1 = PromptTemplate.from_template("""
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
""")
# prompt_template_1.save("./data/translate-lang2lang.json")

# 6. 从保存的文件中加载
prompt_template = PromptTemplate.from_file("data/translate-lang2lang.json")
print(prompt_template)
# lag2lag = input("你想我成为什么翻译助手(格式如：中文-英文)：")
# source_language,dst_language = lag2lag.split('-')
# new_prompt_template = prompt_template.partial(source_language=source_language,dst_language=dst_language)
# print(new_prompt_template)
# print(prompt_template)
# print(prompt_template_1.dict())
# print(prompt_template_1.InputType)
# print(prompt_template_1.OutputType)
# print(prompt_template_1.input_schema)
# print(prompt_template_1.output_schema)
# print(prompt_template_1.config_schema)
# prompt_template_3 = PromptTemplate.from_template("""这是第二个prompt模板:{user_input_words_3}""")
# new_prompt = prompt_template_1+"这是新的模板：{user_input_words_2}"+prompt_template_3
# print(new_prompt)
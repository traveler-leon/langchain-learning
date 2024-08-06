# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/9 11:10
@Auth ： leon
"""
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate


# print(HumanMessage(content="你好"))
# print(HumanMessage(content="你好",id='1234556hhhh',name="leon-message",additional_kwargs={"send_user":"leon"},response_metadata={"res_user":"openai"}))

# 本质上就是在HumanMessagePromptTemplate的prompt成员赋值一个PromptTemplate模板
prompt1 = SystemMessagePromptTemplate.from_template(template = """
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
""",
partial_variables={"source_language":"中文","dst_language":"英文"})
prompt_str = prompt1.format_messages(user_input_words="你是谁？")
prompt_str_2 = prompt1.format(user_input_words="你是谁？")
print(prompt_str,prompt1.input_variables)
print(prompt_str_2)


prompt2 = SystemMessagePromptTemplate.from_template(template = ["""
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：
""",
"""
## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;
""",
"""
## user true task:
question：{user_input_words}->answer：
"""])
prompt_str = prompt2.format_messages(user_input_words="你是谁？",source_language="中文",dst_language="英文")
prompt_str_2 = prompt2.format(user_input_words="你是谁？",source_language="中文",dst_language="英文")
print(prompt_str,prompt2.input_variables)
print(prompt_str_2)


prompt3 = SystemMessagePromptTemplate.from_template(template = [{"text":"""
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：
"""},
"""
## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;
""",
"""
## user true task:
question：{user_input_words}->answer：
"""])
prompt_str = prompt3.format_messages(user_input_words="你是谁？",source_language="中文",dst_language="英文")
prompt_str_2 = prompt3.format(user_input_words="你是谁？",source_language="中文",dst_language="英文")
print(prompt_str,prompt3.input_variables)
print(prompt_str_2)


prompt_1 = PromptTemplate.from_template("""
你是一个翻译助手，你擅长将{source_language}翻译为{dst_language}，请将我发送给你的question的内容翻译为{dst_language}，不要返回无关的内容，只需返回最终翻译结果，下面的history examples中提供了一些具体的案例，为你提供一些参考：
""")

prompt_2 = PromptTemplate.from_template("""
## history examples:
question:美丽->answer:beautiful;
question:男孩->answer:boy;
question:男人->answer:man;
question:456->answer:four hundred and fifty-six;
question:1->answer:one;
question:34->answer:thirty-four;
""")
prompt_3 = PromptTemplate.from_template("""
## user true task:
question：{user_input_words}->answer：
""")

prompt = SystemMessagePromptTemplate(prompt = [prompt_1,prompt_2,prompt_3])
prompt_str = prompt.format_messages(user_input_words="你是谁？",source_language="中文",dst_language="英文")
prompt_str_2 = prompt.format(user_input_words="你是谁？",source_language="中文",dst_language="英文")
print(prompt_str,prompt.input_variables)
print(prompt_str_2)
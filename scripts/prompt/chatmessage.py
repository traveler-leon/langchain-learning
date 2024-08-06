# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/9 11:10
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatMessagePromptTemplate


# 可定义任何角色
h1_prompt_template = ChatMessagePromptTemplate.from_template(
    role="管家",
    template="""
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
)
print(h1_prompt_template.format(user_input_words="你好", source_language="中文",dst_language="英文"))
print(h1_prompt_template.format_messages(user_input_words="你好",source_language="中文",dst_language="英文"))

# 可定义任何角色
h2_prompt_template = ChatMessagePromptTemplate.from_template(
    role="管家",
    template="""
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
    partial_variables={'source_language': "中文", 'dst_language': "英文"}
)
print(h2_prompt_template.format(user_input_words="你好"))
print(h2_prompt_template.format_messages(user_input_words="你好"))

h3_prompt_template = ChatMessagePromptTemplate(
    role="管家",
    prompt = PromptTemplate.from_template(template="""
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
partial_variables={'source_language': "中文", 'dst_language': "英文"})
)
print(h3_prompt_template.format(user_input_words="你好"))
print(h3_prompt_template.format_messages(user_input_words="你好"))
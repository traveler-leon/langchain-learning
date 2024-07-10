# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/9 13:52
@Auth ： leon
"""
from langchain_core.prompts import ChatPromptTemplate,HumanMessagePromptTemplate,ChatMessagePromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

# 1. 调用template的时候，默认只能渲染成为Humman prompt
h1_prompt_template = ChatPromptTemplate.from_template(
    template="请将下列内容翻译为中文:{input}"
)
# print(h1_prompt_template.format_prompt(input="你好"))
# print(h1_prompt_template.format(input="你好"))


h1_prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,："),
        HumanMessage(content="""
        question：美丽->beautiful;
        question：男孩->boy;
        question：男人->man；
        question：456->four hundred and fifty-six;
        question：1->one;
        question：34->thirty-four
        """),
        HumanMessagePromptTemplate.from_template(template="请将下列内容翻译为中文:{input}")
    ]
)
# print(h1_prompt_template.format_prompt(input="你好"))
# print(h1_prompt_template.format(input="你好"))
# print(h1_prompt_template.invoke({"input":"你好"}))


tmp_prompt_template = ChatPromptTemplate.from_messages(
    [
        ('user',"测试一下：{tmp_input}")
    ]
)

h2_prompt_template = ChatPromptTemplate.from_messages(
    [
        tmp_prompt_template,
        SystemMessage(content="你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例"),
        ('system',"翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,："),
        HumanMessage(content="question：美丽->beautiful;"),
        ('assistant','question：男孩->boy;'),
        ('ai','question：男人->man'),
        ('user','question：456->four hundred and fifty-six;'),
        ('human','question：1->one;'),
        'question：34->thirty-four',
        ChatMessagePromptTemplate.from_template(
            role="管家",
            template="请将下列内容翻译为中文:{input}"
        ),
        HumanMessagePromptTemplate.from_template(template="请将下列内容翻译为中文:{input}")
    ]
)
# print(h1_prompt_template.format_prompt(input="你好"))
# print(h1_prompt_template.format(input="你好"))
# print(h2_prompt_template.invoke({"input":"你好",'tmp_input':"测试"}).to_string())


h3_prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例"),
        MessagesPlaceholder(variable_name="chat_content",optional=True,n_messages=2),
        HumanMessagePromptTemplate.from_template(template="请将下列内容翻译为中文:{input}")
    ]
)
insert_template = [
    HumanMessage(content="question：美丽->beautiful;"),
    ('assistant', 'question：男孩->boy;'),
    ('ai', 'question：男人->man'),
    ('user', 'question：456->four hundred and fifty-six;'),
    ('human', 'question：1->one;'),
    'question：34->thirty-four',
    # 暂时不支持ChatMessagePromptTemplate
    # ChatMessagePromptTemplate.from_template(
    #     role="管家",
    #     template="请将下列内容翻译为中文:{input}"
    # )
]
# print(h1_prompt_template.format_prompt(input="你好"))
# print(h1_prompt_template.format(input="你好"))
print(h3_prompt_template.invoke({"input":"你好",'chat_content':insert_template,'tmp_input':"测试"}).to_string())
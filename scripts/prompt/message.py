# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/9 11:10
@Auth ： leon
"""
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage,FunctionMessage,ToolMessage

print(HumanMessage(content="你好"))
print(SystemMessage(content="我不好"))
print(AIMessage("大家好"))
print(FunctionMessage(name="hello",content="你好"))
print(ToolMessage(tool_call_id="1",content="我也挺好的"))

from langchain_core.prompts import HumanMessagePromptTemplate,AIMessagePromptTemplate,SystemMessagePromptTemplate,ChatMessagePromptTemplate

h_prompt_template = HumanMessagePromptTemplate.from_template(
    template="请将下列内容翻译为中文:{input}"
)
print(h_prompt_template.format(input="你好"))
print(h_prompt_template.format_messages(input="你好"))

h1_prompt_template = HumanMessagePromptTemplate.from_template(
    template=["请将下列内容翻译为中文:{input}","请将下列内容翻译为英文:{input}"]
)
print(h1_prompt_template.format(input="你好"))
print(h1_prompt_template.format_messages(input="你好"))

h2_prompt_template = HumanMessagePromptTemplate.from_template(
    template=["请将下列内容翻译为中文:{input_1}","请将下列内容翻译为英文:{input_2}"]
)
print(h2_prompt_template.format(input_1="你好",input_2="挺好"))
print(h2_prompt_template.format_messages(input_1="你好",input_2="挺好"))

h3_prompt_template = HumanMessagePromptTemplate.from_template(
    template=[{'text':"请将下列内容翻译为中文:{input_1}"},{"text":"请将下列内容翻译为英文:{input_2}"}]
)
print(h3_prompt_template.format(input_1="你好",input_2="挺好"))
print(h3_prompt_template.format_messages(input_1="你好",input_2="挺好"))

# 可定义任何角色
h5_prompt_template = ChatMessagePromptTemplate.from_template(
    role="管家",
    template="请将下列内容翻译为中文:{input}"
)
print(h5_prompt_template.format(input="你好"))
print(h5_prompt_template.format_messages(input="你好"))
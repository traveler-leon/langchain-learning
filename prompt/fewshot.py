# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/9 9:44
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
example_prompt = PromptTemplate.from_template("question: {question}")
examples = [
    {'question':'美丽->beautiful'},
    {'question':'男孩->boy'},
    {'question':'男人->man'},
    {'question':'456->four'},
    {'question':'456->four hundred and fifty-six'},
    {'question':'1->one'},
    {'question':'34->thirty - four'}
]

prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="你是一个{lag2lag}文翻译助手，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,",
    suffix="true question:{input}",
    input_variables=['input','lag2lag']
)

new_prompt_template = prompt_template.partial(lag2lag="中德")

prompt = new_prompt_template.invoke({'input':"你好"})
print(prompt.to_string())

#支持保存，但是不支持加载
prompt_template.save('./data/fewshot.json')
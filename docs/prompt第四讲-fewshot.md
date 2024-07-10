## 前提回顾
前面已经用PromptTemplate实现了一个prompt模板了，里面有说明、案例、和实际的问题
```python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/8 9:44
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate
# 1. prompt模板定义
prompt_template = PromptTemplate.from_template("""
你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
examples：
question：美丽->beautiful;
question：男孩->boy;
question：男人->man；
question：456->four hundred and fifty-six;
question：1->one;
question：34->thirty-four
question：{user_input_chinese}
""")

```
## FewShotPromptTemplate
下面我们换一种更加优雅的方式来实现上面的prompt模板
```python
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
```
**参数讲解**
1. example_prompt：你想要案例遵守的格式
2. examples一个案例列表，里面是多个字典，字典的key必须和example_prompt中定义的变量是统一的
3. prefix：你想要在案例前面插入的内容，通常就是这个助手的能力说明
4. suffix:通常就是你想要最后插入的实际的问题的格式
5. input_variables：变量说明，这个变量来自prefix和suffix
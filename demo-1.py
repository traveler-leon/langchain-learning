from langchain.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}"
)
res = prompt_template.format(adjective="funny",content="chickens")
res2 = prompt_template.format_prompt(adjective="funny",content="chickens")
print(res,res2)
print(type(res),type(res2))
print(prompt_template.InputType,prompt_template.OutputType)
print(prompt_template.input_schema,prompt_template.output_schema)
print(prompt_template.get_input_schema())
print(prompt_template.get_graph())
print(prompt_template.get_prompts())
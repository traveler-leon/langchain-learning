from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}"
)
res = prompt_template.format(adjective="funny",content="chickens")
print(res)

print("test")
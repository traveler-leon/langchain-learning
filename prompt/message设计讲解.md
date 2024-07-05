# 前提概要
在langchain中定义了两种模型，一种是llm，它直接调用原生大模型，另一种是chat model，而chat model是在llm的基础上
做了一点封装，本质上还是调用了llm。在chat model的使用中，输入到其中的内容就是message

下面就讲讲message的原生支持
# message支持
## BaseMessage
#### 变量支持
1. content:具体的信息内容
2. additional_kwargs:
3. response_metadata:
4. type:
5. name:
6. id:
#### 方法支持
1. __add__

## HumanMessage
#### 变量支持
type: Literal["human"] = "human"      
本质上只是限制了身份而已
## SystemMessage
#### 变量支持
type: Literal["human"] = "system"
本质上只是限制了身份而已
## AIMessage
#### 变量支持
1. type: Literal["human"] = "ai"
2. tool_calls:工具调用
3. invalid_tool_calls：调用错误的工具信息
4. usage_metadata：message的元数据

#### 方法支持
1. 初始化验证

## ToolMessage
#### 变量支持
1. type: Literal["human"] = "tool"
2. tool_call_id:工具调用
## FunctionMessage
#### 变量支持
1. type: Literal["human"] = "function"
2. name:
## ChatMessage
#### 变量支持
1. type: Literal["human"] = "chat"
2. role:

# message模板支持
## BaseMessagePromptTemplate
#### 变量支持
... ....   
#### 方法支持
1. __add__        
   1.1. 将自身转为ChatPromptTemplate，然后和另一个相加
2. input_variables（子类实现）
3. format_messages子类实现

## _StringImageMessagePromptTemplate
#### 变量支持
1. prompt : Union[StringPromptTemplate, List[Union[StringPromptTemplate, ImagePromptTemplate]]   
2. additional_kwargs: dict = Field(default_factory=dict)
3. _msg_class: Type[BaseMessage]
#### 方法支持
1. from_template
   1.1. 本质上是调用PromptTemplate.from_template，将传入的单个字符串或者是字符串列表转为一个prompt template或者是一系列prompt template存入到prompt这个列表中

2. from_template_file        
   2.1 打开文件，调用from_template
3. format_messages子         
   3.1. 调用format生成一系列的message
4. format      
   4.1 如果self.prompt的是一个单独的StringPromptTemplate，则直接调用prompt的format得到一个格式化后的prompt value
   4.2 如果self.prompt是一个列表，则循环格式化
      4.2.1. 从输入的参数中取出input_variables的数据
      4.2.2. 判断prompt列表中的每一个prompt，如果是StringPromptTemplate，则调用它的format函数生成prompt template，然后保存到formatted变量，最后构建一个字典{"type": "text", "text": formatted},存入list
      4.2.3. 根据初始化后的list用来构建一个message

## _HumanMessagePromptTemplate
#### 变量支持
_msg_class: Type[BaseMessage] = HumanMessage
## _AIMessagePromptTemplate
#### 变量支持
_msg_class: Type[BaseMessage] = AIMessage
## _SystemMessagePromptTemplate
#### 变量支持
_msg_class: Type[BaseMessage] = SystemMessage


对于一个message来说，大致应该包括的内容如下：
1. （content）发送的实际需要交互的内容：这一般是我们想问的问题
2. （type）message的类型：比如ai、humman、system或者是自定义的类型
3. （name）message的名字：方便用户查看
4. （id）message的id：messge的唯一身份标识
5. （additional_kwargs）发送者的一些附加信息
6. （response_metadata）回复着的一些信息

## HumanMessage
将基础message的类型(type)变为"human"

## SystemMessage
将基础message的类型(type)变为"system"
## ToolMessage
1. 将基础message的类型(type)变为"tool"
2. 新增tool_call_id：用来表示tool的id身份
## FunctionMessage
1. 将基础message的类型(type)变为"function"
2. 新增name：用来表示要调用的函数的名字
## ChatMessage
1. 将基础message的类型(type)变为"chat"
2. 新增role：用来表示messge属于哪一个角色发出

## AIMessage
1. 将基础message的类型(type)变为"ai"
2. 新增tool_calls：调用成功的工具合集
   3. name：工具的名字
   4. args：工具的参数
   5. id：工具的id身份
3. 新增invalid_tool_calls：调用失败的工具合集
   4. name: 工具的名字
   5. args: 工具的参数
   6. id: 工具的id身份
   7. error: 错误信息
4. 新增usage_metadata：token使用统计信息
   5. input_tokens: 输入的token数量
   6. output_tokens: 输出的token数量
   7. total_tokens: 总的token数量

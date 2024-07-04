## prompt模板
开篇我介绍了在llm中，通常输入的那个字符串会被我们称之为prompt，下面就是一个中英文翻译助手的prompt例子
```shell
你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
examples：
question：美丽->beautiful;
question：男孩->boy;
question：男人->man；
question：456->four hundred and fifty-six;
question：1->one;
question：34->thirty-four
question：123
```
也就是说不管怎样，你最终给模型一定是上面这一大串东西，你如果要翻译“扑街”,只是把最底部的question替换掉
```shell
你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
examples：
question：美丽->beautiful;
question：男孩->boy;
question：男人->man；
question：456->four hundred and fifty-six;
question：1->one;
question：34->thirty-four
question：扑街
```
但是如果你真的要开发一个中英文翻译助手给用户使用的时候，不可能让用户完整从写这一大堆的东西吧，我们希望的是用户只输入他想要翻译的中文，我们在后台把他输入的内容
根据设定的模板填入，最终将填充后的内容发送给llm
```shell
你是一个中英文翻译助手，你需要把我发给你的question翻译为英文，下面的examples是一些具体翻译的案例，翻译的时候请参考案例来翻译，注意只输出最终翻译的结果,：
examples：
question：美丽->beautiful;
question：男孩->boy;
question：男人->man；
question：456->four hundred and fifty-six;
question：1->one;
question：34->thirty-four
question：{user_input_chinese}
```
用户没输入时，我们定义好的这个模板，就叫做prompt模板（prompt template）,当用户输入内容后这个内容会替换掉模板中的user_input_chinese，替换后的完整内容就是一个
prompt。

**总结**：prompt template就是具有一定变量的字符串，这些变量是运行时用户输入的。用户输入后构成的完整字符串才被叫做prompt

## BasePromptTemplate
而在langchain中，提供了定义prompt template的能力，而prompt template接受用户内容后生产出来的内容叫做prompt value，这里的prompt value和llm需要的prompt还有点
区别，之所以有区别，是因为在langchain设计了两种模型大类，一种是llm，另一种是chatmodel，llm是输入是接收字符串的，这也就是我前面说的prompt了，而chatmodel接受的是message
的，所以二者所需要的数据格式是不一样的。所以为了兼容这两种模型大类，langchian的prompt template生产出的内容是prompt value，而prompt value好处就是既可以转为llm需要是
字符串形式，也可以转为chatmodel需要的message形式，这就很方便了。

**注：上面虽然说chatmodel需要的是message类型的数据，但是底层chatmodel调用的也是llm，自然输入的内容最终也是会转成字符串的，这么设计的原因更多的是减小用户理解的难度**


下面就讲讲langchain对于prompt  template的底层支持，底层是由BasePromptTemplate
###  BasePromptTemplate能力
BasePromptTemplate提供了一些基础能力的支持
	1. 变量保存
	2. 变量类型
	3. 输出解析
	4. 局部变量
	5. metadata
	6. tags
	
1. 校验输入变量
	1.1.输入变量不是一个字典，且只有一个的话，就会将input_variables中保存的变量名拿出来，组成一个字典   
	1.2 如果传入的是一个字典，如果字典和保存在input_variables中有差异，则报错。   
	1.3 返回校验后的输入字典   
	
2. 模板实例化
    2.1 校验config   
	2.2 校验输入变量    
	2.3 格式化模板（交给子类）   
	
3. 局部变量化
	2.1 将局部变量从input_variables提出，更新input_variables    
	
4. 转为dict
5. 保存到本地（只支持json 和yaml ）    

## 思考
在这个底层类中
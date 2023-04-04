**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**codeString：** *string*型，必填

　　用于传入*需要进行渲染的代码内容字符串*

**language：** *string*型，必填

　　用于设置*代码内容对应的语言*，如`'python'`

**codeTheme：** *string*型，默认为`'gh-colors'`

　　用于*设置代码样式主题*，具体使用参考[切换代码主题](/change-code-theme)

**codeBlockStyle：** *dict*型

　　用于为*代码内容中的代码块容器补充自定义css样式*，具体使用参考[自定义代码块样式](/custom-code-block-style)

**codeStyle：** *dict*型

　　用于为*代码内容中的代码块文字补充自定义css样式*，具体使用参考[自定义代码块样式](/custom-code-block-style)

**showLineNumbers：** *bool*型，默认为`True`

　　用于设置*代码块是否显示行号*

**showCopyButton：** *bool*型，默认为`True`

　　用于设置*是否渲染代码块右上角复制按钮*

**wrapLongLines：** *bool*型，默认为`False`

　　用于设置*是否针对代码块中的超长内容行自动换行显示*

**addedLineNumbers：** `list[int]`型，默认为`[]`

　　用于设置*需要施加新增效果的代码行下标列表*

**removedLineNumbers：** `list[int]`型，默认为`[]`

　　用于设置*需要施加移除效果的代码行下标列表*

**addedLineStyle：** *dict*型

　　用于设置*新增效果代码行css样式*

**removedLineStyle：** *dict*型

　　用于设置*移除效果代码行css样式*
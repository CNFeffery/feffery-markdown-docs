**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*整体容器的css样式*

**className：** *string*型

　　用于设置*整体容器的css类名*

**locale：** *string*型，默认为`'zh-cn'`

　　用于配置*部分文案信息国际化*，可选的有`'zh-cn'`、`'en-us'`

**markdownStr：** *string*型

　　用于传入*需要进行渲染的markdown内容字符串*

**codeTheme：** *string*型，默认为`'gh-colors'`

　　用于为*markdown内容中的代码块设置代码样式主题*，具体使用参考[切换代码主题](/change-code-theme)

**renderHtml：** *bool*型，默认为`False`

　　用于设置*是否解析渲染markdown内容中的原生HTML内容*，具体使用参考[渲染原生HTML](/render-raw-html)

**linkTarget：** *string*型，默认为`'_blank'`

　　用于为*markdown内容中的链接设置点击跳转方式*，具体使用参考[改变链接打开方式](/change-link-target)

**codeBlockStyle：** *dict*型

　　用于为*markdown内容中的代码块容器补充自定义css样式*，具体使用参考[自定义代码块样式](/custom-code-block-style)

**codeStyle：** *dict*型

　　用于为*markdown内容中的代码块文字补充自定义css样式*，具体使用参考[自定义代码块样式](/custom-code-block-style)

**showLineNumbers：** *bool*型，默认为`True`

　　用于设置*代码块是否显示行号*

**showCopyButton：** *bool*型，默认为`True`

　　用于设置*是否渲染代码块右上角复制按钮*

**imagePreview：** *bool*型，默认为`False`

　　用于设置*是否以交互预览方式渲染图片内容*

**imageFallback：** *string*型

　　用于设置*图片加载失败后的占位图资源链接*

**imageForceAlignCenter：** *bool*型，默认为`False`

　　用于设置*是否强制所有图片居中显示*

**imageWidth：** *int*或*string*型

　　用于*为所有图片设置统一的宽度值*

**imageHeight：** *int*或*string*型

　　用于*为所有图片设置统一的高度值*

**forceTableAlignCenter：** *bool*型，默认为`True`

　　用于设置*是否强制所有表格居中*

**forceTableHeaderTextAlignCenter：** *bool*型，默认为`True`

　　用于设置*是否强制所有表格标题单元格文字居中*

**forceTableContentTextAlignCenter：** *bool*型，默认为`True`

　　用于设置*是否强制所有表格内容单元格文字居中*

**h1Style：** *dict*型

　　用于*为一级标题元素设置css样式*

**h1ClassName：** *str*型

　　用于*为一级标题元素设置css类*

**h2Style：** *dict*型

　　用于*为二级标题元素设置css样式*

**h2ClassName：** *str*型

　　用于*为二级标题元素设置css类*

**h3Style：** *dict*型

　　用于*为三级标题元素设置css样式*

**h3ClassName：** *str*型

　　用于*为三级标题元素设置css类*

**h4Style：** *dict*型

　　用于*为四级标题元素设置css样式*

**h4ClassName：** *str*型

　　用于*为四级标题元素设置css类*

**h5Style：** *dict*型

　　用于*为五级标题元素设置css样式*

**h5ClassName：** *str*型

　　用于*为五级标题元素设置css类*

**h6Style：** *dict*型

　　用于*为六级标题元素设置css样式*

**h6ClassName：** *str*型

　　用于*为六级标题元素设置css类*

**tableStyle：** *dict*型

　　用于*为表格元素设置css样式*

**tableClassName：** *str*型

　　用于*为表格元素设置css类*

**theadStyle：** *dict*型

　　用于*为表格表头元素设置css样式*

**theadClassName：** *str*型

　　用于*为表格表头元素设置css类*

**trStyle：** *dict*型

　　用于*为表格数据行元素设置css样式*

**trClassName：** *str*型

　　用于*为表格数据行元素设置css类*

**thStyle：** *dict*型

　　用于*为表格表头单元格元素设置css样式*

**thClassName：** *str*型

　　用于*为表格表头单元格元素设置css类*

**tdStyle：** *dict*型

　　用于*为表格内容单元格元素设置css样式*

**tdClassName：** *str*型

　　用于*为表格内容单元格元素设置css类*

**aStyle：** *dict*型

　　用于*为超链接元素设置css样式*

**aClassName：** *str*型

　　用于*为超链接元素设置css类*

**blockquoteStyle：** *dict*型

　　用于*为引用块元素设置css样式*

**blockquoteClassName：** *str*型

　　用于*为引用块元素设置css类*

**inlineCodeStyle：** *dict*型

　　用于*为行内代码元素设置css样式*

**inlineCodeClassName：** *str*型

　　用于*为行内代码元素设置css类*

**hrStyle：** *dict*型

　　用于*为水平分割线元素设置css样式*

**hrClassName：** *str*型

　　用于*为水平分割线元素设置css类*

**strongStyle：** *dict*型

　　用于*为加粗内容元素设置css样式*

**strongClassName：** *str*型

　　用于*为加粗内容元素设置css类*

**checkExternalLink：** *bool*型，默认为`False`

　　用于设置*是否开启链接安全跳转功能*，需配合参数`safeRedirectUrlPrefix`使用

**externalLinkPrefixWhiteList：** `list[string]`型

　　用于设置*外部链接前缀白名单列表*，当`checkExternalLink=True`且`safeRedirectUrlPrefix`有定义时，以`externalLinkPrefixWhiteList`中的某个元素为前缀的外部网址将不会进行安全跳转

**safeRedirectUrlPrefix：** *string*型

　　用于设置*自定义的安全链接跳转服务接口网址前缀*，譬如针对外部链接`https://www.baidu.com/`，若有安全链接跳转服务`/safe-redirect?target=外部链接`，则设置`safeRedirectUrlPrefix="/safe-redirect?target="`即可

**markdownBaseClassName：** *string*型，默认为`'markdown-body'`

　　用于设置*拓展主题对应的类名*，具体使用参考[使用拓展主题](/use-external-theme)

**titleAsId：** *bool*型，默认为`False`

　　用于设置*是否在渲染标题时，将每个标题的内容视作id信息添加到元素上*

**facAnchorLinkDict：** *只读属性*

　　 当设置`titleAsId=True`后，若文档中有合法的标题，可以通过回调函数，将此属性作为`fac.AntdAnchor()`中的`linkDict`参数使用，从而实现自动生成交互目录

**wrapLongLines：** *bool*型，默认为`False`

　　用于设置*是否针对代码块中的超长内容行自动换行显示*

**codeFallbackLanguage：** *string*型

　　针对`markdownStr`中存在语言类型缺失的代码块，用于设置*强制回滚的语言类型*
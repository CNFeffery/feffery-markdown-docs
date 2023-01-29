from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

from views import side_props

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.6
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '更多用法'
                        },
                        {
                            'title': '自定义代码块样式'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('中通过参数'),
                        fac.AntdText('codeBlockStyle', code=True),
                        fac.AntdText('和'),
                        fac.AntdText('codeStyle', code=True),
                        fac.AntdText('可以分别改变代码块容器及代码文字内容的css样式，参考下面的示例：')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            '限制代码块最大高度从而触发滚动条显示',
                            innerTextOrientation='left'
                        ),
                        fmc.FefferyMarkdown(
                            codeBlockStyle={
                                'maxHeight': '300px'
                            },
                            markdownStr="""
```python
import dash
from dash import html
import feffery_markdown_components as fmc

app = dash.Dash(__name__)

raw_markdown = '''
### 1 标题

在文字写书写不同数量的`#`可以完成不同的标题，如下：

# 一级标题

## 二级标题

### 三级标题

### 2 无序列表

无序列表的使用，在符号`-`后加空格使用。如下：

- 无序列表 1
- 无序列表 2
- 无序列表 3

如果要控制列表的层级，则需要在符号`-`前使用空格。如下：

- 无序列表 1
- 无序列表 2
  - 无序列表 2.1
  - 无序列表 2.2

### 3 有序列表

有序列表的使用，在数字及符号`.`后加空格后输入内容，如下：

1. 有序列表 1
2. 有序列表 2
3. 有序列表 3
'''

app.layout = html.Div(
	[
        fmc.FefferyMarrkdown(
        	markdownStr=raw_markdown
        )
    ]
)

if __name__ == '__main__':
    app.run()
```
"""
                        ),

                        fac.AntdDivider(
                            '改变代码内容字体大小',
                            innerTextOrientation='left'
                        ),

                        fmc.FefferyMarkdown(
                            codeStyle={
                                'fontSize': '20px'
                            },
                            markdownStr='''
```python
import dash
from dash import html
import feffery_markdown_components as fmc
```
'''
                        ),

                        fac.AntdDivider(
                            '对代码块css样式进行自定义',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fac.AntdDivider(
    '限制代码块最大高度从而触发滚动条显示',
    innerTextOrientation='left'
),
fmc.FefferyMarkdown(
    codeBlockStyle={
        'maxHeight': '300px'
    },
    markdownStr=\"\"\"
```python
import dash
from dash import html
import feffery_markdown_components as fmc

app = dash.Dash(__name__)

raw_markdown = '''
### 1 标题

在文字写书写不同数量的`#`可以完成不同的标题，如下：

# 一级标题

## 二级标题

### 三级标题

### 2 无序列表

无序列表的使用，在符号`-`后加空格使用。如下：

- 无序列表 1
- 无序列表 2
- 无序列表 3

如果要控制列表的层级，则需要在符号`-`前使用空格。如下：

- 无序列表 1
- 无序列表 2
- 无序列表 2.1
- 无序列表 2.2

### 3 有序列表

有序列表的使用，在数字及符号`.`后加空格后输入内容，如下：

1. 有序列表 1
2. 有序列表 2
3. 有序列表 3
'''

app.layout = html.Div(
[
fmc.FefferyMarrkdown(
markdownStr=raw_markdown
)
]
)

if __name__ == '__main__':
app.run()
```
\"\"\"
),

fac.AntdDivider(
    '改变代码内容字体大小',
    innerTextOrientation='left'
),

fmc.FefferyMarkdown(
    codeStyle={
        'fontSize': '20px'
    },
    markdownStr='''
```python
import dash
from dash import html
import feffery_markdown_components as fmc
```
'''
)                                
"""
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='对代码块css样式进行自定义',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '对代码块css样式进行自定义', 'href': '#对代码块css样式进行自定义'}
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '25px'
            }
        ),

        # 侧边参数栏
        side_props.side_props_layout
    ],
    style={
        'display': 'flex'
    }
)

import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider(
            '限制代码块最大高度从而触发滚动条显示', innerTextOrientation='left'
        ),
        fmc.FefferyMarkdown(
            codeBlockStyle={'maxHeight': '300px'},
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
""",
        ),
        fac.AntdDivider('改变代码内容字体大小', innerTextOrientation='left'),
        fmc.FefferyMarkdown(
            codeStyle={'fontSize': '20px'},
            markdownStr="""
```python
import dash
from dash import html
import feffery_markdown_components as fmc
```
""",
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fac.AntdDivider(
        '限制代码块最大高度从而触发滚动条显示', innerTextOrientation='left'
    ),
    fmc.FefferyMarkdown(
        codeBlockStyle={'maxHeight': '300px'},
        markdownStr="""
```python
import dash
from dash import html
import feffery_markdown_components as fmc

app = dash.Dash(__name__)

raw_markdown = \'\'\'
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
\'\'\'

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
""",
    ),
    fac.AntdDivider('改变代码内容字体大小', innerTextOrientation='left'),
    fmc.FefferyMarkdown(
        codeStyle={'fontSize': '20px'},
        markdownStr="""
```python
import dash
from dash import html
import feffery_markdown_components as fmc
```
""",
    ),
]
'''
        }
    ]

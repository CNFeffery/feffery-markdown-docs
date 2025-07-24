import dash
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        html.Div(id='toc-anchor-demo'),
        fmc.FefferyMarkdown(
            id='markdown-auto-toc-demo',
            titleAsId=True,
            renderHtml=True,
            markdownStr="""
# 1 标题测试
## 1.1 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

### 1.1.1 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

### 1.1.2 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

## 1.2 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

# 2 标题测试
## 2.1 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

### 2.1.1 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

### 2.1.2 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

## 2.2 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>
""",
        ),
    ]

    return demo_contents


@app.callback(
    Output('toc-anchor-demo', 'children'),
    Input('markdown-auto-toc-demo', 'facAnchorLinkDict'),
)
def auto_toc_demo(facAnchorLinkDict):
    if facAnchorLinkDict:
        return fac.AntdAnchor(linkDict=facAnchorLinkDict)

    return dash.no_update


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    html.Div(id='toc-anchor-demo'),
    fmc.FefferyMarkdown(
        id='markdown-auto-toc-demo',
        titleAsId=True,
        renderHtml=True,
        markdownStr="""
# 1 标题测试
## 1.1 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

### 1.1.1 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

### 1.1.2 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

## 1.2 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

# 2 标题测试
## 2.1 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

### 2.1.1 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

### 2.1.2 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>

## 2.2 标题测试

a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>
""",
    ),
]

...

@app.callback(
    Output('toc-anchor-demo', 'children'),
    Input('markdown-auto-toc-demo', 'facAnchorLinkDict'),
)
def auto_toc_demo(facAnchorLinkDict):
    if facAnchorLinkDict:
        return fac.AntdAnchor(linkDict=facAnchorLinkDict)

    return dash.no_update
'''
        }
    ]

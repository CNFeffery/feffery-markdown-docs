import dash
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
from dash.dependencies import Input, Output

from server import app
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
                            'title': '自动生成目录'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('在设置参数'),
                        fac.AntdText('titleAsId=True', code=True),
                        fac.AntdText(
                            '时，会在渲染后为文档中的所有标题元素添加与其内容一致的id信息，同时会产生出属性值'),
                        fac.AntdText('facAnchorLinkDict', code=True),
                        fac.AntdText('，可利用回调函数直接作为'),
                        fac.AntdText('fac', strong=True),
                        fac.AntdText('中锚点组件'),
                        fac.AntdText('AntdAnchor'),
                        fac.AntdText('的参数'),
                        fac.AntdText('linkDict', code=True),
                        fac.AntdText('，从而实现自动目录生成')
                    ]
                ),

                html.Div(
                    [
                        html.Div(id='toc-anchor-demo'),
                        fmc.FefferyMarkdown(
                            id='markdown-auto-toc-demo',
                            titleAsId=True,
                            renderHtml=True,
                            markdownStr='''

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

'''
                        ),

                        fac.AntdDivider(
                            '配合fac实现自动目录生成',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""

html.Div(id='toc-anchor-demo'),
fmc.FefferyMarkdown(
    id='markdown-auto-toc-demo',
    titleAsId=True,
    renderHtml=True,
    markdownStr='''

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

'''
)

...

@app.callback(
    Output('toc-anchor-demo', 'children'),
    Input('markdown-auto-toc-demo', 'facAnchorLinkDict')
)
def auto_toc_demo(facAnchorLinkDict):

    if facAnchorLinkDict:
        return fac.AntdAnchor(
            linkDict=facAnchorLinkDict
        )

    return dash.no_update

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
                    id='配合fac实现自动目录生成',
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
                    {'title': '配合fac实现自动目录生成', 'href': '#配合fac实现自动目录生成'}
                ],
                offsetTop=0
            ),
            id='anchor-container-demo',
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


@app.callback(
    Output('toc-anchor-demo', 'children'),
    Input('markdown-auto-toc-demo', 'facAnchorLinkDict')
)
def auto_toc_demo(facAnchorLinkDict):

    if facAnchorLinkDict:
        return fac.AntdAnchor(
            linkDict=facAnchorLinkDict
        )

    return dash.no_update

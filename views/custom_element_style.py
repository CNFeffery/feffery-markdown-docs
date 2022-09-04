from dash import html
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
import feffery_antd_components as fac

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
                            'title': '自定义各元素样式'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('中支持对渲染结果中主要的一些网页元素单独统一设置css样式或类，以自定义标题样式为例：')
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            h1Style={
                                'backgroundImage': 'linear-gradient(to right, orange, purple)',
                                'color': 'transparent',
                                'display': 'inline-table',
                                '-webkit-background-clip': 'text'
                            },
                            h2Style={
                                'borderBottom': '3px solid #1890ff',
                                'fontFamily': 'KaiTi',
                                'textAlign': 'center',
                                'margin': '0 auto',
                                'display': 'table'
                            },
                            h3Style={
                                'color': 'transparent',
                                '-webkit-text-stroke': '1px black',
                                'letterSpacing': '0.04em'
                            },
                            markdownStr=r'''
# 一级标题

## 二级标题

### 三级标题
'''
                        ),

                        fac.AntdDivider(
                            '以标题样式自定义为例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fmc.FefferyMarkdown(
    h1Style={
        'backgroundImage': 'linear-gradient(to right, orange, purple)',
        'color': 'transparent',
        'display': 'inline-table',
        '-webkit-background-clip': 'text'
    },
    h2Style={
        'borderBottom': '3px solid #1890ff',
        'fontFamily': 'KaiTi',
        'textAlign': 'center',
        'margin': '0 auto',
        'display': 'table'
    },
    h3Style={
        'color': 'transparent',
        '-webkit-text-stroke': '1px black',
        'letterSpacing': '0.04em'
    },
    markdownStr=r'''
# 一级标题

## 二级标题

### 三级标题
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
                    id='以标题样式自定义为例',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '以标题样式自定义为例', 'href': '#以标题样式自定义为例'}
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'margin': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)

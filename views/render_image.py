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
                            'title': '渲染图片内容'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('中渲染图片的方式与常规markdown语法相同，且在设置参数'),
                        fac.AntdText('renderHtml=True', code=True),
                        fac.AntdText('之后，还可以书写原生HTML代码来渲染图片：')
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            renderHtml=True,
                            codeStyle={
                                'fontSize': '20px'
                            },
                            markdownStr='''
- 基于markdown语法渲染图片

![image](/assets/imgs/fmc-logo.svg)

- 基于原生HTML渲染图片

<div style="text-align: center;">
    <img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />
</ div>

'''
                        ),

                        fac.AntdDivider(
                            '基于链接渲染图片',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fmc.FefferyMarkdown(
    renderHtml=True,
    codeStyle={
        'fontSize': '20px'
    },
    markdownStr='''
- 基于markdown语法渲染图片

![image](/assets/imgs/fmc-logo.svg)

- 基于原生HTML渲染图片

<div style="text-align: center;">
<img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />
</ div>

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
                    id='基于链接渲染图片',
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
                    {'title': '基于链接渲染图片', 'href': '#基于链接渲染图片'}
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

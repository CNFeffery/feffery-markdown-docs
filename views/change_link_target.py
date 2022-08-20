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
                            'title': '改变链接打开方式'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('针对内容中的链接，可以设置链接打开方式，设置参数'),
                        fac.AntdText('linkTarget', code=True),
                        fac.AntdText('即可，参考下面的示例：')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            '默认linkTarget="_blank"',
                            innerTextOrientation='left'
                        ),
                        fmc.FefferyMarkdown(
                            markdownStr='''[fac官网](http://fac.feffery.tech/)'''
                        ),

                        fac.AntdDivider(
                            'linkTarget="_self"',
                            innerTextOrientation='left'
                        ),
                        fmc.FefferyMarkdown(
                            linkTarget='_self',
                            markdownStr='''[fac官网](http://fac.feffery.tech/)'''
                        ),

                        fac.AntdDivider(
                            '处理markdown内容中链接的打开方式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fac.AntdDivider(
    '默认linkTarget="_blank"',
    innerTextOrientation='left'
),
fmc.FefferyMarkdown(
    markdownStr='''[fac官网](http://fac.feffery.tech/)'''
),

fac.AntdDivider(
    'linkTarget="_self"',
    innerTextOrientation='left'
),
fmc.FefferyMarkdown(
    linkTarget='_self',
    markdownStr='''[fac官网](http://fac.feffery.tech/)'''
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
                    id='处理markdown内容中链接的打开方式',
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
                    {'title': '处理markdown内容中链接的打开方式',
                        'href': '#处理markdown内容中链接的打开方式'}
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

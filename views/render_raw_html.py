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
                            'title': '渲染原生HTML'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('中默认不开启原生HTML渲染，如果需要开启，设置参数'),
                        fac.AntdText('renderHtml=True', code=True),
                        fac.AntdText('即可，参考下面的示例：')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            '默认不开启',
                            innerTextOrientation='left'
                        ),
                        fmc.FefferyMarkdown(
                            markdownStr='''
<span style="display:block;text-align:right;color:orangered;">橙色居右</span>
<span style="display:block;text-align:center;color:orangered;">橙色居中</span>

'''
                        ),

                        fac.AntdDivider(
                            '开启后',
                            innerTextOrientation='left'
                        ),
                        fmc.FefferyMarkdown(
                            renderHtml=True,
                            markdownStr='''
<span style="display:block;text-align:right;color:orangered;">橙色居右</span>
<span style="display:block;text-align:center;color:orangered;">橙色居中</span>

'''
                        ),

                        fac.AntdDivider(
                            '利用fmc渲染原生HTML',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fac.AntdDivider(
    '默认不开启',
    innerTextOrientation='left'
),
fmc.FefferyMarkdown(
    markdownStr='''
<span style="display:block;text-align:right;color:orangered;">橙色居右</span>
<span style="display:block;text-align:center;color:orangered;">橙色居中</span>

'''
),

fac.AntdDivider(
    '开启后',
    innerTextOrientation='left'
),
fmc.FefferyMarkdown(
    renderHtml=True,
    markdownStr='''
<span style="display:block;text-align:right;color:orangered;">橙色居右</span>
<span style="display:block;text-align:center;color:orangered;">橙色居中</span>

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
                    id='利用fmc渲染原生HTML',
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
                    {'title': '利用fmc渲染原生HTML', 'href': '#利用fmc渲染原生HTML'}
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

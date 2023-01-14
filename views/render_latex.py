from dash import html
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
import feffery_antd_components as fac

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
                            'title': '渲染LaTeX公式'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('中支持渲染基于LaTeX的行内公式与块公式，其中字符串需要前缀'),
                        fac.AntdText('r', code=True),
                        fac.AntdText('从而避免转义，具体使用参考下面的例子：'),
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            markdownStr=r'''
　　这是行LaTeX公式示例：$E=mc^2$

　　这是块LaTeX公式示例：

$$

\lim_{x \to \infty} \frac{1}{n(n+1)}

$$

'''
                        ),

                        fac.AntdDivider(
                            '利用fmc渲染LaTeX公式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString=r"""
fmc.FefferyMarkdown(
    markdownStr=r'''
　　这是行LaTeX公式示例：$E=mc^2$

　　这是块LaTeX公式示例：

$$

\lim_{x \to \infty} \frac{1}{n(n+1)}

$$

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
                    id='利用fmc渲染LaTeX公式',
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
                    {'title': '利用fmc渲染LaTeX公式', 'href': '#利用fmc渲染LaTeX公式'}
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

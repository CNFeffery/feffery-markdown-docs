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
                            'title': '支持GFM语法'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('支持'),
                        fac.AntdText('GFM', strong=True),
                        fac.AntdText(
                            '（GitHub Flavored Markdown）',
                            italic=True
                        ),
                        fac.AntdText('中的常用语法：')
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            markdownStr=r'''
## 自动识别链接

www.example.com, https://example.com, and contact@example.com.

## 删除线

~one~ or ~~two~~ tildes.

## 表格

| a | b  |  c |  d  |
| - | :- | -: | :-: |
| 1 | 2  |  3 |  4  |
| 5 | 6  |  7 |  8  |
| 9 | 10  |  11 |  12  |

## 待办事项

* [ ] to do
* [x] done

'''
                        ),

                        fac.AntdDivider(
                            '在fmc中直接使用GFM语法',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fmc.FefferyMarkdown(
    markdownStr=r'''
## 自动识别链接

www.example.com, https://example.com, and contact@example.com.

## 删除线

~one~ or ~~two~~ tildes.

## 表格

| a | b  |  c |  d  |
| - | :- | -: | :-: |
| 1 | 2  |  3 |  4  |
| 5 | 6  |  7 |  8  |
| 9 | 10  |  11 |  12  |

## 待办事项

* [ ] to do
* [x] done

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
                    id='在fmc中直接使用GFM语法',
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
                    {'title': '在fmc中直接使用GFM语法', 'href': '#在fmc中直接使用GFM语法'}
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

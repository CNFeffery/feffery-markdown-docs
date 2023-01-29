from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

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
                            'title': '完整参数说明'
                        },
                        {
                            'title': 'FefferySyntaxHighlighter'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                html.Div(
                    [
                        fac.AntdDivider(
                            '参数说明',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),
                        fmc.FefferyMarkdown(
                            markdownStr=open('./documents/FefferySyntaxHighlighter参数说明.md',
                                             encoding='utf-8').read()
                        ),
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='FefferySyntaxHighlighter参数说明',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto'
            }
        )
    ],
    style={
        'display': 'flex',
        'padding': '25px'
    }
)

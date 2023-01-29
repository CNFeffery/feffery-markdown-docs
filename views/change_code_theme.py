from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

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
                            'title': '切换代码主题'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('中内置了数十种常见的代码主题，你可以通过设置参数'),
                        fac.AntdText('codeTheme', code=True),
                        fac.AntdText('来改变代码主题，参考下面的示例：')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fmc.FefferyMarkdown(
                                    markdownStr=f'''
```python
# 当前代码主题：{theme}
import dash
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

app = dash.Dash(__name__)
```
''',
                                    codeTheme=theme
                                )
                                for theme in [
                                    'a11y-dark', 'atom-dark', 'coldark-cold', 'coldark-dark', 'coy', 'coy-without-shadows', 'darcula', 'dracula',
                                    'nord', 'okaidia', 'prism', 'solarizedlight', 'twilight', 'duotone-sea', 'duotone-dark', 'duotone-light',
                                    'duotone-space', 'gh-colors', 'gruvbox-dark', 'material-dark', 'night-owl', 'one-light', 'pojoaque',
                                    'solarized-dark-atom', 'synthwave84', 'z-touch'
                                ]
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            'fmc中内置的全部代码主题',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fac.AntdSpace(
    [
        fmc.FefferyMarkdown(
            markdownStr=f'''
```python
# 当前代码主题：{theme}
import dash
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

app = dash.Dash(__name__)
```
''',
            codeTheme=theme
        )
        for theme in [
            'a11y-dark', 'atom-dark', 'coldark-cold', 'coldark-dark', 'coy', 'coy-without-shadows', 'darcula', 'dracula',
            'nord', 'okaidia', 'prism', 'solarizedlight', 'twilight', 'duotone-sea', 'duotone-dark', 'duotone-light',
            'duotone-space', 'gh-colors', 'gruvbox-dark', 'material-dark', 'night-owl', 'one-light', 'pojoaque',
            'solarized-dark-atom', 'synthwave84', 'z-touch'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
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
                    id='fmc中内置的全部代码主题',
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
                    {'title': 'fmc中内置的全部代码主题', 'href': '#fmc中内置的全部代码主题'}
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

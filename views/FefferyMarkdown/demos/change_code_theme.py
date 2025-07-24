import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fmc.FefferyMarkdown(
                markdownStr=f"""
```python
# 当前代码主题：{theme}
import dash
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

app = dash.Dash(__name__)
```
""",
                codeTheme=theme,
            )
            for theme in [
                'a11y-dark',
                'atom-dark',
                'coldark-cold',
                'coldark-dark',
                'coy',
                'coy-without-shadows',
                'darcula',
                'dracula',
                'nord',
                'okaidia',
                'prism',
                'solarizedlight',
                'twilight',
                'duotone-sea',
                'duotone-dark',
                'duotone-light',
                'duotone-space',
                'gh-colors',
                'gruvbox-dark',
                'material-dark',
                'night-owl',
                'one-light',
                'pojoaque',
                'solarized-dark-atom',
                'synthwave84',
                'z-touch',
            ]
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fac.AntdSpace(
    [
        fmc.FefferyMarkdown(
            markdownStr=f"""
```python
# 当前代码主题：{theme}
import dash
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

app = dash.Dash(__name__)
```
""",
            codeTheme=theme,
        )
        for theme in [
            'a11y-dark',
            'atom-dark',
            'coldark-cold',
            'coldark-dark',
            'coy',
            'coy-without-shadows',
            'darcula',
            'dracula',
            'nord',
            'okaidia',
            'prism',
            'solarizedlight',
            'twilight',
            'duotone-sea',
            'duotone-dark',
            'duotone-light',
            'duotone-space',
            'gh-colors',
            'gruvbox-dark',
            'material-dark',
            'night-owl',
            'one-light',
            'pojoaque',
            'solarized-dark-atom',
            'synthwave84',
            'z-touch',
        ]
    ],
    direction='vertical',
    style={'width': '100%'},
)
'''
        }
    ]

from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fmc.FefferySyntaxHighlighter(
        codeString="""
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import (
    html, dcc, Input, Output, State
)

app = dash.Dash(__name__)
""",
        language='python',
        removedLineNumbers=[2, 3, 4],
        addedLineNumbers=[5, 6, 7],
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fmc.FefferySyntaxHighlighter(
    codeString="""
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import (
    html, dcc, Input, Output, State
)

app = dash.Dash(__name__)
""",
    language='python',
    removedLineNumbers=[2, 3, 4],
    addedLineNumbers=[5, 6, 7],
)
'''
        }
    ]

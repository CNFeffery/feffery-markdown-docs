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
                            'title': '独立的代码高亮渲染'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('中的'),
                        fac.AntdText('FefferySyntaxHighlighter', strong=True),
                        fac.AntdText('可用于直接进行指定语言的代码高亮渲染：'),
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferySyntaxHighlighter(
                            codeString='''
def python_function_demo():

    print("this is a python function")
''',
                            language='python'
                        ),

                        fmc.FefferySyntaxHighlighter(
                            codeString='''
const javascriptFunctionDemo = () => {
    console.log("this is a javascript function")
}
''',
                            language='javascript',
                            codeTheme='a11y-dark'
                        ),

                        fmc.FefferySyntaxHighlighter(
                            codeString='''
r_function_demo <- function() {
    print("this is a R function")
}
''',
                            language='r',
                            codeTheme='synthwave84'
                        ),

                        fmc.FefferySyntaxHighlighter(
                            codeString='''
function julia_function()
    println("this is a julia function")
end
''',
                            language='julia',
                            codeTheme='night-owl'
                        ),

                        fac.AntdDivider(
                            '使用FefferySyntaxHighlighter渲染代码高亮',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fmc.FefferySyntaxHighlighter(
    codeString='''
def python_function_demo():

    print("this is a python function")
''',
    language='python'
),

fmc.FefferySyntaxHighlighter(
    codeString='''
const javascriptFunctionDemo = () => {
    console.log("this is a javascript function")
}
''',
    language='javascript',
    codeTheme='a11y-dark'
),

fmc.FefferySyntaxHighlighter(
    codeString='''
r_function_demo <- function() {
    print("this is a R function")
}
''',
    language='r',
    codeTheme='synthwave84'
),

fmc.FefferySyntaxHighlighter(
    codeString='''
function julia_function()
    println("this is a julia function")
end
''',
    language='julia',
    codeTheme='night-owl'
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
                    id='使用FefferySyntaxHighlighter渲染代码高亮',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fmc.FefferySyntaxHighlighter(
                            codeString='''
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import (
    html, dcc, Input, Output, State
)

app = dash.Dash(__name__)
''',
                            language='python',
                            removedLineNumbers=[2, 3, 4],
                            addedLineNumbers=[5, 6, 7]
                        ),

                        fac.AntdDivider(
                            '为代码行渲染diff效果',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fmc.FefferySyntaxHighlighter(
    codeString='''
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import (
    html, dcc, Input, Output, State
)

app = dash.Dash(__name__)
''',
    language='python',
    removedLineNumbers=[2, 3, 4],
    addedLineNumbers=[5, 6, 7]
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
                    id='为代码行渲染diff效果',
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
                    {
                        'title': '使用FefferySyntaxHighlighter渲染代码高亮',
                        'href': '#使用FefferySyntaxHighlighter渲染代码高亮'
                    },
                    {
                        'title': '为代码行渲染diff效果',
                        'href': '#为代码行渲染diff效果'
                    }
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '25px'
            }
        ),

        # 侧边参数栏
        side_props.side_props_layout_syntax_highlighter
    ],
    style={
        'display': 'flex'
    }
)

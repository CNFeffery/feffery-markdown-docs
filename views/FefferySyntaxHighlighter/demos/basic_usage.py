from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fmc.FefferySyntaxHighlighter(
            codeString="""
def python_function_demo():

    print("this is a python function")
""",
            language='python',
        ),
        fmc.FefferySyntaxHighlighter(
            codeString="""
const javascriptFunctionDemo = () => {
    console.log("this is a javascript function")
}
""",
            language='javascript',
            codeTheme='a11y-dark',
        ),
        fmc.FefferySyntaxHighlighter(
            codeString="""
r_function_demo <- function() {
    print("this is a R function")
}
""",
            language='r',
            codeTheme='synthwave84',
        ),
        fmc.FefferySyntaxHighlighter(
            codeString="""
function julia_function()
    println("this is a julia function")
end
""",
            language='julia',
            codeTheme='night-owl',
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fmc.FefferySyntaxHighlighter(
        codeString="""
def python_function_demo():

    print("this is a python function")
""",
        language='python',
    ),
    fmc.FefferySyntaxHighlighter(
        codeString="""
const javascriptFunctionDemo = () => {
    console.log("this is a javascript function")
}
""",
        language='javascript',
        codeTheme='a11y-dark',
    ),
    fmc.FefferySyntaxHighlighter(
        codeString="""
r_function_demo <- function() {
    print("this is a R function")
}
""",
        language='r',
        codeTheme='synthwave84',
    ),
    fmc.FefferySyntaxHighlighter(
        codeString="""
function julia_function()
    println("this is a julia function")
end
""",
        language='julia',
        codeTheme='night-owl',
    ),
]
'''
        }
    ]

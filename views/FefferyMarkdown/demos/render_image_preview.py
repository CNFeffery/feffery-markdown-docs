from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fmc.FefferyMarkdown(
        imagePreview=True,
        renderHtml=True,
        codeStyle={'fontSize': '20px'},
        markdownStr="""
- 基于markdown语法渲染图片

![image](/assets/imgs/fmc-logo.svg)

- 基于原生HTML渲染图片

<div style="text-align: center;">
<img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />
</ div>

""",
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fmc.FefferyMarkdown(
    imagePreview=True,
    renderHtml=True,
    codeStyle={'fontSize': '20px'},
    markdownStr="""
- 基于markdown语法渲染图片

![image](/assets/imgs/fmc-logo.svg)

- 基于原生HTML渲染图片

<div style="text-align: center;">
<img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />
</ div>

""",
)
'''
        }
    ]

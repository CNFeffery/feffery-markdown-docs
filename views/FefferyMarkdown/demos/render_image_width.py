from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fmc.FefferyMarkdown(
        imageForceAlignCenter=True,
        imageWidth='33%',
        renderHtml=True,
        codeStyle={'fontSize': '20px'},
        markdownStr="""
- 强制统一图片宽度为`33%`

![image](/assets/imgs/fmc-logo.svg)

<img src="/assets/imgs/index/玩转dash星球二维码.jpg" width="200" height="200" />

""",
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fmc.FefferyMarkdown(
    imageForceAlignCenter=True,
    imageWidth='33%',
    renderHtml=True,
    codeStyle={'fontSize': '20px'},
    markdownStr="""
- 强制统一图片宽度为`33%`

![image](/assets/imgs/fmc-logo.svg)

<img src="/assets/imgs/index/玩转dash星球二维码.jpg" width="200" height="200" />

""",
)
'''
        }
    ]

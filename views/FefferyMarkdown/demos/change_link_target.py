import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('默认linkTarget="_blank"', innerTextOrientation='left'),
        fmc.FefferyMarkdown(
            markdownStr="""[fac官网](http://fac.feffery.tech/)"""
        ),
        fac.AntdDivider('linkTarget="_self"', innerTextOrientation='left'),
        fmc.FefferyMarkdown(
            linkTarget='_self',
            markdownStr="""[fac官网](http://fac.feffery.tech/)""",
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fac.AntdDivider('默认linkTarget="_blank"', innerTextOrientation='left'),
    fmc.FefferyMarkdown(
        markdownStr="""[fac官网](http://fac.feffery.tech/)"""
    ),
    fac.AntdDivider('linkTarget="_self"', innerTextOrientation='left'),
    fmc.FefferyMarkdown(
        linkTarget='_self',
        markdownStr="""[fac官网](http://fac.feffery.tech/)""",
    ),
]
'''
        }
    ]

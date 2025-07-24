import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('默认不开启', innerTextOrientation='left'),
        fmc.FefferyMarkdown(
            markdownStr="""
<span style="display:block;text-align:right;color:orangered;">橙色居右</span>
<span style="display:block;text-align:center;color:orangered;">橙色居中</span>

<details><summary>点我展开</summary>

这是可展开内容测试巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉

</details>
"""
        ),
        fac.AntdDivider('开启后', innerTextOrientation='left'),
        fmc.FefferyMarkdown(
            renderHtml=True,
            markdownStr="""
<span style="display:block;text-align:right;color:orangered;">橙色居右</span>
<span style="display:block;text-align:center;color:orangered;">橙色居中</span>

<details><summary>点我展开</summary>

这是可展开内容测试巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉

</details>
""",
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fac.AntdDivider('默认不开启', innerTextOrientation='left'),
    fmc.FefferyMarkdown(
        markdownStr="""
<span style="display:block;text-align:right;color:orangered;">橙色居右</span>
<span style="display:block;text-align:center;color:orangered;">橙色居中</span>

<details><summary>点我展开</summary>

这是可展开内容测试巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉

</details>
"""
    ),
    fac.AntdDivider('开启后', innerTextOrientation='left'),
    fmc.FefferyMarkdown(
        renderHtml=True,
        markdownStr="""
<span style="display:block;text-align:right;color:orangered;">橙色居右</span>
<span style="display:block;text-align:center;color:orangered;">橙色居中</span>

<details><summary>点我展开</summary>

这是可展开内容测试巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉

</details>
""",
    ),
]
'''
        }
    ]

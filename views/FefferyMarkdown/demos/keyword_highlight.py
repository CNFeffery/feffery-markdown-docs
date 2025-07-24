from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fmc.FefferyMarkdown(
        searchKeyword='标题',
        markdownStr="""
# 1 测试一级标题
## 1.1 测试二级标题
### 1.1.1 测试三级标题

测试内容。

""",
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fmc.FefferyMarkdown(
    searchKeyword='标题',
    markdownStr="""
# 1 测试一级标题
## 1.1 测试二级标题
### 1.1.1 测试三级标题

测试内容。

""",
)
'''
        }
    ]

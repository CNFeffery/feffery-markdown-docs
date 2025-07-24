from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fmc.FefferyMarkdown(
        h1Style={
            'backgroundImage': 'linear-gradient(to right, orange, purple)',
            'color': 'transparent',
            'display': 'inline-table',
            '-webkit-background-clip': 'text',
        },
        h2Style={
            'borderBottom': '3px solid #1890ff',
            'fontFamily': 'KaiTi',
            'textAlign': 'center',
            'margin': '0 auto',
            'display': 'table',
        },
        h3Style={
            'color': 'transparent',
            '-webkit-text-stroke': '1px black',
            'letterSpacing': '0.04em',
        },
        markdownStr=r"""
# 一级标题

## 二级标题

### 三级标题
""",
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fmc.FefferyMarkdown(
    h1Style={
        'backgroundImage': 'linear-gradient(to right, orange, purple)',
        'color': 'transparent',
        'display': 'inline-table',
        '-webkit-background-clip': 'text',
    },
    h2Style={
        'borderBottom': '3px solid #1890ff',
        'fontFamily': 'KaiTi',
        'textAlign': 'center',
        'margin': '0 auto',
        'display': 'table',
    },
    h3Style={
        'color': 'transparent',
        '-webkit-text-stroke': '1px black',
        'letterSpacing': '0.04em',
    },
    markdownStr=r"""
# 一级标题

## 二级标题

### 三级标题
""",
)
'''
        }
    ]

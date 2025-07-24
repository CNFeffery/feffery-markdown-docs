from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fmc.FefferyMarkdown(
        markdownStr=r"""
　　这是行内LaTeX公式示例：$E=mc^2$

　　这是块级LaTeX公式示例：

$$

\lim_{x \to \infty} \frac{1}{n(n+1)}

$$

"""
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': r'''
fmc.FefferyMarkdown(
    markdownStr=r"""
　　这是行内LaTeX公式示例：$E=mc^2$

　　这是块级LaTeX公式示例：

$$

\lim_{x \to \infty} \frac{1}{n(n+1)}

$$

"""
)
'''
        }
    ]

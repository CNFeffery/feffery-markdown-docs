import feffery_antd_components as fac
from dash.dependencies import Component

# 国际化
from i18n import translator


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {
                    'title': translator.t(
                        'FefferySyntaxHighlighter 代码语法高亮'
                    )
                },
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferySyntaxHighlighter 代码语法高亮'), level=2
        ),
        fac.AntdParagraph(
            translator.t('对常见类型代码字符串进行语法高亮展示。')
        ),
    ]

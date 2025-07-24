from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    diff,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferySyntaxHighlighter')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('对常见各类型代码字符串进行语法高亮展示。'),
        },
        {
            'path': 'diff',
            'title': t('代码diff效果'),
            'description': t(
                '配合参数`removedLineNumbers`、`addedLineNumbers`实现代码diff效果。'
            ),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )

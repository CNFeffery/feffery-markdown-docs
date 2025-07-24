from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    change_code_theme,  # noqa: F401
    render_latex,  # noqa: F401
    render_mermaid,  # noqa: F401
    support_gfm,  # noqa: F401
    render_raw_html,  # noqa: F401
    change_link_target,  # noqa: F401
    custom_code_block_style,  # noqa: F401
    render_image_basic,  # noqa: F401
    render_image_preview,  # noqa: F401
    render_image_align_center,  # noqa: F401
    render_image_width,  # noqa: F401
    custom_element_style,  # noqa: F401
    use_external_theme,  # noqa: F401
    external_link_redirect,  # noqa: F401
    auto_render_toc,  # noqa: F401
    keyword_highlight,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyMarkdown')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最基础的markdown内容渲染。'),
        },
        {
            'path': 'change_code_theme',
            'title': t('更换代码主题'),
            'description': t(
                '针对代码块内容，设置参数`codeTheme`来更换使用不同的内置代码高亮主题。'
            ),
        },
        {
            'path': 'render_latex',
            'title': t('渲染LaTeX公式'),
            'description': t(
                '可直接渲染常见的行内、块级**LaTeX**公式，注意字符串需要前缀`r`以避免转义。'
            ),
        },
        {
            'path': 'render_mermaid',
            'title': t('渲染Mermaid图表'),
            'description': t(
                '支持将**mermaid**类型的代码块直接渲染为图表，注意需要在`dash.Dash()`中通过参数`external_scripts`额外引入此项功能所需的**mermaid**静态资源。'
            ),
        },
        {
            'path': 'support_gfm',
            'title': t('支持GFM语法'),
            'description': t(
                '支持GFM（GitHub Flavored Markdown）中的常用语法。'
            ),
        },
        {
            'path': 'render_raw_html',
            'title': t('渲染原生HTML'),
            'description': t(
                '默认不开启原生HTML渲染，如果需要开启，设置参数`renderHtml=True`即可。'
            ),
        },
        {
            'path': 'change_link_target',
            'title': t('改变链接跳转方式'),
            'description': t(
                '针对内容中的链接，设置参数`linkTarget`来改变点击链接后的跳转方式。'
            ),
        },
        {
            'path': 'custom_code_block_style',
            'title': t('自定义代码块样式'),
            'description': t(
                '针对代码块内容，可设置参数`codeBlockStyle`、`codeStyle`进行进一步的样式自定义。'
            ),
        },
        {
            'path': 'render_image_basic',
            'title': t('基础图片渲染'),
            'description': t(
                '默认支持markdown中的图片渲染语法，设置参数`renderHtml=True`可支持原生HTML形式的图片渲染。'
            ),
        },
        {
            'path': 'render_image_preview',
            'title': t('交互式图片预览'),
            'description': t(
                '设置参数`imagePreview=True`后，可自针对图片进行交互式预览查看。'
            ),
        },
        {
            'path': 'render_image_align_center',
            'title': t('图片居中显示'),
            'description': t(
                '设置参数`imageForceAlignCenter=True`后，可针对文档中的全部图片进行强制居中显示。'
            ),
        },
        {
            'path': 'render_image_width',
            'title': t('统一设置图片宽度'),
            'description': t('通过参数`imageWidth`可统一设置图片宽度。'),
        },
        {
            'path': 'custom_element_style',
            'title': t('自定义各元素样式'),
            'description': t(
                '针对自定义元素内容，可通过相应的样式参数，进行进一步的样式自定义。'
            ),
        },
        {
            'path': 'use_external_theme',
            'title': t('使用拓展主题'),
            'description': t(
                '配合参数`markdownBaseClassName`可使用拓展主题，可在[此处](https://github.com/CNFeffery/feffery-markdown-components/raw/main/fmc-themes/fmc-themes.zip)下载拓展样式主题包，解压后放入当前应用的`assets`静态资源目录下即可。'
            ),
        },
        {
            'path': 'external_link_redirect',
            'title': t('外部链接重定向'),
            'description': t(
                '针对文档渲染内容中的外部链接，可进行重定向安全跳转。'
            ),
        },
        {
            'path': 'auto_render_toc',
            'title': t('自动生成目录'),
            'description': t(
                '设置参数`titleAsId=True`时，会在渲染后为文档中的所有标题元素添加与其内容一致的`id`信息，同时会产生出属性值`facAnchorLinkDict`，可通过回调函数直接作为[fac](https://fac.feffery.tech)中锚点组件[AntdAnchor](https://fac.feffery.tech/AntdAnchor)的参数`linkDict`，从而实现自动目录生成。'
            ),
            'iframe': True,
        },
        {
            'path': 'keyword_highlight',
            'title': t('关键字高亮'),
            'description': t('通过参数`searchKeyword`启用关键字高亮功能。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )

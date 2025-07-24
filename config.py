import json
import feffery_markdown_components as fmc

# 国际化
from i18n import translator


class AppConfig:
    """
    应用常规参数配置
    """

    # 应用默认标签页标题
    title = 'feffery-markdown-components在线文档'

    # 应用logo地址
    logo_path = 'imgs/fmc-logo.svg'

    # 页首标题
    page_header_title = 'feffery-markdown-components'

    # 当前组件版本
    library_version = fmc.__version__

    # 组件仓库地址
    library_repo = 'https://github.com/CNFeffery/feffery-markdown-components'

    # 文档仓库地址
    doc_library_repo = 'https://github.com/CNFeffery/feffery-markdown-docs'

    # 文档Gitee仓库地址
    doc_gitee_library_repo = 'https://gitee.com/cnfeffery/feffery-markdown-docs'

    # 文档仓库分支名称
    doc_library_branch = 'main'

    # 当前应用是否为正式发布模式
    is_release = True

    # 文档贡献者信息
    doc_contributors = json.load(open('./public/contributors.json'))

    # 项目国际化指南地址
    i18n_guide_link = (
        'https://github.com/CNFeffery/feffery-utils-docs/issues/166'
    )

    @staticmethod
    def side_menu_items() -> list:
        # 侧边菜单栏数据结构
        return [
            {
                'component': 'ItemGroup',
                'props': {'key': '快速入门', 'title': translator.t('快速入门')},
                'children': [
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/what-is-fmc',
                            'name': '/what-is-fmc',
                            'href': '/what-is-fmc',
                            'title': translator.t('fmc是什么'),
                        },
                    }
                ],
            },
            {'component': 'Divider', 'props': {'dashed': True}},
            {
                'component': 'ItemGroup',
                'props': {'key': '组件介绍', 'title': translator.t('组件介绍')},
                'children': [
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/FefferyMarkdown',
                            'name': '/FefferyMarkdown',
                            'title': translator.t(
                                'FefferyMarkdown markdown渲染'
                            ),
                            'href': '/FefferyMarkdown',
                        },
                    },
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/FefferySyntaxHighlighter',
                            'name': '/FefferySyntaxHighlighter',
                            'title': translator.t(
                                'FefferySyntaxHighlighter 代码语法高亮'
                            ),
                            'href': '/FefferySyntaxHighlighter',
                        },
                    },
                ],
            },
        ]

    # 侧边菜单栏key值 -> 展开项节点key值数组
    side_menu_expand_keys = {}


class DocsConfig:
    """
    文档所需特殊参数配置
    """

    # 具有额外参数说明的组件
    components_with_extra_params = []

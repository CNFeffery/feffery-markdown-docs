from dash import html
from flask import request
from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

from server import app

# 国际化
from i18n import translator

latest_deploy_datetime = datetime.today().strftime('%Y-%m-%d')


def render() -> Component:
    """渲染“fmc是什么”文档页"""

    current_locale = request.cookies.get(translator.cookie_name, 'zh-cn')

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(),
                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                translator.t(
                                    'feffery-markdown-components: Dash应用中强大的markdown渲染组件库'
                                ),
                                strong=True,
                                style={'fontSize': '30px'},
                            ),
                            fac.AntdText('🐣', style={'fontSize': '30px'}),
                        ],
                        id='🐣',
                    ),
                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                translator.t('文档最近更新：'), strong=True
                            ),
                            fac.AntdText(latest_deploy_datetime, code=True),
                        ]
                    ),
                    fac.AntdDivider(),
                    fac.AntdParagraph(
                        (
                            'feffery-markdown-components（简称fmc），基于react-markdown，将原始markdown文本直接渲染为美观的网页内容。'
                            if current_locale == 'zh-cn'
                            else 'feffery-markdown-components (abbreviated as fmc), based on react-markdown, directly renders raw markdown text into aesthetically pleasing web content.'
                        )
                    ),
                    html.Div(
                        [
                            html.Img(
                                src=app.get_asset_url('imgs/fmc-logo.svg'),
                                style={'height': '300px'},
                            )
                        ],
                        style={'textAlign': 'center'},
                    ),
                    fac.AntdDivider(),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('🤩', style={'fontSize': '26px'}),
                            fac.AntdText(
                                translator.t('特性'),
                                strong=True,
                                style={'fontSize': '26px'},
                            ),
                        ],
                        id=translator.t('特性'),
                    ),
                    html.Ul(
                        [
                            html.Li(
                                translator.t(
                                    '💪 稳定兼容，支持常用markdown语法及latex数学公式渲染'
                                ),
                                style={'listStyleType': 'circle'},
                            ),
                            html.Li(
                                translator.t('😋 使用简单，功能参数直观明了'),
                                style={'listStyleType': 'circle'},
                            ),
                            html.Li(
                                translator.t(
                                    '💎 样式美观，内置20+代码主题风格'
                                ),
                                style={'listStyleType': 'circle'},
                            ),
                        ]
                    ),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('🛫', style={'fontSize': '26px'}),
                            fac.AntdText(
                                translator.t('版本'),
                                strong=True,
                                style={'fontSize': '26px'},
                            ),
                        ],
                        id=translator.t('版本'),
                    ),
                    html.Ul(
                        [
                            html.Li(
                                fac.AntdParagraph(
                                    [
                                        fac.AntdText(
                                            translator.t('pypi最新稳定版本：')
                                        ),
                                        fac.AntdTag(content=fmc.__version__),
                                        html.Img(
                                            src='https://img.shields.io/pypi/v/feffery-markdown-components.svg?color=dark-green',
                                            style={
                                                'height': 20,
                                                'transform': 'translateY(5px)',
                                            },
                                        ),
                                    ]
                                ),
                                style={'listStyleType': 'circle'},
                            )
                        ]
                    ),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('📦', style={'fontSize': '26px'}),
                            fac.AntdText(
                                translator.t('安装'),
                                strong=True,
                                style={'fontSize': '26px'},
                            ),
                        ],
                        id=translator.t('安装'),
                    ),
                    fac.AntdTitle(translator.t('最新稳定版本：'), level=5),
                    fac.AntdText(
                        f'pip install feffery-markdown-components=={fmc.__version__} -U',
                        keyboard=True,
                        copyable=True,
                    ),
                    fac.AntdTitle(translator.t('最新预发布版本：'), level=5),
                    fac.AntdText(
                        'pip install feffery-markdown-components --pre -U',
                        keyboard=True,
                        copyable=True,
                    ),
                    *(
                        [
                            fac.AntdDivider(),
                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '🎩', style={'fontSize': '26px'}
                                    ),
                                    fac.AntdText(
                                        '加入交流群',
                                        strong=True,
                                        style={'fontSize': '26px'},
                                    ),
                                ],
                                id='加入交流群',
                            ),
                            fac.AntdCollapse(
                                html.Div(
                                    fac.AntdImage(
                                        src=app.get_asset_url(
                                            'imgs/index/feffery-添加好友二维码.jpg'
                                        ),
                                        style={
                                            'width': '300px',
                                            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                            'borderRadius': '5px',
                                        },
                                    ),
                                    style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                    },
                                ),
                                title='微信扫码添加好友，备注【dash学习】',
                                isOpen=True,
                                ghost=True,
                            ),
                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '👉', style={'fontSize': '26px'}
                                    ),
                                    fac.AntdText(
                                        '玩转dash公众号',
                                        strong=True,
                                        style={'fontSize': '26px'},
                                    ),
                                ],
                                id='玩转dash公众号',
                            ),
                            fac.AntdCollapse(
                                html.Div(
                                    fac.AntdImage(
                                        src=app.get_asset_url(
                                            'imgs/index/玩转dash公众号.jpg'
                                        ),
                                        style={
                                            'height': '300px',
                                            'width': '300px',
                                            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                            'borderRadius': '5px',
                                        },
                                    ),
                                    style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                    },
                                ),
                                title='扫码关注我的知识分享公众号【玩转dash】',
                                isOpen=True,
                                ghost=True,
                            ),
                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '🌏', style={'fontSize': '26px'}
                                    ),
                                    fac.AntdText(
                                        '玩转dash知识星球',
                                        strong=True,
                                        style={'fontSize': '26px'},
                                    ),
                                ],
                                id='玩转dash知识星球',
                            ),
                            fac.AntdCollapse(
                                html.Div(
                                    fac.AntdImage(
                                        src=app.get_asset_url(
                                            'imgs/index/玩转dash星球二维码.jpg'
                                        ),
                                        style={
                                            'width': '300px',
                                            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                            'borderRadius': '5px',
                                        },
                                    ),
                                    style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                    },
                                ),
                                title='更多dash高级知识技巧及海量应用案例模板，欢迎加入我的知识星球【玩转dash】',
                                isOpen=True,
                                ghost=True,
                            ),
                        ]
                        if current_locale == 'zh-cn'
                        else []
                    ),
                    html.Div(style={'height': '200px'}),
                ],
                style={'flex': 'auto'},
            ),
            html.Div(
                fac.AntdAnchor(
                    linkDict=[
                        {'title': '🐣' + translator.t('简介'), 'href': '#🐣'},
                        {
                            'title': '🤩' + translator.t('特性'),
                            'href': '#' + translator.t('特性'),
                        },
                        {
                            'title': '🛫' + translator.t('版本'),
                            'href': '#' + translator.t('版本'),
                        },
                        {
                            'title': '📦' + translator.t('安装'),
                            'href': '#' + translator.t('安装'),
                        },
                        *(
                            [
                                {
                                    'title': '🎩加入交流群',
                                    'href': '#加入交流群',
                                },
                                {
                                    'title': '👉玩转dash公众号',
                                    'href': '#玩转dash公众号',
                                },
                                {
                                    'title': '🌏玩转dash知识星球',
                                    'href': '#玩转dash知识星球',
                                },
                            ]
                            if current_locale == 'zh-cn'
                            else []
                        ),
                    ],
                    offsetTop=65,
                ),
                style={'flex': 'none'},
            ),
        ],
        style={'display': 'flex', 'padding': 25},
    )

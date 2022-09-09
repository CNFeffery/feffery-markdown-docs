from dash import dcc, html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
from dash.dependencies import Input, Output, State

from config import Config
from server import app, server
from views import (
    what_is_fmc,
    getting_started,
    change_code_theme,
    render_latex,
    support_gfm,
    render_raw_html,
    change_link_target,
    custom_code_block_style,
    render_image,
    custom_element_style,
    use_external_theme,
    external_link_redirect,
    auto_render_toc,
    all_props
)

app.layout = fuc.FefferyTopProgress(
    html.Div(
        [
            # 注入url监听
            dcc.Location(id='url'),

            # 注入快捷添加好友悬浮卡片
            html.Div(
                [
                    fac.AntdPopover(
                        fac.AntdButton(
                            fac.AntdIcon(icon='antd-bulb'),
                            shape='circle',
                            style={
                                'zoom': '1.25',
                                'boxShadow': '0 3px 6px -4px #0000001f, 0 6px 16px #00000014, 0 9px 28px 8px #0000000d'
                            }
                        ),
                        placement='left',
                        content=[
                            fac.AntdText(
                                '微信扫码加我好友，备注【dash学习】加入学习交流群，更多灵感更快进步',
                                strong=True
                            ),
                            fac.AntdImage(
                                src=app.get_asset_url(
                                    'imgs/feffery-添加好友二维码.jpg'),
                                width=250,
                                preview=False
                            )
                        ],
                        overlayStyle={
                            'width': '300px',
                            'height': '408px'
                        }
                    )
                ],
                style={
                    'position': 'fixed',
                    'right': '100px',
                    'bottom': '200px',
                    'zIndex': 99999
                }
            ),

            # 侧边栏折叠按钮
            # fac.AntdButton(
            #     fac.AntdIcon(
            #         id='fold-side-menu-icon',
            #         icon='antd-menu-fold'
            #     ),
            #     id='fold-side-menu',
            #     size='large',
            #     type='text',
            #     style={
            #         'position': 'fixed',
            #         'top': '400px',
            #         'left': 0,
            #         'zIndex': 99999,
            #         'padding': '5px 8px',
            #         'boxShadow': '2px 0 8px #00000026',
            #         'borderRadius': '0 4px 4px 0',
            #         'backgroundColor': 'white'
            #     }
            # ),

            # 页面结构
            fac.AntdRow(
                [
                    fac.AntdCol(
                        html.Img(
                            src=app.get_asset_url(
                                'imgs/fmc-logo.svg'),
                            style={
                                'height': '50px',
                                'padding': '0 10px',
                                'marginTop': '7px'
                            }
                        ),
                    ),
                    fac.AntdCol(
                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'feffery-markdown-components',
                                    strong=True,
                                    style={
                                        'fontSize': '35px'
                                    }
                                ),
                                fac.AntdText(
                                    f'v{fmc.__version__}',
                                    style={
                                        'fontSize': '10px',
                                        'paddingLeft': '2px'
                                    }
                                )
                            ]
                        )
                    ),

                    fac.AntdCol(
                        html.Div(
                            [
                                html.A(
                                    fac.AntdImage(
                                        alt='fmc源码仓库，欢迎star',
                                        src='https://img.shields.io/github/stars/CNFeffery/feffery-markdown-components?style=social',
                                        preview=False,
                                        fallback=None,
                                        style={
                                            'transform': 'translateY(0px) scale(1.25)'
                                        }
                                    ),
                                    href='https://github.com/CNFeffery/feffery-markdown-components',
                                    target='_blank',
                                    style={
                                        'cursor': 'pointer'
                                    }
                                ),

                                html.A(
                                    '皖ICP备2021012734号-1',
                                    href='https://beian.miit.gov.cn/',
                                    target='_blank',
                                    style={
                                        'fontSize': '10px',
                                        'marginLeft': '50px',
                                        'color': '#494f54'
                                    }
                                )
                            ],
                            style={
                                'float': 'right',
                                'paddingRight': '20px',
                                'marginTop': '20.5px'
                            }
                        ),
                        flex='auto'
                    )
                ],
                align="middle",
                style={
                    'height': '64px',
                    'boxShadow': 'rgb(240 241 242) 0px 2px 14px',
                    'background': 'white',
                    'marginBottom': '5px'
                }
            ),

            fac.AntdRow(
                [
                    fac.AntdCol(
                        fac.AntdAffix(
                            html.Div(
                                [
                                    fac.AntdMenu(
                                        id='router-menu',
                                        menuItems=Config.menuItems,
                                        mode='inline',
                                        defaultOpenKeys=[],
                                        style={
                                            'height': '100%',
                                            'overflow': 'hidden auto',
                                            'paddingBottom': '50px'
                                        }
                                    ),

                                    fac.AntdButton(
                                        fac.AntdIcon(
                                            id='fold-side-menu-icon',
                                            icon='antd-arrow-left'
                                        ),
                                        id='fold-side-menu',
                                        type='text',
                                        shape='circle',
                                        style={
                                            'position': 'absolute',
                                            'zIndex': 999,
                                            'top': '10px',
                                            'right': '-15px',
                                            'boxShadow': '0 4px 10px 0 rgba(0,0,0,.1)',
                                            'background': 'white'
                                        }
                                    )
                                ],
                                id='side-menu',
                                style={
                                    'width': '220px',
                                    'height': '100vh',
                                    'overflowY': 'auto',
                                    'transition': 'width 0.2s',
                                    'borderRight': '1px solid rgb(240, 240, 240)',
                                    'paddingRight': 20
                                }
                            ),
                            offsetTop=0
                        ),
                        flex='none'
                    ),

                    fac.AntdCol(
                        [
                            html.Div(
                                id='docs-content',
                                style={
                                    'backgroundColor': 'rgb(255, 255, 255)'
                                }
                            )
                        ],
                        flex='auto',
                        style={
                            'padding': '25px'
                        }
                    ),

                    fac.AntdBackTop(
                        duration=0.5
                    )
                ],
                wrap=False
            )
        ]
    ),
    listenPropsMode='exclude',
    excludeProps=Config.exclude_props,
    minimum=0.33,
    speed=800,
    debug=True
)


@app.callback(
    [Output('docs-content', 'children'),
     Output('router-menu', 'currentKey')],
    Input('url', 'pathname')
)
def render_docs_content(pathname):
    '''
    路由回调
    '''

    if pathname == '/what-is-fmc' or pathname == '/':
        pathname = '/what-is-fmc'
        return what_is_fmc.docs_content, pathname

    elif pathname == '/getting-started':
        return getting_started.docs_content, pathname

    elif pathname == '/change-code-theme':
        return change_code_theme.docs_content, pathname

    elif pathname == '/render-latex':
        return render_latex.docs_content, pathname

    elif pathname == '/support-gfm':
        return support_gfm.docs_content, pathname

    elif pathname == '/render-raw-html':
        return render_raw_html.docs_content, pathname

    elif pathname == '/change-link-target':
        return change_link_target.docs_content, pathname

    elif pathname == '/custom-code-block-style':
        return custom_code_block_style.docs_content, pathname

    elif pathname == '/render-image':
        return render_image.docs_content, pathname

    elif pathname == '/custom-element-style':
        return custom_element_style.docs_content, pathname

    elif pathname == '/use-external-theme':
        return use_external_theme.docs_content, pathname

    elif pathname == '/external-link-redirect':
        return external_link_redirect.docs_content, pathname

    elif pathname == '/auto-render-toc':
        return auto_render_toc.docs_content, pathname

    elif pathname == '/all-props':
        return all_props.docs_content, pathname

    return fac.AntdResult(status='404', title='您访问的页面不存在！'), pathname


app.clientside_callback(
    '''
    (nClicks, oldStyle) => {
        if (nClicks) {
            if (oldStyle.width === '220px') {
                return [
                    {
                        'width': 20,
                        'height': '100vh',
                        'overflowY': 'auto',
                        'transition': 'width 0.2s',
                        'borderRight': '1px solid rgb(240, 240, 240)',
                        'paddingRight': 20
                    },
                    'antd-arrow-right'
                ]
            }
            return [
                {
                    'width': '220px',
                    'height': '100vh',
                    'transition': 'width 0.2s',
                    'borderRight': '1px solid rgb(240, 240, 240)',
                    'paddingRight': 20
                },
                'antd-arrow-left'
            ]
        }
        return window.dash_clientside.no_update;
    }
    ''',
    [Output('side-menu', 'style'),
     Output('fold-side-menu-icon', 'icon')],
    Input('fold-side-menu', 'nClicks'),
    State('side-menu', 'style')
)

if __name__ == '__main__':
    app.run(debug=True)

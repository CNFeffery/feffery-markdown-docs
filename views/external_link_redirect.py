from dash import html
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
import feffery_antd_components as fac

from views import side_props

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.6
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '更多用法'
                        },
                        {
                            'title': '外部链接安全跳转'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText(
                            '针对文档渲染内容中的外部链接，可轻松进行安全跳转提示功能（譬如知乎中针对外链的点击跳转策略）：')
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            checkExternalLink=True,
                            externalLinkPrefixWhiteList=[
                                'http://fac.feffery.tech'],
                            safeRedirectUrlPrefix='/safe-redirect?target=',
                            markdownStr='''
- 内部链接正常跳转

[内部链接示例](/what-is-fmc)

- 非白名单外部链接中转提示跳转

[非白名单外部链接示例](https://github.com/CNFeffery/feffery-markdown-components)

- 白名单外部链接正常跳转

[白名单外部链接示例](http://fac.feffery.tech/what-is-fac)

'''
                        ),

                        fac.AntdDivider(
                            '外部链接安全跳转',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
from flask import request

@app.server.route('/safe-redirect')
def safe_redirect():

    target = request.args.get('target')

    return f'''
<div style="padding: 25px 20px; position: fixed; top: 35vh; left: 50vw; border: 1px solid #f0f0f0; transform: translate(-50%, -50%);">
    <span >检测到未知的外部链接，请谨慎访问：</ span>
    <a href="{target}">{target}</ a>
</ div>
'''

...

fmc.FefferyMarkdown(
    checkExternalLink=True,
    externalLinkPrefixWhiteList=['http://fac.feffery.tech'],
    safeRedirectUrlPrefix='/safe-redirect?target=',
    markdownStr='''
- 内部链接正常跳转

[内部链接示例](/what-is-fmc)

- 非白名单外部链接中转提示跳转

[非白名单外部链接示例](https://github.com/CNFeffery/feffery-markdown-components)

- 白名单外部链接正常跳转

[白名单外部链接示例](http://fac.feffery.tech/what-is-fac)

'''
)
"""
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='外部链接安全跳转',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '外部链接安全跳转', 'href': '#外部链接安全跳转'}
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '25px'
            }
        ),

        # 侧边参数栏
        side_props.side_props_layout
    ],
    style={
        'display': 'flex'
    }
)

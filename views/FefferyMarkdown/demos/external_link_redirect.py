from dash.dependencies import Component
import feffery_markdown_components as fmc


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fmc.FefferyMarkdown(
        checkExternalLink=True,
        externalLinkPrefixWhiteList=['http://fac.feffery.tech'],
        safeRedirectUrlPrefix='/safe-redirect?target=',
        markdownStr="""
- 内部链接正常跳转

[内部链接示例](/what-is-fmc)

- 非白名单外部链接中转提示跳转

[非白名单外部链接示例](https://github.com/CNFeffery/feffery-markdown-components)

- 白名单外部链接正常跳转

[白名单外部链接示例](http://fac.feffery.tech/what-is-fac)

""",
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
from flask import request

...

@app.server.route('/safe-redirect')
def safe_redirect():
    target = request.args.get('target')

    return f"""
<div style="padding: 25px 20px; position: fixed; top: 35vh; left: 50vw; border: 1px solid #f0f0f0; transform: translate(-50%, -50%);">
    <span >检测到未知的外部链接，请谨慎访问：</ span>
    <a href="{target}">{target}</ a>
</ div>
"""

...

fmc.FefferyMarkdown(
    checkExternalLink=True,
    externalLinkPrefixWhiteList=['http://fac.feffery.tech'],
    safeRedirectUrlPrefix='/safe-redirect?target=',
    markdownStr="""
- 内部链接正常跳转

[内部链接示例](/what-is-fmc)

- 非白名单外部链接中转提示跳转

[非白名单外部链接示例](https://github.com/CNFeffery/feffery-markdown-components)

- 白名单外部链接正常跳转

[白名单外部链接示例](http://fac.feffery.tech/what-is-fac)

""",
)
'''
        }
    ]

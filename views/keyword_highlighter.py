from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

from views import side_props

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(duration=0.6),
                fac.AntdBreadcrumb(
                    items=[{"title": "更多用法"}, {"title": "关键词高亮"}]
                ),
                fac.AntdDivider(isDashed=True),
                fac.AntdParagraph(
                    [
                        fac.AntdText("　　fmc", strong=True),
                        fac.AntdText(
                            "中支持对文档中的指定关键词进行高亮，适合文档搜索等场景，具体使用参考下面的例子："
                        ),
                    ]
                ),
                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            searchKeyword="标题",
                            markdownStr="""
# 1 测试一级标题
## 1.1 测试二级标题
### 1.1.1 测试三级标题

测试内容。

""",
                        ),
                        fac.AntdDivider(
                            "高亮显示关键词",
                            lineColor="#f0f0f0",
                            innerTextOrientation="left",
                        ),
                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language="python",
                                codeString='''
fmc.FefferyMarkdown(
    searchKeyword="标题",
    markdownStr="""
# 1 测试一级标题
## 1.1 测试二级标题
### 1.1.1 测试三级标题

测试内容。

""",
)
''',
                            ),
                            title="点击查看代码",
                            is_open=False,
                            ghost=True,
                        ),
                    ],
                    style={
                        "marginBottom": "40px",
                        "padding": "10px 10px 20px 10px",
                        "border": "1px solid #f0f0f0",
                    },
                    id="高亮显示关键词",
                    className="div-highlight",
                ),
                html.Div(style={"height": "100px"}),
            ],
            style={"flex": "auto", "padding": "25px"},
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[{"title": "高亮显示关键词", "href": "#高亮显示关键词"}],
                offsetTop=0,
            ),
            style={"flex": "none", "padding": "25px"},
        ),
        # 侧边参数栏
        side_props.side_props_layout,
    ],
    style={"display": "flex"},
)

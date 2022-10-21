from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

raw_markdown = '''
### 1 标题

在文字写书写不同数量的`#`可以完成不同的标题，如下：

# 一级标题

## 二级标题

### 三级标题

### 2 无序列表

无序列表的使用，在符号`-`后加空格使用。如下：

- 无序列表 1
- 无序列表 2
- 无序列表 3

如果要控制列表的层级，则需要在符号`-`前使用空格。如下：

- 无序列表 1
- 无序列表 2
  - 无序列表 2.1
  - 无序列表 2.2

### 3 有序列表

有序列表的使用，在数字及符号`.`后加空格后输入内容，如下：

1. 有序列表 1
2. 有序列表 2
3. 有序列表 3
'''

docs_content = html.Div(
    [
        fac.AntdBackTop(
            containerId='docs-content',
            duration=0.6
        ),

        html.Div(
            [
                fac.AntdTitle(
                    '1 开发环境的准备',
                    id='1 开发环境的准备',
                    level=2
                ),
                fmc.FefferyMarkdown(
                    markdownStr=open('./documents/1 开发环境的准备.md',
                                     encoding='utf-8').read()
                ),
                fac.AntdDivider(),
                fac.AntdTitle(
                    '2 基础使用',
                    id='2 基础使用',
                    level=2
                ),
                fmc.FefferyMarkdown(
                    markdownStr=open('./documents/2 基础使用.md',
                                     encoding='utf-8').read()
                ),
                fac.AntdDivider(),
                fmc.FefferyMarkdown(
                    markdownStr=raw_markdown
                )
            ],
            style={
                'flex': 'auto',
                'marginBottom': '200px'
            }
        ),

        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '1 开发环境的准备', 'href': '#1 开发环境的准备'},
                    {'title': '2 基础使用', 'href': '#2 基础使用'}
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'margin': '20px'
            }
        )
    ],
    style={
        'display': 'flex',
        'padding': '25px'
    }
)

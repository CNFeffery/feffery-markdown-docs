from dash import html
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app

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
                            'title': '使用拓展主题'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('中可以配合参数'),
                        fac.AntdText('markdownBaseClassName', code=True),
                        fac.AntdText('使用拓展主题包来对默认的整体样式风格进行替换，当前全部可用主题包'),
                        html.A(
                            '下载',
                            href='https://github.com/CNFeffery/feffery-markdown-components/raw/main/fmc-themes/fmc-themes.zip',
                            target='_blank'
                        ),
                        fac.AntdText('（国内加速'),
                        html.A(
                            '下载',
                            href='https://github.91chi.fun/https://github.com/CNFeffery/feffery-markdown-components/blob/main/fmc-themes/fmc-themes.zip',
                            target='_blank'
                        ),
                        fac.AntdText('），'),
                        fac.AntdText('将对应的主题包解压复制到到你的'),
                        fac.AntdText('assets', code=True),
                        fac.AntdText('目录中任意位置即可，当前所有可用主题效果如下：')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSegmented(
                            id='markdown-base-theme-select',
                            size='large',
                            options=[
                                {
                                    'label': theme,
                                    'value': theme
                                }
                                for theme in [
                                    'markdown-body', 'theme-drake', 'theme-drake-juejin',
                                    'theme-forest', 'theme-blubook', 'theme-pie'
                                ]
                            ],
                            block=True,
                            defaultValue='markdown-body'
                        ),

                        fmc.FefferyMarkdown(
                            id='markdown-base-theme-demo',
                            markdownStr=r'''

## 表格

| a | b  |  c |  d  |
| - | :- | -: | :-: |
| 1 | 2  |  3 |  4  |
| 5 | 6  |  7 |  8  |
| 9 | 10  |  11 |  12  |

## 待办事项

* [ ] to do
* [x] done

`Dash`与`fmc`的安装非常简单，这里建议大家养成好习惯，使用**虚拟环境**来构建我们开发`Dash`应用所使用到的环境，以使用`conda`作为环境管理软件为例，执行下列控制台命令我们来创建一个`Python`版本为`3.8`，名称为`dash-dev-demo`的环境，其中临时使用到国内上海交大的`conda`镜像源：

```bash
conda create -n dash-dev-demo python=3.8 -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main -y
```

使用`conda activate dash-dev-demo`激活我们刚刚创建的环境之后，再执行以下命令，就可以完成`Dash`+`fmc`+`fac`环境的搭建啦 😀（[`fac`](http://fac.feffery.tech/)是由我开发维护的另一个功能十分丰富的`Dash`通用网页组件库）：

```bash
pip install dash feffery-antd-components feffery-markdown-components
```

# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题

- 列表1
  - 列表1-1
  - 列表1-2

## 自动识别链接

www.example.com, https://example.com, and contact@example.com.

## 删除线

~one~ or ~~two~~ tildes.
'''
                        ),

                        fac.AntdDivider(
                            '使用不同的拓展主题',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeStyle={
                                    'whiteSpace': 'pre-wrap'
                                },
                                codeString="""
fac.AntdSegmented(
    id='markdown-base-theme-select',
    size='large',
    options=[
        {
            'label': theme,
            'value': theme
        }
        for theme in [
            'markdown-body', 'theme-drake', 'theme-drake-juejin',
            'theme-forest', 'theme-blubook', 'theme-pie'
        ]
    ],
    block=True,
    defaultValue='markdown-body'
),

fmc.FefferyMarkdown(
    id='markdown-base-theme-demo',
    markdownStr=r'''

## 表格

| a | b  |  c |  d  |
| - | :- | -: | :-: |
| 1 | 2  |  3 |  4  |
| 5 | 6  |  7 |  8  |
| 9 | 10  |  11 |  12  |

## 待办事项

* [ ] to do
* [x] done

`Dash`与`fmc`的安装非常简单，这里建议大家养成好习惯，使用**虚拟环境**来构建我们开发`Dash`应用所使用到的环境，以使用`conda`作为环境管理软件为例，执行下列控制台命令我们来创建一个`Python`版本为`3.8`，名称为`dash-dev-demo`的环境，其中临时使用到国内上海交大的`conda`镜像源：

```bash
conda create -n dash-dev-demo python=3.8 -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main -y
```

使用`conda activate dash-dev-demo`激活我们刚刚创建的环境之后，再执行以下命令，就可以完成`Dash`+`fmc`+`fac`环境的搭建啦 😀（[`fac`](http://fac.feffery.tech/)是由我开发维护的另一个功能十分丰富的`Dash`通用网页组件库）：

```bash
pip install dash feffery-antd-components feffery-markdown-components
```

# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题

- 列表1
- 列表1-1
- 列表1-2

## 自动识别链接

www.example.com, https://example.com, and contact@example.com.

## 删除线

~one~ or ~~two~~ tildes.
'''
)

...

@app.callback(
    Output('markdown-base-theme-demo', 'markdownBaseClassName'),
    Input('markdown-base-theme-select', 'value')
)
def markdown_base_theme_switch(theme):

    return theme
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
                    id='利用fmc渲染LaTeX公式',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '使用不同的拓展主题', 'href': '#使用不同的拓展主题'}
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
        'display': 'flex'
    }
)


@app.callback(
    Output('markdown-base-theme-demo', 'markdownBaseClassName'),
    Input('markdown-base-theme-select', 'value')
)
def markdown_base_theme_switch(theme):

    return theme

import feffery_antd_components as fac
import feffery_markdown_components as fmc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSegmented(
            id='markdown-base-theme-select',
            size='large',
            options=[
                {'label': theme, 'value': theme}
                for theme in [
                    'markdown-body',
                    'theme-drake',
                    'theme-drake-juejin',
                    'theme-forest',
                    'theme-blubook',
                    'theme-pie',
                ]
            ],
            block=True,
            defaultValue='markdown-body',
        ),
        fmc.FefferyMarkdown(
            id='markdown-base-theme-demo',
            markdownStr=r"""
## 表格

| a | b  |  c |  d  |
| - | :- | -: | :-: |
| 1 | 2  |  3 |  4  |
| 5 | 6  |  7 |  8  |
| 9 | 10  |  11 |  12  |

## 待办事项

* [ ] to do
* [x] done

`Dash`与`fmc`的安装非常简单，这里建议大家养成好习惯，使用**虚拟环境**来构建我们开发`Dash`应用所使用到的环境，以使用`conda`作为环境管理软件为例，执行下列控制台命令我们来创建一个`Python`版本为`3.10`，名称为`dash-dev-demo`的环境，其中临时使用到国内上海交大的`conda`镜像源：

```bash
conda create -n dash-dev-demo python=3.10 -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main -y
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
""",
        ),
    ]

    return demo_contents


@app.callback(
    Output('markdown-base-theme-demo', 'markdownBaseClassName'),
    Input('markdown-base-theme-select', 'value'),
)
def markdown_base_theme_switch(theme):
    return theme


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fac.AntdSegmented(
        id='markdown-base-theme-select',
        size='large',
        options=[
            {'label': theme, 'value': theme}
            for theme in [
                'markdown-body',
                'theme-drake',
                'theme-drake-juejin',
                'theme-forest',
                'theme-blubook',
                'theme-pie',
            ]
        ],
        block=True,
        defaultValue='markdown-body',
    ),
    fmc.FefferyMarkdown(
        id='markdown-base-theme-demo',
        markdownStr=r"""
## 表格

| a | b  |  c |  d  |
| - | :- | -: | :-: |
| 1 | 2  |  3 |  4  |
| 5 | 6  |  7 |  8  |
| 9 | 10  |  11 |  12  |

## 待办事项

* [ ] to do
* [x] done

`Dash`与`fmc`的安装非常简单，这里建议大家养成好习惯，使用**虚拟环境**来构建我们开发`Dash`应用所使用到的环境，以使用`conda`作为环境管理软件为例，执行下列控制台命令我们来创建一个`Python`版本为`3.10`，名称为`dash-dev-demo`的环境，其中临时使用到国内上海交大的`conda`镜像源：

```bash
conda create -n dash-dev-demo python=3.10 -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main -y
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
""",
    ),
]

...

@app.callback(
    Output('markdown-base-theme-demo', 'markdownBaseClassName'),
    Input('markdown-base-theme-select', 'value'),
)
def markdown_base_theme_switch(theme):
    return theme
'''
        }
    ]

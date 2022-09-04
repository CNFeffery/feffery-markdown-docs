from dash import html
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
import feffery_antd_components as fac

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
                            'title': '渲染图片内容'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fmc', strong=True),
                        fac.AntdText('中渲染图片的方式与常规markdown语法相同，且在设置参数'),
                        fac.AntdText('renderHtml=True', code=True),
                        fac.AntdText('之后，还可以书写原生HTML代码来渲染图片：')
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            renderHtml=True,
                            codeStyle={
                                'fontSize': '20px'
                            },
                            markdownStr='''
- 基于markdown语法渲染图片

![image](/assets/imgs/fmc-logo.svg)

- 基于原生HTML渲染图片

<div style="text-align: center;">
    <img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />
</ div>

'''
                        ),

                        fac.AntdDivider(
                            '基于链接渲染图片',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fmc.FefferyMarkdown(
    renderHtml=True,
    codeStyle={
        'fontSize': '20px'
    },
    markdownStr='''
- 基于markdown语法渲染图片

![image](/assets/imgs/fmc-logo.svg)

- 基于原生HTML渲染图片

<div style="text-align: center;">
<img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />
</ div>

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
                    id='基于链接渲染图片',
                    className='div-highlight'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　通过设置参数'),
                        fac.AntdText('imagePreview', code=True),
                        fac.AntdText('为'),
                        fac.AntdText('True', code=True),
                        fac.AntdText('可为渲染出的所有图片添加交互式预览功能：')
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            imagePreview=True,
                            renderHtml=True,
                            codeStyle={
                                'fontSize': '20px'
                            },
                            markdownStr='''
- 基于markdown语法渲染图片

![image](/assets/imgs/fmc-logo.svg)

- 基于原生HTML渲染图片

<div style="text-align: center;">
    <img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />
</ div>

'''
                        ),

                        fac.AntdDivider(
                            '交互式图片预览功能',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""  
fmc.FefferyMarkdown(
    imagePreview=True,
    renderHtml=True,
    codeStyle={
        'fontSize': '20px'
    },
    markdownStr='''
- 基于markdown语法渲染图片

![image](/assets/imgs/fmc-logo.svg)

- 基于原生HTML渲染图片

<div style="text-align: center;">
<img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />
</ div>

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
                    id='交互式图片预览功能',
                    className='div-highlight'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　当渲染内容中的部分图片加载失败时，默认会为其渲染占位图，你也可以通过参数'),
                        fac.AntdText('imageFallback', code=True),
                        fac.AntdText('来自行设置加载失败占位图：')
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            renderHtml=True,
                            codeStyle={
                                'fontSize': '20px'
                            },
                            markdownStr='''
- 默认的加载失败占位图

![image](/assets/imgs/fmc-logo-.svg)

<div style="text-align: center;">
    <img src="/assets/imgs/fmc-logo-.svg" width="200" height="200" />
</ div>

'''
                        ),

                        fac.AntdDivider(
                            '加载失败占位图',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fmc.FefferyMarkdown(
    renderHtml=True,
    codeStyle={
        'fontSize': '20px'
    },
    markdownStr='''
- 默认的加载失败占位图

![image](/assets/imgs/fmc-logo-.svg)

<div style="text-align: center;">
<img src="/assets/imgs/fmc-logo-.svg" width="200" height="200" />
</ div>

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
                    id='加载失败占位图',
                    className='div-highlight'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　设置参数'),
                        fac.AntdText('imageForceAlignCenter=True', code=True),
                        fac.AntdText('可以强制文档中所有图片以居中方式渲染，这在使用原生markdown语法插入图片时非常实用：')
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            imageForceAlignCenter=True,
                            renderHtml=True,
                            codeStyle={
                                'fontSize': '20px'
                            },
                            markdownStr='''
- 强制所有图片居中显示

![image](/assets/imgs/fmc-logo.svg)

<img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />

'''
                        ),

                        fac.AntdDivider(
                            '强制所有图片居中显示',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fmc.FefferyMarkdown(
    imageForceAlignCenter=True,
    renderHtml=True,
    codeStyle={
        'fontSize': '20px'
    },
    markdownStr='''
- 强制所有图片居中显示

![image](/assets/imgs/fmc-logo.svg)

<img src="/assets/imgs/fmc-logo.svg" width="200" height="200" />

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
                    id='强制所有图片居中显示',
                    className='div-highlight'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　当你希望文档中的图片大小可以统一时，可以设置参数'),
                        fac.AntdText('imageWidth', code=True),
                        fac.AntdText('或'),
                        fac.AntdText('imageHeight', code=True),
                        fac.AntdText('为一定的值：')
                    ]
                ),

                html.Div(
                    [
                        fmc.FefferyMarkdown(
                            imageForceAlignCenter=True,
                            imageWidth='25%',
                            renderHtml=True,
                            codeStyle={
                                'fontSize': '20px'
                            },
                            markdownStr='''
- 强制统一图片宽度为`25%`

![image](/assets/imgs/fmc-logo.svg)

<img src="/assets/imgs/feffery-添加好友二维码.jpg" width="200" height="200" />

'''
                        ),

                        fac.AntdDivider(
                            '统一设置图片的尺寸',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeString="""
fmc.FefferyMarkdown(
    imageForceAlignCenter=True,
    imageWidth='25%',
    renderHtml=True,
    codeStyle={
        'fontSize': '20px'
    },
    markdownStr='''
- 强制统一图片宽度为`25%`

![image](/assets/imgs/fmc-logo.svg)

<img src="/assets/imgs/feffery-添加好友二维码.jpg" width="200" height="200" />

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
                    id='统一设置图片的尺寸',
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
                    {'title': '基于链接渲染图片', 'href': '#基于链接渲染图片'},
                    {'title': '交互式图片预览功能', 'href': '#交互式图片预览功能'},
                    {'title': '加载失败占位图', 'href': '#加载失败占位图'},
                    {'title': '强制所有图片居中显示', 'href': '#强制所有图片居中显示'},
                    {'title': '统一设置图片的尺寸', 'href': '#统一设置图片的尺寸'},
                ],
                offsetTop=50
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

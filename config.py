class Config:
    # 顶端进度条需要忽略的监听目标
    exclude_props = [
        'side-menu.style',
        'fold-side-menu-icon.icon',
        'markdown-base-theme-demo.markdownBaseClassName',
        'side-props.style'
    ]

    # 定义侧边菜单树状结构数据
    menuItems = [
        {
            'component': 'ItemGroup',
            'props': {
                'key': '/',
                'title': '快速入门'
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': '/what-is-fmc',
                        'href': '/what-is-fmc',
                        'title': 'fmc是什么？'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/getting-started',
                        'href': '/getting-started',
                        'title': 'Dash+fmc 快速上手'
                    }
                }
            ]
        },
        {
            'component': 'ItemGroup',
            'props': {
                'key': '/',
                'title': '更多用法'
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': '/change-code-theme',
                        'href': '/change-code-theme',
                        'title': '切换代码主题'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/render-latex',
                        'href': '/render-latex',
                        'title': '渲染LaTeX公式'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/support-gfm',
                        'href': '/support-gfm',
                        'title': '支持GFM语法'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/render-raw-html',
                        'href': '/render-raw-html',
                        'title': '渲染原生HTML'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/change-link-target',
                        'href': '/change-link-target',
                        'title': '改变链接打开方式'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/custom-code-block-style',
                        'href': '/custom-code-block-style',
                        'title': '自定义代码块样式'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/render-image',
                        'href': '/render-image',
                        'title': '渲染图片内容'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/custom-element-style',
                        'href': '/custom-element-style',
                        'title': '自定义各元素样式'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/use-external-theme',
                        'href': '/use-external-theme',
                        'title': '使用拓展主题'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/external-link-redirect',
                        'href': '/external-link-redirect',
                        'title': '外部链接安全跳转'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/auto-render-toc',
                        'href': '/auto-render-toc',
                        'title': '自动生成目录'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/independent-code-syntax-highlighter-render',
                        'href': '/independent-code-syntax-highlighter-render',
                        'title': '独立的代码高亮渲染'
                    }
                }
            ]
        },
        {
            'component': 'ItemGroup',
            'props': {
                'key': '/all-props',
                'title': '完整参数说明'
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': '/markdown-all-props',
                        'href': '/markdown-all-props',
                        'title': 'FefferyMarkdown'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/syntax-highlighter-all-props',
                        'href': '/syntax-highlighter-all-props',
                        'title': 'FefferySyntaxHighlighter'
                    }
                }
            ]
        }
    ]

import re
import dash
from flask import request


class CustomDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        # scripts = (
        #     kwargs.pop('scripts').replace(
        #         'https://unpkg.com/', 'https://npm.elemecdn.com/'
        #     )
        # )
        scripts = kwargs.pop("scripts")

        # 提取scripts部分符合条件的外部js资源
        external_scripts = re.findall('(<script src="http.*?"></script>)', scripts)

        # 将原有的script标签内容替换为带备用地址错误切换的版本
        for external_script in external_scripts:
            if "mermaid.min.js" in external_script:
                pass
            else:
                # 提取当前资源地址
                origin_script_src = re.findall('"(.*?)"', external_script)[0]
                # 抽取关键信息
                library_name, library_version, library_file = re.findall(
                    "com/(.+)@(.+?)/(.+?)$", origin_script_src
                )[0]
                # 基于阿里cdn构建新的资源地址
                new_library_src = f"https://registry.npmmirror.com/{library_name}/{library_version}/files/{library_file}"

                scripts = scripts.replace(
                    external_script,
                    """<script src="{}" onerror='this.remove(); let fallbackScript = document.createElement("script"); fallbackScript.src = "{}"; document.querySelector("head").prepend(fallbackScript);'></script>""".format(
                        re.findall('"(.*?)"', external_script)[0].replace(
                            origin_script_src,
                            new_library_src,
                        ),
                        re.findall('"(.*?)"', external_script)[0],
                    ),
                )

        scripts = (
            """<script>
window.onerror = async function(message, source, lineno, colno, error) {
    if (message.includes('is not defined') !== -1) {
        await waitForModules();
    }
}

async function waitForModules() {
    const requiredModules = [
        'DashRenderer',
        'dash_html_components',
        'dash_core_components',
        'feffery_antd_components',
        'feffery_utils_components',
        'feffery_markdown_components'
    ];

    while (!areModulesDefined(requiredModules)) {
        await delay(100); // 延迟100毫秒
    }

    // 变量已定义，触发事件
    var renderer = new DashRenderer();
}

function areModulesDefined(modules) {
    return modules.every(module => window[module]);
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
</script>
"""
            + scripts
        )

        return super(CustomDash, self).interpolate_index(scripts=scripts, **kwargs)


app = CustomDash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=["./documents"],
    compress=True,
    external_scripts=[
        "https://registry.npmmirror.com/mermaid/latest/files/dist/mermaid.min.js"
    ],
)

app.title = "feffery-markdown-components在线文档"

server = app.server


@app.server.route("/safe-redirect")
def safe_redirect():
    target = request.args.get("target")

    return f"""
<div style="padding: 25px 20px; position: fixed; top: 35vh; left: 50vw; border: 1px solid #f0f0f0; transform: translate(-50%, -50%);">
    <span >检测到未知的外部链接，请谨慎访问：</ span>
    <a href="{target}">{target}</ a>
</ div>
"""

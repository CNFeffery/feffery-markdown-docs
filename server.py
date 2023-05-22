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
        scripts = kwargs.pop('scripts')

        # 提取scripts部分符合条件的外部js资源
        external_scripts = re.findall(
            '(<script src="http.*?"></script>)', scripts)

        # 将原有的script标签内容替换为带备用地址错误切换的版本
        for external_script in external_scripts:
            scripts = scripts.replace(
                external_script,
                '''<script src="{}" onerror='this.remove(); let fallbackScript = document.createElement("script"); fallbackScript.src = "{}"; document.querySelector("footer").appendChild(fallbackScript);'></script>'''.format(
                    re.findall('"(.*?)"', external_script)[0],
                    re.findall('"(.*?)"', external_script)[0]
                    .replace('https://unpkg.com/', 'https://npm.elemecdn.com/')
                )
            )

        scripts = '''<script>
window.onerror = async function(message, source, lineno, colno, error) { 
    if ( message.includes("DashRenderer") !== -1 ) {
        while ( typeof renderer === 'undefined' ) {
            try {
                var renderer = new DashRenderer();
            } catch {
                await new Promise(resolve => setTimeout(resolve, 200));
            }
        }
    }
}
</script>
''' + scripts

        return super(CustomDash, self).interpolate_index(scripts=scripts, **kwargs)

app = CustomDash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=[
        './documents'
    ],
    compress=True
)

app.title = 'feffery-markdown-components在线文档'

server = app.server


@app.server.route('/safe-redirect')
def safe_redirect():

    target = request.args.get('target')

    return f'''
<div style="padding: 25px 20px; position: fixed; top: 35vh; left: 50vw; border: 1px solid #f0f0f0; transform: translate(-50%, -50%);">
    <span >检测到未知的外部链接，请谨慎访问：</ span>
    <a href="{target}">{target}</ a>
</ div>
'''

import dash
from flask import request


class CustomDash(dash.Dash):

    def interpolate_index(self, **kwargs):
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'https://unpkg.zhimg.com/')
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'http://npm.elemecdn.com/')
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'https://fastly.jsdelivr.net/npm/')

        scripts = kwargs.pop('scripts')

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
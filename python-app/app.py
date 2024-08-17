import logging
import sys
from flask import Flask, request, render_template_string
import socket


app = Flask(__name__)

# 创建一个流处理器(StreamHandler),并设置为输出到stderr
stream_handler = logging.StreamHandler(stream=sys.stderr)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

# 为应用程序日志添加处理器
app.logger.addHandler(stream_handler)

# 设置日志级别为DEBUG
app.logger.setLevel(logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def index():
    # 获取请求头信息
    headers = request.headers
    # 获取响应信息（示例）
    response_info = {'status': 'success', 'message': 'Response data here.'}
    # 获取主机名
    hostname = socket.gethostname()

    # HTML 模板
    html_content = '''
    <html>
        <head><title>Server Info</title></head>
        <body>
            <h1>Server Information</h1>
            <h2>Hostname</h2>
            <table border="1">
                <tr><th>Hostname</th><td>{}</td></tr>
            </table>
            <h2>Request Headers</h2>
            <table border="1">
                <tr><th>Header</th><th>Value</th></tr>
                {}
            </table>
            <h2>Response Information</h2>
            <table border="1">
                <tr><th>Status</th><td>{}</td></tr>
                <tr><th>Message</th><td>{}</td></tr>
            </table>
        </body>
    </html>
    '''

    # 处理请求头信息为 HTML 表格格式
    request_headers_html = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in headers.items())

    return render_template_string(html_content.format(hostname, request_headers_html, response_info['status'], response_info['message']))


if __name__ == '__main__':
    app.run(debug=True)

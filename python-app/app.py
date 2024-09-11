import logging
import sys
from flask import Flask, request
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
def display_headers_and_hostname():
    # 获取请求头信息
    headers = request.headers

    # 获取服务器主机名
    hostname = socket.gethostname()

    # 将请求头信息和主机名格式化为 HTML
    headers_html = '<h1>New version</h1><ul>'
    for header, value in headers.items():
        headers_html += f'<li><strong>{header}:</strong> {value}</li>'
    headers_html += '</ul>'

    # 添加主机名信息
    headers_html += f'<h2>Server Hostname: {hostname}</h2>'

    return headers_html


if __name__ == '__main__':
    app.run(debug=True)

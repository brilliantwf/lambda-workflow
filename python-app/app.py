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
    # 获取服务器的主机名
    hostname = socket.gethostname()
    
    # 获取请求头信息
    request_headers = request.headers
    request_headers_dict = dict(request_headers)
    
    # 获取响应头信息（在此示例中，响应头信息是空的，因为它将在响应生成后填充）
    response_headers_dict = {}

    # 渲染 HTML
    return render_template_string('''
    <html>
    <head>
        <title>Server Info</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>服务器信息</h1>
        
        <h2>主机名</h2>
        <table>
            <tr><th>主机名</th></tr>
            <tr><td>{{ hostname }}</td></tr>
        </table>
        
        <h2>请求头信息</h2>
        <table>
            <tr><th>头部名称</th><th>值</th></tr>
            {% for key, value in request_headers_dict.items() %}
            <tr><td>{{ key }}</td><td>{{ value }}</td></tr>
            {% endfor %}
        </table>
        
        <h2>响应头信息</h2>
        <table>
            <tr><th>头部名称</th><th>值</th></tr>
            {% for key, value in response_headers_dict.items() %}
            <tr><td>{{ key }}</td><td>{{ value }}</td></tr>
            {% endfor %}
        </table>
    </body>
    </html>
    ''', hostname=hostname, request_headers_dict=request_headers_dict, response_headers_dict=response_headers_dict)


if __name__ == '__main__':
    app.run(debug=True)

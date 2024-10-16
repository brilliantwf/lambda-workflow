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
    headers_html = '<h1>Header信息V2</h1><ul>'
    for header, value in headers.items():
        headers_html += f'<li><strong>{header}:</strong> {value}</li>'
    headers_html += '</ul>'

    # 根据Header中Cloudfront-Viewer-Country 国家代码返回对应的国旗标志emoji
    if 'Cloudfront-Viewer-Country' in headers:
        country_code = headers['Cloudfront-Viewer-Country']
        if country_code == 'JP':
            headers_html += '<h2>Viewer From 🇯🇵</h2>'
        elif country_code == 'US':
            headers_html += '<h2>Viewer From 🇺🇸</h2>'
        else:
            headers_html += '<h2>Viewer From 🌍</h2>'
    
    # 将Header中Host信息添加到HTML中
    headers_html += f'<h2>Host: {headers["Host"]}</h2>'
    return headers_html

# 输出日志到stdout
app.logger.info.f(f'Request received: {request.headers}')
app.logger.flush()

if __name__ == '__main__':
    app.run(debug=True)

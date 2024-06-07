import logging
import sys
from flask import Flask, render_template

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
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

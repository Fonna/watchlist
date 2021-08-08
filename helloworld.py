# 导入flask
from flask import Flask

# 首先创建app对象
# 全局统一管理路由、配置信息和视图信息
# app = Flask(__name__)  # ->Flask(模块名字，字符类型)
app = Flask(
    __name__,
    static_url_path="/s",
    static_folder="static_files",
    template_folder="templates",
)


# 有了app这个抽象的对象后，就可以定义路由和视图
# 装饰器的作用是将路由器映射到视图函数index
# 此处是根目录
@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run()

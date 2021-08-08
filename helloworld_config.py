# 导入flask
from flask import Flask
import json


def create_app(config):
    """
    构建Flask对象的工厂模式
    """
    app = Flask(__name__, template_folder="templates", static_url_path="/s")
    app.config.from_object(config)
    app.config.from_envvar("PNKG", silent=True)
    return app


# 配置对象方式加载配置信息
class DefaultConfig(object):
    # 默认配置
    # 配置参数变量使用大写
    SECRET_KEY = "jingJING:QdfdfKG"


class DevelopConfig(DefaultConfig):
    # 默认配置
    # 配置参数变量使用大写
    DEBUG = True


# 首先创建app对象
# 全局统一管理路由、配置信息和视图信息
# app = Flask(__name__)  # ->Flask(模块名字，字符类型)
# app = Flask(__name__)


app = create_app(DefaultConfig)
# 设置配置参数
# app.config.from_object(DefaultConfig)
# app.config.from_pyfile("setting.py")
# app.config.from_envvar("PROJT_SET", silent=True)


# 有了app这个抽象的对象后，就可以定义路由和视图
# 装饰器的作用是将路由器映射到视图函数index
# 此处是根目录
@app.route("/", methods=["POST", "GET"])
def index():
    print(app.config["SECRET_KEY"])
    return "Hello World!"


print("*" * 30)
print(app.url_map)
print("*" * 30)
# app.url_map.iter_rules() -> 返回的是一个迭代器
# for rule in app.url_map.iter_rules():
#     print(f"路由名称是{rule.endpoint}，路由路径是{rule.rule}")


# @app.route("/")
# def route_map():
#     """[主视图，返回所有视图地址]"""
#     rules_iterator = app.url_map.iter_rules()
#     return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})


if __name__ == "__main__":
    # 运行flask提供的调试服务器
    # app.run(host, port, debug)
    # 在1.0版本后，Flask调整了开启服务器命令，可以不用app.run，而在命令行中使用flask run
    # flask run是读取flask_app的环境变量中的文件名来运行文件
    # 也可flask run -h host -p port指定端口等
    # app.run("0.0.0.0", 8000)
    app.run()

""""
app.py 程序主页
"""
from flask import Flask, render_template
from flask import escape, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import click

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.root_path, "data.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app


@app.route("/")
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template("index.html", user=user, movies=movies)


@app.route("/home")
@app.route("/index")
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route("/")
def hello_1():
    return "Welcome!"


@app.route("/user/<name>")
def user_page(name):
    return "User: %s" % escape(name)


@app.route("/test")
def test_url_for():
    # 下面是一些调用示例
    print(url_for("hello"))  # 输出：/

    print(url_for("user_page", name="fonna"))

    print(url_for("user_page", name="gabuli"))

    print(url_for("test_url_for"))

    print(url_for("test_url_for", num=2))
    return "Test page"


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
    name = "Grey Li"
    movies = [
        {"title": "My Neighbor Totoro", "year": "1988"},
        {"title": "Dead Poets Society", "year": "1989"},
        {"title": "A Perfect World", "year": "1993"},
        {"title": "Leon", "year": "1994"},
        {"title": "Mahjong", "year": "1996"},
        {"title": "Swallowtail Butterfly", "year": "1996"},
        {"title": "King of Comedy", "year": "1999"},
        {"title": "Devils on the Doorstep", "year": "1999"},
        {"title": "WALL-E", "year": "2008"},
        {"title": "The Pork of Music", "year": "2012"},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m["title"], year=m["year"])
        db.session.add(movie)

    db.session.commit()
    click.echo("Done.")


name = "Grey Li"
movies = [
    {"title": "My Neighbor Totoro", "year": "1988"},
    {"title": "Dead Poets Society", "year": "1989"},
    {"title": "A Perfect World", "year": "1993"},
    {"title": "Leon", "year": "1994"},
    {"title": "Mahjong", "year": "1996"},
    {"title": "Swallowtail Butterfly", "year": "1996"},
    {"title": "King of Comedy", "year": "1999"},
    {"title": "Devils on the Doorstep", "year": "1999"},
    {"title": "WALL-E", "year": "2008"},
    {"title": "The Pork of Music", "year": "2012"},
]

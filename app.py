""""
app.py 程序主页
"""
from flask import Flask
from flask import escape, url_for

app = Flask(__name__)

@app.route('/home')
@app.route('/index')
def hello():
	return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/')
def hello_1():
	return 'Welcome!'

@app.route('/user/<name>')
def user_page(name):
	return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
	# 下面是一些调用示例
	print(url_for('hello'))   # 输出：/

	print(url_for('user_page', name='fonna'))

	print(url_for('user_page', name='gabuli'))

	print(url_for('test_url_for'))

	print(url_for('test_url_for', num=2))
	return 'Test page'
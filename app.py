from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name

@app.route('/user/<name>/<tet>')
def user_pages(name,tet):
    return 'User: %s and tet: %s' %(name,tet)

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='abbb'))  # 输出：/user/greyli
    print(url_for('user_page', name='cddd'))  # 输出：/user/peter
    print(url_for('user_pages', name='abbb',tet='1111'))  # 输出：/user/greyli
    print(url_for('user_pages', name='cddd',tet='2222'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=3))  # 输出：/test?num=2
    return 'Test Page'


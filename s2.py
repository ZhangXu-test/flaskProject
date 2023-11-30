# -- coding: utf-8 --
# date：2023/11/29 10:32
# author: ZhangXu
import functools

from flask import Flask, render_template, jsonify, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'abc'

DATA_DICT = {
    1: {'name': 'aaa', 'age': 17},
    2: {'name': 'bbb', 'age': 18},
    3: {'name': 'ccc', 'age': 19}
}


def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        username = session.get('aaa')
        if not username:
            return redirect('/login')
        return func(*args, **kwargs)
    return inner


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'aaa' and pwd == 'bbb':
        session['aaa'] = 'aaa'
        return redirect('/index')
    error = '用户名或密码错误'
    return render_template('login.html', error= error)
    # return jsonify({'code': 1000, 'data': [1, 2, 3]})


@app.route('/index', endpoint='idx')
@auth
def index():
    data_dict = DATA_DICT
    return render_template('index.html', data_dict=data_dict)


@app.route('/index/edit', methods=['GET', 'POST'])
@auth
def index_edit():
    nid = int(request.args.get('nid'))
    if request.method == 'GET':
        info = DATA_DICT[nid]
        return render_template('edit.html', info=info)
    user = request.form.get('user')
    age = request.form.get('age')
    DATA_DICT[nid]['name'] = user
    DATA_DICT[nid]['age'] = age
    return redirect(url_for('idx'))


@app.route('/index/delete/<int:nid>')
@auth
def index_delete(nid):
    del DATA_DICT[nid]
    return redirect(url_for('idx'))


if __name__ == '__main__':
    app.run()

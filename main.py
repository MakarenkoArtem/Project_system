from os import listdir, remove, rmdir, mkdir, environ, path
from flask import Flask, render_template, request, redirect
from flask_restful import Api
from flask_login import LoginManager
from api.action_resource import ActionResource
from api.column_resource import ColumnResource
import datetime
import requests
from data import db_session
from data.values import Value
from data.columns import Column
from data.projects import Project

app = Flask(__name__)
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=1)
api = Api(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/', methods=['GET', 'POST'])
def none():  # форма для добавления таблицы
    name = ''
    error = ''
    db_sess = db_session.create_session()
    if request.method == 'POST':
        project = db_sess.query(Project).filter(Project.name == request.form['name']).all()
        if request.form["button"] == 'Open':
            if not len(project):
                name = request.form['name']
                error = 'Нет такой таблицы'
            else:
                return redirect('/' + str(project[0].id))
        else:
            if not len(project):
                project = Project(name=request.form['name'], author_id=-1, columns_id='')
                db_sess.add(project)
                db_sess.commit()
                return redirect('/' + str(project.id))
            else:
                name = request.form['name']
                error = 'Такая таблица уже есть'
    return render_template('none.html', name=name, error=error)


@app.route('/<int:table_id>', methods=['GET', 'POST'])
def test(table_id):  # форма для добавления теста
    db_sess = db_session.create_session()
    project = db_sess.query(Project).filter(Project.id == table_id).one()
    print(project)
    table = {}
    for column_id in project.columns_id.split():
        print(column_id)
        column = db_sess.query(Column).filter(Column.id == int(column_id)).one()
        table[column] = db_sess.query(Value).filter(Value.column_id == int(column_id)).all()
    print(table)

    # columns = db_sess.query(Column).filter(Column.project_id == project.id).all()
    # values = {i.id: db_sess.query(Value).filter(Value.column_id == i.id).all() for i in columns}
    # print(f"{request.scheme}://{request.server[0]}:{request.server[1]}/api/v1/action/2113")
    # requests.post(f"{request.scheme}://{request.server[0]}:{request.server[1]}/api/v1/action/2113",
    #              data={'action_id': 123, 'column_id': 1})
    # return redirect('/')
    return render_template('test1.html', project=project, table=table)
    # columns=columns,
    # actions=values)


@app.route('/test1', methods=['GET', 'POST'])
def test1():  # форма для добавления теста
    # return redirect('/')
    return render_template('test1.html', columns={1: "в ожидании", 2: 'в процессе', 3: 'завершено'},
                           actions=[{1: "создание дизайна", 2: 'создание бд', 3: 'создание запросов'}, {}, {}])


"""*********************Подключение API*******************************"""
api.add_resource(ActionResource, '/api/v1/action/<int:column_id>')
api.add_resource(ColumnResource, '/api/v1/column/<int:project_id>')
"""*******************************************************************"""


def main():
    db_session.global_init()
    if 'HEROKU' in environ:
        port = int(environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(port=8080, host='127.0.0.1', debug=False)


if __name__ == "__main__":
    main()
'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 2000))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()'''

from flask import Flask, render_template, request
from flask_restful import Api
from flask_login import LoginManager
from api.action_resource import ActionResource
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


@app.route('/<int:table_id>', methods=['GET', 'POST'])
def test(table_id):  # форма для добавления теста
    db_sess = db_session.create_session()
    test = db_sess.query(Project).filter(Project.id == table_id).one()
    print(test)
    print(vars(request))
    print(f"{request.scheme}://{request.server[0]}:{request.server[1]}/api/v1/action/2113")
    requests.post(f"{request.scheme}://{request.server[0]}:{request.server[1]}/api/v1/action/2113",
                  data={'action_id': 123, 'column_id': 1})
    # return redirect('/')
    return render_template('test.html', columns={1: "в ожидании", 2: 'в процессе', 3: 'завершено'},
                           actions={1: ["создание дизайна", 1], 2: ['создание бд', 1], 3: ['создание запросов', 1]})


@app.route('/test1', methods=['GET', 'POST'])
def test1():  # форма для добавления теста
    # return redirect('/')
    return render_template('test1.html', columns={1: "в ожидании", 2: 'в процессе', 3: 'завершено'},
                           actions=[{1: "создание дизайна", 2: 'создание бд', 3: 'создание запросов'}, {}, {}])


"""*********************Подключение API*******************************"""
api.add_resource(ActionResource, '/api/v1/action/<table_id>')
"""*******************************************************************"""



def main():
    db_session.global_init()
    app.run(port=8080, host='127.0.0.11', debug=False)


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

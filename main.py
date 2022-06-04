from flask import Flask, render_template, redirect, request, session
from flask_restful import Api
from flask_login import LoginManager, current_user, login_user
from api.action_resource import ActionResource
import datetime
import requests

app = Flask(__name__)
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=1)
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/<int:table_id>', methods=['GET', 'POST'])
def test(table_id):  # форма для добавления теста
    print(vars(request))
    requests.post(f"{request.scheme}://{request.server[0]}:{request.server[1]}/api/v1/action/2113", data={'action_id':123, 'column_id':1})
    # return redirect('/')
    return render_template('test.html')


@app.route('/test1', methods=['GET', 'POST'])
def test1():  # форма для добавления теста
    # return redirect('/')
    return render_template('test1.html')


"""*********************Подключение API*******************************"""
api.add_resource(ActionResource, '/api/v1/action/<int:table_id>')
"""*******************************************************************"""


def main():
    app.run(port=8080, host='127.0.0.11', debug=False)


if __name__ == "__main__":
    main()

from flask_restful import Resource, abort, url_for, reqparse
from flask import jsonify

# from data import db_session
# from data.lessons import Lesson
from fuzzywuzzy import fuzz

parser = reqparse.RequestParser()
parser.add_argument('action_id', required=False)
parser.add_argument('column_id', required=False)

'''def abort_if_lessons_not_found(lesson_id):
    session = db_session.create_session()
    lesson = session.query(Lesson).get(lesson_id)
    if not lesson:
        abort(404, message=f"Lesson {lesson_id} not found")
    return lesson

def abort_if_title_lessons_not_found(lesson_title):
    session = db_session.create_session()
    lesson = None
    for i in session.query(Lesson).all():
        print("!!!!!", i.title)
        print("-".join(i.title.split()).lower(), lesson_title)
    s = [[fuzz.ratio("-".join(i.title.split()).lower(), lesson_title), i] for i in session.query(Lesson).all()]
    s.sort(reverse=True)
    print(s)
    if s[0][0] > 90:
        lesson = s[0][1]
    if not lesson:
        abort(404, message=f"Lesson {lesson_title} not found")
    return lesson
'''

class ActionResource(Resource):
    def __init__(self):
        print(23)
    def post(self, table_id):
        args = parser.parse_args()
        print(table_id)
        print(args['action_id'], args['column_id'])
        return jsonify({'success': 'OK'})

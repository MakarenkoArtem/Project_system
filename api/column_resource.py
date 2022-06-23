from flask_restful import Resource, abort, url_for, reqparse
from flask import jsonify
from data import db_session, columns, projects, columns
from fuzzywuzzy import fuzz

parser = reqparse.RequestParser()
parser.add_argument('id', required=False)
parser.add_argument('pos', required=False)
parser.add_argument('name', required=False)

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


class ColumnResource(Resource):
    def put(self, project_id):
        args = parser.parse_args()
        id, pos = args['id'], int(args['pos']) - 1
        db_sess = db_session.create_session()
        project = db_sess.query(projects.Project).filter(projects.Project.id == project_id).one()
        cols = [i for i in project.columns_id.split() if i != id]
        cols = cols[:pos] + [id] + cols[pos:]
        project.columns_id = " ".join(cols)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def post(self, project_id):
        args = parser.parse_args()
        name = args['name']
        db_sess = db_session.create_session()
        column = columns.Column(name=name, project_id=project_id)
        db_sess.add(column)
        db_sess.commit()
        project = db_sess.query(projects.Project).filter(projects.Project.id == project_id).one()
        project.columns_id += ' ' + str(column.id)
        # db_sess.add(project)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def delete(self, project_id):
        args = parser.parse_args()
        id = args['id']
        db_sess = db_session.create_session()
        project = db_sess.query(projects.Project).filter(projects.Project.id == project_id).one()
        cols = [i for i in project.columns_id.split() if i != str(id)]
        project.columns_id = " ".join(cols)
        db_sess.delete(db_sess.query(columns.Column).filter(columns.Column.id == id).one())
        db_sess.commit()
        return jsonify({'success': 'OK'})

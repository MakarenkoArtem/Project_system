import sqlalchemy
from werkzeug.security import check_password_hash, generate_password_hash
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class Value(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'values'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    column_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('columns.id'), nullable=True)

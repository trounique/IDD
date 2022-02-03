import os
from app import db
from sqlalchemy import func
from datetime import datetime


class Result(db.Model):
    __tablename__ = 'results'  # 定义数据库表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date = db.Column(db.String(100))

    def __repr__(self):
        return '<Result ID=%r>' % self.id


def pre_process(data_path):
    file_name = os.path.split(data_path)[1].split('.')[0]  # 没有后缀的文件名
    return data_path, file_name


def result_max_id():
    result = db.session.query(func.count(Result.id)).scalar()
    return result


def result_add_file(list_data):
    id = result_max_id() + 1
    name = list_data[0]
    date = list_data[1]
    new_results = Result(id=id, name=name, date=date)
    db.session.add(new_results)
    db.session.commit()


def result_query_history():
    results = Result.query.all()
    table_list = []
    for things in results:
        list_thing = [things.id, things.date, things.name]
        table_list.append(list_thing)
    print(table_list)
    print('1')
    return table_list

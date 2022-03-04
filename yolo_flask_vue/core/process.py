import os
from app import db
from sqlalchemy import func
import datetime
import time


class Result(db.Model):
    __tablename__ = 'results'  # 定义数据库表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date = db.Column(db.String(100))
    date_check = db.Column(db.String(100))
    mainboard_good = db.Column(db.String(100))
    interface_good = db.Column(db.String(100))
    mainboard_lack = db.Column(db.String(100))
    interface_lack = db.Column(db.String(100))
    fan_good = db.Column(db.String(100))
    fan_lack = db.Column(db.String(100))

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
    mainboard_good = list_data[2]
    mainboard_lack = list_data[3]
    fan_good = list_data[4]
    fan_lack = list_data[5]
    interface_good = list_data[6]
    interface_lack = list_data[7]
    dt_strf_check = list_data[8]
    new_results = Result(id=id, name=name, date=date, mainboard_good=mainboard_good, mainboard_lack=mainboard_lack,
                         fan_good=fan_good, fan_lack=fan_lack, interface_good=interface_good,
                         interface_lack=interface_lack, date_check=dt_strf_check)
    db.session.add(new_results)
    db.session.commit()


def result_query_history():
    results = Result.query.all()
    table_list = []
    for things in results:
        list_thing = [things.id, things.date, things.name, things.mainboard_good, things.mainboard_lack,
                      things.interface_good, things.interface_lack, things.fan_good, things.fan_lack]
        table_list.append(list_thing)
    return table_list


def result_query_bar_chart_history():
    dt_seven_day = []
    dt_strf_today = time.strftime("%Y-%m-%d", time.localtime())
    dt_seven_day.append(dt_strf_today)
    result_data = []
    result_today = Result.query.filter_by(date_check=dt_strf_today).all()
    result_data.append(result_today)
    mainboard_lack_data = []
    fan_lack_data = []
    interface_lack_data = []
    for i in range(1, 7):
        dt_strf = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        # delta = datetime.timedelta(days=i)
        # now = datetime.datetime.now()
        # dt = now - delta
        # dt_time = time.mktime(dt.timetuple())
        # dt_strf = time.strftime("%Y-%m-%d", dt_time)
        dt_seven_day.append(dt_strf)
    xAxis_data = dt_seven_day
    for i in range(1, 7):
        result_last = Result.query.filter_by(date_check=xAxis_data[i]).all()
        result_data.append(result_last)
    for i in range(0, 7):
        mainboard_lack_count = 0
        fan_lack_count = 0
        interface_lack_count = 0
        for things in result_data[i]:
            mainboard_lack_count = mainboard_lack_count + int(things.mainboard_lack)
            fan_lack_count = fan_lack_count + int(things.fan_lack)
            interface_lack_count = interface_lack_count + int(things.interface_lack)
        mainboard_lack_data.append(mainboard_lack_count)
        fan_lack_data.append(fan_lack_count)
        interface_lack_data.append(interface_lack_count)
    list_data = [mainboard_lack_data, fan_lack_data, interface_lack_data, xAxis_data]
    return list_data


def result_query_bar_chart_history():
    dt_seven_day = []
    dt_strf_today = time.strftime("%Y-%m-%d", time.localtime())
    dt_seven_day.append(dt_strf_today)
    result_data = []
    result_today = Result.query.filter_by(date_check=dt_strf_today).all()
    result_data.append(result_today)
    mainboard_lack_data = []
    fan_lack_data = []
    interface_lack_data = []
    for i in range(1, 7):
        dt_strf = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        # delta = datetime.timedelta(days=i)
        # now = datetime.datetime.now()
        # dt = now - delta
        # dt_time = time.mktime(dt.timetuple())
        # dt_strf = time.strftime("%Y-%m-%d", dt_time)
        dt_seven_day.append(dt_strf)
    xAxis_data = dt_seven_day
    for i in range(1, 7):
        result_last = Result.query.filter_by(date_check=xAxis_data[i]).all()
        result_data.append(result_last)
    for i in range(0, 7):
        mainboard_lack_count = 0
        fan_lack_count = 0
        interface_lack_count = 0
        for things in result_data[i]:
            mainboard_lack_count = mainboard_lack_count + int(things.mainboard_lack)
            fan_lack_count = fan_lack_count + int(things.fan_lack)
            interface_lack_count = interface_lack_count + int(things.interface_lack)
        mainboard_lack_data.append(mainboard_lack_count)
        fan_lack_data.append(fan_lack_count)
        interface_lack_data.append(interface_lack_count)
    list_data = [mainboard_lack_data, fan_lack_data, interface_lack_data, xAxis_data]
    return list_data


def result_query_line_chart_history():
    dt_30_day = []
    dt_strf_now = time.strftime("%Y-%m-%d", time.localtime())
    dt_30_day.append(dt_strf_now)
    result_data = []
    result_today = Result.query.filter_by(date_check=dt_strf_now).all()
    result_data.append(result_today)
    mainboard_lack_data = []
    fan_lack_data = []
    interface_lack_data = []
    for i in range(1, 30):
        dt_strf = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        # delta = datetime.timedelta(days=i)
        # now = datetime.datetime.now()
        # dt = now - delta
        # dt_time = time.mktime(dt.timetuple())
        # dt_strf = time.strftime("%Y-%m-%d", dt_time)
        dt_30_day.append(dt_strf)
    xAxis_data = dt_30_day
    for i in range(1, 30):
        result_last = Result.query.filter_by(date_check=xAxis_data[i]).all()
        result_data.append(result_last)
    for i in range(0, 30):
        mainboard_lack_count = 0
        fan_lack_count = 0
        interface_lack_count = 0
        for things in result_data[i]:
            mainboard_lack_count = mainboard_lack_count + int(things.mainboard_lack)
            fan_lack_count = fan_lack_count + int(things.fan_lack)
            interface_lack_count = interface_lack_count + int(things.interface_lack)
        mainboard_lack_data.append(mainboard_lack_count)
        fan_lack_data.append(fan_lack_count)
        interface_lack_data.append(interface_lack_count)
    list_data = [mainboard_lack_data, fan_lack_data, interface_lack_data, xAxis_data]
    return list_data

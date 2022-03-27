from datetime import date
import logging as rel_log
import os
import shutil
from datetime import timedelta
from flask import *
from processor.AIDetector_pytorch import Detector
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import core.main
from core.process import *
import time

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = r'./uploads'
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'secret!'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

ALLOWED_EXTENSIONS = {'png', 'jpg'}

werkzeug_logger = rel_log.getLogger('werkzeug')
werkzeug_logger.setLevel(rel_log.ERROR)

# 解决缓存刷新问题.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


# 添加header解决跨域
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return redirect(url_for('static', filename='./index.html'))


@app.route("/api/query/all", methods=['GET', 'POST'])
def query_all():
    res_list = result_query_history()
    data_array = []
    srcList = []
    for i in range(len(res_list)):
        tmp_list = ['http://127.0.0.1:5003/tmp/draw/' + res_list[i][2]]
        srcList.append(tmp_list)
        data_obj = {"id": res_list[i][0], "date": res_list[i][1], "name": res_list[i][2],
                    "mainboard_good": res_list[i][3], "interface_good": res_list[i][4],
                    "mainboard_lack": res_list[i][5], "interface_lack": res_list[i][6],
                    "fan_good": res_list[i][7], "fan_lack": res_list[i][8],
                    "draw_url": 'http://127.0.0.1:5003/tmp/draw/' + res_list[i][2],
                    "qval": res_list[i][9], "flexible": res_list[i][10]
                    }
        data_array.append(data_obj)
    return jsonify(msg="success", infor="获取成功", list=data_array, srcList=srcList)


@app.route("/api/pie_chart", methods=['GET', 'POST'])
def pie_chart():
    res_list = result_query_history()
    mainboard_lack = 0
    fan_lack = 0
    interface_lack = 0
    flexible = 0
    for i in range(len(res_list)):
        mainboard_lack = mainboard_lack + int(res_list[i][5])
        interface_lack = interface_lack + int(res_list[i][6])
        fan_lack = fan_lack + int(res_list[i][8])
        flexible = flexible + int(res_list[i][10])
    lack_data = [{"value": mainboard_lack, "name": "主板螺丝缺失"}, {"value": fan_lack, "name": "风扇螺丝缺失"},
                 {"value": interface_lack, "name": "接口未接上"}, {"value": flexible, "name": "螺丝松动"}]
    return jsonify(msg="success", infor="获取成功", lack_data=lack_data)


@app.route("/api/bar_chart", methods=['GET', 'POST'])
def bar_chart():
    list_data = result_query_bar_chart_history()
    mainboard_lack_data = list_data[0]
    fan_lack_data = list_data[1]
    interface_lack_data = list_data[2]
    xAxis_data = list_data[3]
    flexible_data = list_data[4]
    return jsonify(msg="success", infor="获取成功", mainboard_lack_data=mainboard_lack_data, fan_lack_data=fan_lack_data,
                   interface_lack_data=interface_lack_data, xAxis_data=xAxis_data, flexible_data=flexible_data)


@app.route("/api/line_chart", methods=['GET', 'POST'])
def line_chart():
    list_data = result_query_line_chart_history()
    mainboard_lack_data = list_data[0]
    fan_lack_data = list_data[1]
    interface_lack_data = list_data[2]
    xAxis_data = list_data[3]
    flexible_data = list_data[4]
    return jsonify(msg="success", infor="获取成功", mainboard_lack_data=mainboard_lack_data, fan_lack_data=fan_lack_data,
                   interface_lack_data=interface_lack_data, xAxis_data=xAxis_data, flexible_data=flexible_data)


@app.route("/api/qval_chart", methods=['GET', 'POST'])
def qval_chart():
    list_data = result_query_qval_chart_history()
    xAxis_data = list_data[0]
    qval_data = list_data[1]
    return jsonify(msg="success", infor="获取成功", xAxis_data=xAxis_data, qval_data=qval_data)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    qval = ''
    file = request.files['file']
    # dt = datetime.datetime.now()
    if file and allowed_file(file.filename):
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_path)
        shutil.copy(src_path, './tmp/ct')
        image_path = os.path.join('./tmp/ct', file.filename)
        pid, image_info = core.main.c_main(
            image_path, current_app.model, file.filename.rsplit('.', 1)[1])
        # dt_strf = dt.strftime("%Y-%m-%d")
        dt_strf = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        dt_strf_check = time.strftime("%Y-%m-%d", time.localtime())
        image_keys = list(image_info.keys())
        mainboard_good = 0
        mainboard_lack = 0
        fan_good = 0
        fan_lack = 0
        interface_good = 0
        interface_lack = 0
        flexible = 0
        for name in image_keys:
            if name[:14] == 'mainboard_good':
                mainboard_good = mainboard_good + 1
            if name[:14] == 'mainboard_lack':
                mainboard_lack = mainboard_lack + 1
            if name[:8] == 'fan_good':
                fan_good = fan_good + 1
            if name[:8] == 'fan_lack':
                fan_lack = fan_lack + 1
            if name[:14] == 'interface_good':
                interface_good = interface_good + 1
            if name[:14] == 'interface_lack':
                interface_lack = interface_lack + 1
        if (mainboard_lack == 0) & (fan_lack == 0) & (interface_lack == 0):
            qval = '螺丝安装合格'
        else:
            qval = '螺丝安装不合格'
        list_data = [pid, dt_strf, mainboard_good, mainboard_lack, fan_good, fan_lack, interface_good, interface_lack,
                     dt_strf_check, qval, flexible]
        result_add_file(list_data)
        num_list = []
        list_name = ['主板螺丝完好数目', '主板螺丝缺失数目', '风扇螺丝完好数目', '风扇螺丝缺失数目', '接口正确接上数目', '接口没有接上数目', '螺丝松动数目']
        for i in range(len(list_name)):
            data_obj = {"name": list_name[i], "num": list_data[i + 2]}
            num_list.append(data_obj)
        return jsonify({'status': 1,
                        'image_url': 'http://127.0.0.1:5003/tmp/ct/' + pid,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid,
                        'image_info': image_info,
                        'num_list': num_list,
                        'qval': qval}
                       )

    return jsonify({'status': 0})


@app.route("/download", methods=['GET'])
def download_file():
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)..
    return send_from_directory('data', 'testfile.zip', as_attachment=True)


# show photo
@app.route('/tmp/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        if not file is None:
            image_data = open(f'tmp/{file}', "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response


if __name__ == '__main__':
    files = [
        'uploads', 'tmp/ct', 'tmp/draw',
        'tmp/image', 'tmp/mask', 'tmp/uploads'
    ]
    for ff in files:
        if not os.path.exists(ff):
            os.makedirs(ff)
    with app.app_context():
        current_app.model = Detector()
    app.run(host='127.0.0.1', port=5003, debug=True)

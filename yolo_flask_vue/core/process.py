import os


def pre_process(data_path):
    file_name = os.path.split(data_path)[1].split('.')[0]  # 没有后缀的文件名
    return data_path, file_name

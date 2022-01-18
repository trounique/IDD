import cv2
import numpy as np
from PIL import Image


def predict(dataset, model, ext):
    global img_y
    x = dataset[0].replace('\\', '/')
    # x = dataset[0]
    file_name = dataset[1]
    print(x)
    print(file_name)
    x = cv2.imread(x)
    # x = Image.open(x).convert('RGB')
    # x = np.array(x)
    img_y, image_info = model.detect(x)
    cv2.imwrite('./tmp/draw/{}.{}'.format(file_name, ext), img_y)
    # raise Exception('保存图片时出错.Error saving thepicture.')
    return image_info

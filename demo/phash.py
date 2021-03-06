import cv2
import numpy as  np
from compiler.ast import flatten
import sys


def pHash(imgfile):
    '''
    get image phash value
    :param imgfile:
    :return:
    '''

    img = cv2.imread(imgfile, 0)
    img = cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)

    # 创建二维列表
    h, w = img.shape[:2]
    vis0 = np.zeros((h, w), np.float32)
    # 填充数据
    vis0[:h, :w] = img

    # 二维Dct变换
    vis1 = cv2.dct(cv2.dct(vis0))
    vis1.resize(32, 32)

    # 把二维list变成一维list
    img_list = flatten(vis1.tolist())

    # 计算均值
    avg = sum(img_list) * 1. / len(img_list)
    avg_list = ['0' if i < avg else '1' for i in img_list]

    # 得到哈希值
    return ''.join(['%x' % int(''.join(avg_list[x:x + 4]), 2) for x in range(0, 32 * 32, 4)])

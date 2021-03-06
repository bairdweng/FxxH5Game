import random
import json


# 获取随机字符串。0 随机，1大写，-1小写
def getRandomStrWithOption(length, option):
    seed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(length):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    if option == -1:
        return salt.lower()
    elif option == 1:
        return salt.upper()
    else:
        return salt


# 计算机随机字符串。
def getJsonFileRandomString():
    with open('./temple/dc.json', 'r') as f:
        list = json.loads(f.read())
        index = random.randint(0, len(list) - 1)

    return list[index]


def getiOSGjz():
    list = ['Model',
            'View',
            'TableView',
            'ViewController',
            'TableViewController',
            'TableViewCell',
            'CollectionViewController',
            'CollectionViewCell',
            'ReusableView',
            'Animation',
            'AnimationGroup',
            'BasicAnimation',
            'DisplayLink',
            'EAGLLayer',
            'EmitterCell',
            'EmitterLayer',
            'GradientLayer',
            'ElementQuery',
            'Resource',
            'Request',
            'Management',
            'Screenshot',
            'SiriService',
            'DrawingContext',
            'Label',
            'KeyframeAnimation',
            'MediaTimingFunction',
            'ReplicatorLayer',
            'ScrollLayer',
            'ColorKernel',
            'DataMatrixCodeDescriptor',
            'Detector',
            'FaceFeature',
            'Feature',
            'FilterShape',
            'Screen']
    index = random.randint(0, len(list) - 1)
    return list[index]

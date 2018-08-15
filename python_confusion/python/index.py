#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
import InstercodeTofunction
# import variableconfusion
import InstercodeToFile
import helper
import shutil
import Packaging

# from start import VariableConfusion

# 需要处理的工程目录。

ys_pro_dir = '../iOS_Product/PGPlatFormSDK'

pro_root_dir = ''

# pro_root_dir = '../iOS_Product/MJProduct/DSDKsiPFfeAmf/DSDKsiPFfeAmf/Mains/GameSDK/MainFunction/'
# pro_root_dir = '../iOS_Product/HunXiao'
# 前缀。
pro_qz_str = helper.getRandomStrWithOption(2, -1).upper()

# 过滤的类。
filterClassNames = ['AppDelegate', 'ViewController']

# 过滤的目录。
filterClassDirs = ['AFNetworking',
                   'Helper'
                   'Base64',
                   'MJCSMassonry',
                   'MJFDFullscreenPopGesture',
                   'MJSVProgressHUD',
                   'NJKWebViewProgress',
                   'Reachability']

# 过滤的目录，页游平台手游SDK版
filterClassDirs = ['PGFIQKKeyboardManager',
                   'PGPFSVProgressHUD',
                   'Base64',
                   'IOPSAFFNetworking',
                   'SBJson',
                   'SSXMMasonry',
                   'Header']

filterClassDirs = ['PGFIQKKeyboardManager',
                   'SSXMMasonry',
                   'IOPSAFFNetworking',
                   'SBJson',
                   'Header']


def getClassName():
    zj = helper.getJsonFileRandomString().lower().capitalize() + helper.getJsonFileRandomString().lower().capitalize()
    hz = helper.getRandomStrWithOption(2, -1).capitalize()

    iosGjz = helper.getiOSGjz()

    return pro_qz_str + zj + hz + iosGjz


def getPathLastDir(path):
    s_dirs = path.split('/')
    last_dir = s_dirs[len(s_dirs) - 1]
    return last_dir


def start(rootDir):

    global pro_root_dir
    if (os.path.exists(rootDir) == False):
        return
    new_dir = '../templeDir/'
    if (os.path.exists(new_dir)):
        shutil.rmtree(new_dir)

    os.makedirs(new_dir)
    last_dir = getPathLastDir(rootDir)
    shutil.copytree(rootDir, '../templeDir/' + last_dir)

    pro_root_dir = '../templeDir/' + last_dir + '/'

    start2(pro_root_dir)

    newSDKName = helper.getRandomStrWithOption(4, 1) + 'SDK'

    changeFrameWorkName('PGSDK', newSDKName)
    changeBundleName(newSDKName)
    changeSDKFeference(pro_root_dir, 'PGSDK', newSDKName)
    # 打包SDK。
    Packaging.start(pro_root_dir, newSDKName)

    # 归档。

    print('==========执行完毕')


def start2(rootDir):
    if (os.path.exists(rootDir) == False):
        return
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isfile(pathname)):
            if '.h' in filename or '.swift' in filename:
                # 过滤器处理
                isNext = True
                for fix in filterClassNames:
                    if filename == fix + '.h':
                        isNext = False

                if '+' in filename:
                    isNext = False
                rootDir = os.path.dirname(pathname)
                last_dir = getPathLastDir(rootDir)
                for dir in filterClassDirs:
                    if dir == last_dir:
                        isNext = False

                if isNext == False:
                    continue

                oldFileName = filename.replace('.h', '')
                oldFileName = oldFileName.replace('.swift', '')

                newFileName = getClassName()

                # newFileName = oldFileName

                # 更改类名。
                changeClassName(pathname, oldFileName, newFileName)

                # 更改工程。
                changeXcodepro(getXcodeprojPath(pro_root_dir), oldFileName, newFileName)
                # 更改其它类的调用。
                changeFeference(pro_root_dir, oldFileName, newFileName)

                classPath = rootDir + '/' + newFileName + '.m'

                # 往函数插入代码。
                InstercodeTofunction.start(classPath)

                # 往类插入代码
                InstercodeToFile.start(classPath)


        else:
            start2(pathname)


# 更改类名。
def changeClassName(pathname, oldFileName, newFileName):
    # 根目录
    rootDir = os.path.dirname(pathname)
    # 过滤点m。
    # oldFileName = filename.replace('.h', '')
    # newFileName = getClassName()

    oldPath = rootDir + '/' + oldFileName
    newPath = rootDir + '/' + newFileName
    if os.path.exists(oldPath + '.h'):
        os.rename(oldPath + '.h', newPath + '.h')
    if os.path.exists(oldPath + '.m'):
        os.rename(oldPath + '.m', newPath + '.m')
    if os.path.exists(oldPath + '.swift'):
        os.rename(oldPath + '.swift', newPath + '.swift')


def changeFrameWorkName(oldName, newname):
    proj_path = getXcodeprojPath(pro_root_dir)
    with open(proj_path, "r", encoding="utf-8") as f:
        xcontent = f.read()
        xcontent = re.sub(r'\b' + oldName + r'\b', newname, xcontent)
        print('更改:' + oldName + '------------>' + newname)
    with open(proj_path, "w", encoding="utf-8") as f:
        f.write(xcontent)


def changeBundleName(newname):
    bundlePath = pro_root_dir + 'DataSources/PGSDK.bundle'
    newbundlePath = pro_root_dir + 'DataSources/' + newname + '.bundle'
    for file in os.listdir(bundlePath):
        path = bundlePath + '/' + file
        with open(path, 'rb') as f:
            image_data = f.read()
        str = helper.getRandomStrWithOption(100, -1)
        new_image_data = image_data + bytes(str, 'utf-8')
        with open(path, 'wb') as f:
            f.write(new_image_data)
        newPath = bundlePath + '/' + helper.getRandomStrWithOption(10, -1) + file
        os.rename(path, newPath)

    os.rename(bundlePath, newbundlePath)


def changeSDKFeference(rootDir, oldName, newName):
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isfile(pathname)):
            if ('.h' in pathname) or ('.m' in pathname) or ('.pch' in pathname):
                with open(pathname, "r", encoding="utf-8") as f:
                    content = f.read()
                    content = re.sub(r'\b' + oldName + r'\b', newName, content)
                with open(pathname, "w", encoding="utf-8") as f:
                    f.write(content)
        else:
            changeSDKFeference(pathname, oldName, newName)


def changeXcodepro(proj_path, oldName, newName):
    with open(proj_path, "r", encoding="utf-8") as f:
        xcontent = f.read()
        xcontent = re.sub(r'\b' + oldName + r'.h\b', newName + '.h', xcontent)
        xcontent = re.sub(r'\b' + oldName + r'.m\b', newName + '.m', xcontent)
        xcontent = re.sub(r'\b' + oldName + r'.swift\b', newName + '.swift', xcontent)
        print('混淆:' + oldName + '------------>' + newName)
    with open(proj_path, "w", encoding="utf-8") as f:
        f.write(xcontent)


# 更改工程其它类的引用。
def changeFeference(rootDir, oldName, newName):
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isfile(pathname)):
            if ('.h' in pathname) or ('.m' in pathname) or ('.pch' in pathname) or ('.swift' in pathname):
                content = ""
                with open(pathname, "r", encoding="utf-8") as f:
                    content = f.read()
                    content = re.sub(r'\b' + oldName + r'\b', newName, content)
                    content = re.sub(r'\b' + oldName + '.h"' + r'\b', '"' + newName + '.h"', content)
                with open(pathname, "w", encoding="utf-8") as f:
                    f.write(content)
        else:
            changeFeference(pathname, oldName, newName)


# 获取xcodeproj路径。
def getXcodeprojPath(rootDir):
    x_path = ""
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if '.xcodeproj' in pathname:
            x_path = pathname

    if (len(x_path) > 0):
        x_path = x_path + '/project.pbxproj'
    return x_path


start(ys_pro_dir)

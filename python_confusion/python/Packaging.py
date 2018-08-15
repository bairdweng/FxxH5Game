#!/usr/bin/python
# -*- coding: UTF-8 -*-
import shutil
import os
import datetime
import zipfile


def start(pro_root_dir, newSDKName):
    # 导出SDK。
    os.system('xcodebuild -project '
              + pro_root_dir + 'PGPlatFormSDK.xcodeproj'
              + ' -scheme ' + newSDKName
              + ' clean build'
              + ' SYMROOT=../SDK | xcpretty')

    # 删除Debug-iphoneos
    shutil.move('../templeDir/SDK/Debug-iphoneos/' + newSDKName + '.framework',
                '../templeDir/SDK/' + newSDKName + '.framework')
    # 删除Debug-iphoneos
    os.rmdir('../templeDir/SDK/Debug-iphoneos')
    # 复制资源文件bundle
    shutil.copytree(pro_root_dir + 'DataSources/' + newSDKName + '.bundle',
                    '../templeDir/SDK/' + newSDKName + '.bundle')

    new_zip_name = datetime.datetime.now().strftime('%m%d_%H%M') + '_SDK.zip'
    # 压缩文件夹
    zip_dir(pro_root_dir + '../SDK', pro_root_dir + '../' + new_zip_name)

    # 移动到归档
    shutil.move('../templeDir/' + new_zip_name, '../TheArchive/' + new_zip_name)


def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for dir in dirs:
                filelist.append(os.path.join(root, dir))
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        # print arcname
        zf.write(tar, arcname)
    zf.close()

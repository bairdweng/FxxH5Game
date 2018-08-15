# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os

import re

import helper


def start2(path):
    if (os.path.exists(path) == False):
        return
    with open(path, 'r', encoding="utf-8") as f:
        content = f.read()
        # 查找变量
        pattern = re.compile(r'\*[a-zA-Z]+')
        list = pattern.findall(content)
        fix_list = []
        for element in list:
            if (element not in fix_list):
                element = element.replace('*', '')

                fix_strs = ['alloc', 'const', 'data', 'new', 'class', 'error', 'infoDictionary']
                isOk = True
                for str in fix_strs:
                    if str in element:
                        isOk = False
                # 过滤关键字。
                if len(element) < 4:
                    isOk = False
                if isOk:
                    fix_list.append(element)
        new_content = content
        for l in fix_list:
            # 新属性
            new_l = helper.getRandomStrWithOption(10, -1)
            l_list = new_content.split('\n')

            t_content = ''
            for ll in l_list:
                if l in ll:
                    ll = fixis_funtion(l, new_l, ll)
                t_content = t_content + ll + '\n'
            new_content = t_content

        # 写入
        with open(path, 'w', encoding="utf-8") as f:
            f.write(new_content)


# 过滤关键字
def fix_gjz(list):
    fix_list = []
    for element in list:
        if (element not in fix_list):
            element = element.replace('*', '')

            fix_strs = ['alloc', 'const', 'data', 'new', 'class','error', 'infoDictionary']
            isOk = True
            for str in fix_strs:
                if str in element:
                    isOk = False
            # 过滤关键字。
            if len(element) < 4:
                isOk = False
            if isOk:
                fix_list.append(element)
    return fix_list


def start(path):
    if (os.path.exists(path) == False):
        return
    with open(path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        # print(lines)
        content = ''
        isOK = False

        t_list = []
        n_str_list = []
        for i in range(0, len(lines), 1):
            # print(l)
            # 函数开头。
            l = lines[i]
            if '-' in l and '(' in l and ')' in l and '{' in l:
                isOK = True
            if '}' in l:
                # 往下找
                isHas = False
                for k in range(i + 1, len(lines), 1):
                    k_str = lines[k]
                    if ('-' in k_str or '+' in k_str) and '(' in k_str and ')' in k_str:
                        isHas = True
                    if '{' in k_str or '}' in k_str or '@end' in k_str:
                        break
                if isHas:
                    t_list = []
                    n_str_list = []
                    isOK = False

            if isOK:
                pattern = re.compile(r'\*[a-zA-Z]+')
                ls = pattern.findall(l)
                # print('ls====',ls)

                gjz = fix_gjz(ls)
                if len(gjz) > 0:
                    t_list.append(gjz[0])
                    n_str_list.append(helper.getRandomStrWithOption(4, -1))

                if len(t_list) > 0:

                    for i in range(0, len(t_list), 1):
                        old_str = t_list[i]
                        new_str = n_str_list[i]
                        # l = re.sub(r'\b' + old_str + r'\b', new_str, l)
                        l = fixis_funtion(old_str, new_str, l)
                    # print(t_list)
                    # print(n_str_list)

            content = content + l

            # 写入
            with open(path, 'w', encoding="utf-8") as f:
                f.write(content)
            # print(content)


def fixis_funtion(old_str, new_str, content_str):
    ary = content_str.split(":")
    # 临时字符串
    t_ll = ""
    if len(ary) > 1:
        for i in range(0, len(ary), 1):
            str = ary[i]
            # 如果不是以关键词结尾，说明可以替换。
            if not str.endswith(old_str):
                str = fixis_point_self(old_str, new_str, str)
            # 不是最后一个需要加：
            if i != len(ary) - 1:
                t_ll = t_ll + str + ':'
            else:
                t_ll = t_ll + str
        ll = t_ll
    else:
        ll = fixis_point_self(old_str, new_str, content_str)
    return ll


# 判断变量是否是其它类的引用。
def fixis_point_self(old_str, new_str, content_str):
    content_str = re.sub(r'\b' + old_str + r'\b', new_str, content_str)
    return content_str

    # ary = content_str.split('.')
    # if len(ary) > 1:
    #     t_str = ''
    #     for i in range(0, len(ary), 1):
    #         isOK = True
    #         ary_str = ary[i]
    #
    #         if old_str in ary_str and i > 0:
    #             # 匹配到的上一个是不是self，是的话才匹配。
    #             last_str = ary[i - 1]
    #             if last_str != 'self':
    #                 isOK = False
    #         if isOK:
    #             ary_str = re.sub(r'\b' + old_str + r'\b', new_str, ary_str)
    #
    #         if i != len(ary) - 1:
    #             t_str = t_str + ary_str + '.'
    #         else:
    #             t_str = t_str + ary_str
    #
    #     content_str = t_str
    # else:
    #     content_str = re.sub(r'\b' + old_str + r'\b', new_str, content_str)
    #
    # return content_str

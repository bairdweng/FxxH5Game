
import os
import helper
# 插入代码到函数。
def start(path):
    if (os.path.exists(path) == False):
        return

    with open(path, 'r', encoding="utf-8") as f:
        list = f.readlines()
        needInserts = []
        for l in range(0, len(list), 1):
            l_str = list[l]
            if ('}' in l_str) and ('//' in l_str) == False and (';' in l_str) == False and ('/*' in l_str) == False:
                # 往下走看是否有函数名。
                # print(l+1, l_str)
                isHas = False
                for k in range(l + 1, len(list), 1):
                    k_str = list[k]
                    if ('-' in k_str or '+' in k_str) and '(' in k_str and ')' in k_str:
                        isHas = True

                    if '{' in k_str or '}' in k_str or '@end' in k_str:
                        break

                # continue
                if isHas == True:
                    # 往回查找看是否有return。
                    # return所在的行数
                    return_line = 0
                    isR = False
                    isIm_p = False
                    for s in range(l, -1, -1):
                        l_str = list[s]
                        if 'return' in l_str and ('//' in l_str) == False and ('/*' in l_str) == False and (
                                '*/' in l_str) == False:
                            isR = True
                            # return_line = s

                        # 判断是否有 @implementation 有的话不插入。
                        if '@implementation' in l_str:
                            isIm_p = True

                        if '{' in l_str:
                            break
                    # 是否有注释
                    isZs = False
                    # 往下找，是否有注释。
                    for s in range(l, len(list), 1):
                        l_str = list[s]
                        if '*/' in l_str:
                            isZs = True
                        if '/*' in l_str:
                            break
                    # 如果没有return，没有注释，那么条件成立
                    if isZs == False and isR == False and isIm_p == False:
                        needInserts.append(l)

        addLine = 0
        for i in needInserts:
            code = '\n    NSString *bl = @"bl_str";\n    bl = nil;\n'
            code = code.replace('bl', helper.getRandomStrWithOption(4, -1))
            list.insert(i + addLine, code)
            addLine = addLine + 1
        content = ""
        for l in list:
            content = content + l

        with open(path, 'w', encoding="utf-8") as f:
            f.write(content)

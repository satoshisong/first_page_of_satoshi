print('来和我一起创建矩阵吧！')
line = int(input('请输入第一个矩阵的行数好嘛qwq：'))
row = int(input('再输入第一个矩阵的列数吧：'))
i = 1
j = 1
matrix1 = []
line2 = int(input('那么，请输入第二个矩阵的行数：'))
row2 = int(input('再输入第二个矩阵的列数，谢谢~'))
if row != line2:
    print('很抱歉，这两个矩阵不能相乘呢~!')
else:
    for p in range(line):
        matrix1.append([])
    while i <= line:
        while j <= row:
            m = input(f'请你输入第一个矩阵第{i}行,第{j}列的元素,直到这条导引消失！')
            matrix1[i-1].append(m)
            j += 1
        j = 1
        i += 1
    print(matrix1)        #输出是为了检查矩阵
    i2 = 1
    j2= 1
    matrix2 = []
    for q in range(line2):
        matrix2.append([])
    while i2 <= line2:
        while j2 <= row2:
            m2 = input(f'接下来请输入第二个矩阵第 {i2}行,第{j2}列的元素,直到这条导引消失！')
            matrix2[i2-1].append(m2)
            j2 += 1
        j2 = 1
        i2 += 1
    print(matrix2)        
    result = []
    i2i = 1
    j2j = 1
    result_ij = 0
    for r in range(line):
        result.append([])
    while i2i <= line :
        while j2j <= row2:
            for x in range(row):            #这里是矩阵乘法的定义式
                a = (int(matrix1[i2i-1][x])) 
                b = (int(matrix2[x][j2j-1]))
                result_ij += (a*b)
            result[i2i-1].append(result_ij)
            j2j += 1
            result_ij = 0
        j2j = 1
        i2i += 1
    print("下方显示的就是结果啦:-)")
    print(result)
import time
time.sleep(10)


import numpy as np

def parseData(data):
    arr = []
    for i in data:
        curArr = []
        curArr.append((i[5] * i[6])/i[2])
        curArr.append(i[3])
        curArr.append(i[4])
        curArr.append((i[6] * i[7])/i[0])
        curArr.append(i[8])
        arr.append(curArr)
    return np.array(arr)
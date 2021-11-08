import numpy as np
import math

def normalizeData(data, weights):
    arr = np.transpose(data)
    newArr = np.array([])
    index = 0
    for i in arr:
        curArr = []
        for number in i:
            curArr.append(number * number)
        denom = math.sqrt(sum(curArr))
        newArr = np.append(newArr, np.divide(i, denom) * weights[index])
        index = index + 1
    newArr = np.reshape(newArr, (-1, len(arr[0])))
    return (np.transpose(newArr))
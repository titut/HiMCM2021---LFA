import numpy as np
import math

def getBestWorst(data, impact):
    arr = np.transpose(data)
    bestArr = np.array([])
    worstArr = np.array([])
    returnArr = np.array([])
    index = 0
    for i in arr:
        if(impact[index] == 0):
            bestArr = np.append(bestArr, np.square(i-i.min()))
        else:
            bestArr = np.append(bestArr, np.square(i-i.max()))
        index = index + 1
    bestArr = np.reshape(bestArr, (-1, len(arr[0])))
    bestArr = np.transpose(bestArr)
    for i in bestArr:
        returnArr = np.append(returnArr, math.sqrt(sum(i)))
    index = 0
    for i in arr:
        if(impact[index] == 0):
            worstArr = np.append(worstArr, np.square(i-i.max()))
        else:
            worstArr = np.append(worstArr, np.square(i-i.min()))
        index = index + 1
    worstArr = np.reshape(worstArr, (-1, len(arr[0])))
    worstArr = np.transpose(worstArr)
    for i in worstArr:
        returnArr = np.append(returnArr, math.sqrt(sum(i)))
    return np.reshape(returnArr, (-1, len(worstArr)))
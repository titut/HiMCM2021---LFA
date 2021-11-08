import numpy as np

def normalize(data):
    arr = np.transpose(data)
    newArr = np.array([])
    for i in arr:
        newArr = np.append(newArr, i/(sum(i)))
    return np.transpose(np.reshape(newArr, (-1, len(arr[0]))))
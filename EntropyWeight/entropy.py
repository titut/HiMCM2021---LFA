import numpy as np

def entropy(data):
    arr = np.transpose(data)
    n = []
    for i in arr:
        sum = 0
        for j in i:
            sum = sum + j * np.log(j)
        n.append(sum)
    n = np.array(n)
    n = n * (1/np.log(len(arr[0]))) * -1
    return n
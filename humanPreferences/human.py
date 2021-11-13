import numpy as np

scale = [
    [2368, 2595, 2792, 3020],
    [657.161, 822.007, 963.993, 1128.839],
    [1.673, 1.901, 2.099, 2.327],
]

def humanWeights(data):
    weight = data
    for i in range(0,3):
        if(weight[i] < scale[i][0]):
            weight[i] = 1
        elif(weight[i] > scale[i][0] and weight[i] < scale[i][1]):
            weight[i] = 2
        elif(weight[i] > scale[i][1] and weight[i] < scale[i][2]):
            weight[i] = 3
        elif(weight[i] > scale[i][2] and weight[i] < scale[i][3]):
            weight[i] = 4
        elif(weight[i] > scale[i][3]):
            weight[i] = 5
    weight[0] = 6 - weight[0]
    arr = np.array(weight)
    arr = arr/(sum(arr))
    return arr
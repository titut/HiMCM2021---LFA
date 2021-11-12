import numpy as np

def calculate(names,data):
    arr = []
    for i in range(0, len(data[0])):
        arr.append({"name":names[i],"value":data[1][i]/(data[1][i] + data[0][i])})
    return arr
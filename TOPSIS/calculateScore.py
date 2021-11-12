import numpy as np

def calculate(data):
    arr = []
    for i in range(0, len(data[0])):
        arr.append(data[1][i]/(data[1][i] + data[0][i]))
    return arr
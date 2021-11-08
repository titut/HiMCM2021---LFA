import numpy as np

def calculate(data):
    for i in range(0, len(data[0])):
        print(data[1][i]/(data[1][i] + data[0][i]))
    return
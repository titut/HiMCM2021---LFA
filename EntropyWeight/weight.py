import numpy as np

def weight(data):
    arr = 1 - data
    return list(arr/sum(arr))
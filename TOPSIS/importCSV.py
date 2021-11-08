import csv
import numpy as np

def importCSV(file):
    with open(file, newline='') as csvfile:
        csvLines = csv.reader(csvfile)
        arr = []
        for row in csvLines:
            arr.append(row)
        for y in range(0, len(arr)):
            for x in range(0, len(arr[y])):
                arr[y][x] = float(arr[y][x])
        return np.array(arr)
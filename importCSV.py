import csv
import numpy as np

def importCSV(file):
    with open(file, newline='') as csvfile:
        csvLines = csv.reader(csvfile)
        arr = []
        for row in csvLines:
            arr.append(row)
        for y in range(0, len(arr)):
            arr[y].pop(0)
            for i in range(0, len(y)):
                print(i)
            arr[y].pop(1)
        return np.array(arr).astype(np.float)
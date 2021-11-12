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
            arr[y].pop(1)
            if(arr[y][4] == "N/A"):
                arr[y][4] = arr[y][3]
        return np.array(arr).astype(np.float)
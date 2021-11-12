import csv
import numpy as np

def importCSV(file):
    with open(file, newline='') as csvfile:
        csvLines = csv.reader(csvfile)
        arr = []
        names = []
        for row in csvLines:
            names.append(row[0])
            row.pop(0)
            row.pop(1)
            if(row[4]=="N/A"):
                row[3]=row[4]
            arr.append(row)
        
        return names,np.array(arr).astype(np.float)
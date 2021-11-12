from importCSV import importCSV
from parseData import parseData
from EntropyWeight.entropyWeight import entropyWeight
from TOPSIS.topsis import Topsis

data = parseData(importCSV("data.csv"))
print(data)
weight = entropyWeight(data)
impact = [1,1,1,1,1]

print(Topsis(data, weight, impact))
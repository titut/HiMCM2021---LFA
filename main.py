from importCSV import importCSV
from parseData import parseData
from EntropyWeight.entropyWeight import entropyWeight
from TOPSIS.topsis import Topsis
from pprint import pprint

#names, 

#one for loop instead? combine functions?
names,csv = importCSV("data1.csv")
data = parseData(csv)
weight = entropyWeight(data)
impact = [1,1,1,1,1]

pprint(Topsis(names,data, weight, impact))
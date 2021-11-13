from importCSV import importCSV
from parseData import parseData
from EntropyWeight.entropyWeight import entropyWeight
from humanPreferences.human import humanWeights
from TOPSIS.topsis import Topsis
from pprint import pprint
import numpy as np

#names, 
#one for loop instead? combine functions of parseData and import?
names,csv = importCSV("data1.csv")
data = parseData(csv)
print(data)
humanWeight = humanWeights([2888, 884, 2.6, 4])
weight = entropyWeight(data)
humanWeight = np.append(humanWeight, weight[4])
weight = (humanWeight + weight)/2
impact = [1,1,1,1,1]

pprint(Topsis(names,data, weight, impact))
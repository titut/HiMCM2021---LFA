from importCSV import importCSV
from normalize import normalizeData
from idealBestWorst import getBestWorst
from calculateScore import calculate

#import data from csv file
print('Importing data...')
data = importCSV("data.csv")
weights = [1,1,1,1,1]
impact = [0,0,0,0,1]
print(data)

#normalize data
print()
print()
print('Normalizing data...')
normData = normalizeData(data, weights)
print(normData)

#calculate Euclidean Distance
print()
print()
print('Calculating Euclidean Distance...')
bestWorst = getBestWorst(normData, impact)
print(bestWorst)

#calculate topsis score
print()
print()
print('Calculating Topsis Score...')
calculate(bestWorst)
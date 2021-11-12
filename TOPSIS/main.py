from importCSV import importCSV
from normalize import normalizeData
from idealBestWorst import getBestWorst
from calculateScore import calculate

#import data from csv file
print('Importing data...')
data = importCSV("data.csv")
weights = [1,1,1,1,1]#subjective average 
#impact = [8,256,7,5000,25000]
impact = [1,1,1,1,0]
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
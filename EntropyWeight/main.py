from importCSV import importCSV
from normalize import normalize
from entropy import entropy
from weight import weight

#import data from csv file
print('Importing data...')
data = importCSV("data.csv")
print(data)

#normalize data
print()
print()
print('Normalizing data...')
normData = normalize(data)
print(normData)

#compute entropy
print()
print()
print('Computing Entropy...')
entropyData = entropy(normData)
print(entropyData)

#compute weights
print()
print()
print('Computing Weights...')
weights = weight(entropyData)
print(weights)
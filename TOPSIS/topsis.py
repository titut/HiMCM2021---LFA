from TOPSIS.normalize import normalizeData
from TOPSIS.idealBestWorst import getBestWorst
from TOPSIS.calculateScore import calculate

def Topsis(data, weights, impact):

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
    return calculate(bestWorst)
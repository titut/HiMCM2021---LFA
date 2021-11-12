from TOPSIS.normalize import normalizeData
from TOPSIS.idealBestWorst import getBestWorst
from TOPSIS.calculateScore import calculate

def Topsis(names,data, weights, impact):

    #normalize data
    print('\n\nNormalizing data...')
    normData = normalizeData(data, weights)
    print(normData)

    #calculate Euclidean Distance
    print('\n\nCalculating Euclidean Distance...')
    bestWorst = getBestWorst(normData, impact)
    print(bestWorst)

    #calculate topsis score
    print('\n\nCalculating Topsis Score...')
    return calculate(names,bestWorst)
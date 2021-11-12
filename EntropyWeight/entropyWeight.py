from EntropyWeight.normalize import normalize
from EntropyWeight.entropy import entropy
from EntropyWeight.weight import weight

def entropyWeight(data):

    #normalize data
    print('\n\nNormalizing data...')
    normData = normalize(data)
    print(normData)

    #compute entropy
    print('\n\nComputing Entropy...')
    entropyData = entropy(normData)
    print(entropyData)

    #compute weights
    print('\n\nComputing Weights...')
    weights = weight(entropyData)
    print(weights)
    return weights
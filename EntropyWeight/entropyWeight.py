from EntropyWeight.normalize import normalize
from EntropyWeight.entropy import entropy
from EntropyWeight.weight import weight

def entropyWeight(data):

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
    return weights
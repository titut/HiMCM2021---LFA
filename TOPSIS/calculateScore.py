
def calculate(names,data):
    arr = {}
    for i in range(0, len(data[0])):
        arr[names[i]]=data[1][i]/(data[1][i] + data[0][i])
    return sorted(arr.items(), key=lambda x: x[1],reverse=True)

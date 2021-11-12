import pandas as pd
import matplotlib.pyplot as plt

from importCSV import importCSV

names,csv = importCSV("data1.csv")
arr1=[]
arr2=[]
for i in csv:
    arr1.append(i[0])
    arr2.append(i[6])

data = {'Cost': arr1,
        'Capacity': arr2
       }
  
df = pd.DataFrame(data,columns=['Cost','Capacity'],index=names)
df.plot(x ='Cost', y='Capacity', kind = 'scatter')
plt.show()

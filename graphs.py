import pandas as pd
import matplotlib.pyplot as plt

from importCSV import importCSV

names,csv = importCSV("data1.csv")
arr1=[]
arr2=[]
for i in csv:
    arr1.append(i[0])
    arr2.append((i[5] * i[6])/i[2])

data = {
    'Cost': arr1,
    'Energy Density': arr2
}
df = pd.DataFrame(data,columns=['Cost','Energy Density'],index=names)
df.plot(x ='Cost', y='Energy Density', kind = 'scatter')
plt.show()
""" 
arr1=[]
arr2=[]
for i in csv:
    arr1.append(i[0])
    arr2.append(i[3])

data = {'Cost': arr1,
        'Continuous': arr2
       }
  
df = pd.DataFrame(data,columns=['Cost','Continuous'],index=names)
df.plot(x ='Cost', y='Continuous', kind = 'scatter')
plt.show()
 """
""" arr1=[]
arr2=[]
for i in csv:
    arr1.append(i[0])
    arr2.append(i[4])
data = {'Cost': arr1,
        'Instant': arr2
       }
df = pd.DataFrame(data,columns=['Cost','Instant'],index=names)
ax=df.plot(x ='Cost', y='Instant', kind = 'scatter')

def annotate_df(row):  
    ax.annotate(row.name, row.values,
                xytext=(5,0), 
                textcoords='offset points',
                size=5, 
                color='darkslategrey')
    
_ = df.apply(annotate_df, axis=1)
plt.show() """
#find outliers and delete 

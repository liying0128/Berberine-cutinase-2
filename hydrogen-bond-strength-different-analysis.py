import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=np.zeros((229,5))
data=pd.DataFrame(data)

for i in range (23,229):
    data.iat[i,0]=i
    if len(ListHBoRes(i,'water',results=5))==0:
        continue
    else:
        data.iat[i,2]=ListHBoRes(i,'water',results=5)[1]
        
for i in range(23,229):
    data.iat[i,3]=data.iat[i,1]-data.iat[i,2]
data.to_excel('hydrogen_energy_diff.xlsx')
plt.plot(data.iloc[:,0],data.iloc[:,3])


#color residue
for i in range(23,229):
    colo=180+data.iat[i,3]
    colo=int(colo)
    ColorRes(i,colo)

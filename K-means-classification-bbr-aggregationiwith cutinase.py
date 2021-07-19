from yasara import *
LoadPDB('1crn')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.zeros((1001,7))
data=pd.DataFrame(data)
data.index=data.index/10
DelObj('All')
ana_name='BBR-10-cu-sst'
BBR_num=10

for i in range (0,1001):
    if i<10:
        name=ana_name+'0000'+str(i)+'.sim'
    elif i<100:
        name=ana_name+'000'+str(i)+'.sim'
    elif i<1000:
        name=ana_name+'00'+str(i)+'.sim'
    else:
        name=ana_name+'0'+str(i)+'.sim'
    LoadSce(ana_name+'_water.sce')
    LoadSim(name)
    NumberRes('All','23')
    #for k in range(6):
    for m in range(BBR_num):
        res='Res '+str(m+229)
        dis=[]
        dis.append(GroupDistance('Res 208',res))
        dis.append(GroupDistance('Res 131',res))
        dis.append(GroupDistance('Res 27',res))
        dis.append(GroupDistance('Res 178',res))
        dis.append(GroupDistance('Res 222',res))
        dis.append(GroupDistance('Res 120',res))
        k=dis.index(min(dis))
        data.iat[i,k]=data.iat[i,k]+1
    DelObj('All')
data.to_excel(ana_name+'k_menas_aggregation_with_ST.xlsx')

import seaborn as sns

plt.style.use('seaborn-bright')
sns.violinplot(data=data.iloc[:,0:6],width=1,linewidth=(0.2))
plt.xlabel('Residue',fontsize=12)
plt.ylabel('Number of BBR aggregation',fontsize=12)
plt.title('BBR 10 μg/ml with ST')
plt.savefig(ana_name+'aggregation cutinase with ST.png', dpi=1000)
        
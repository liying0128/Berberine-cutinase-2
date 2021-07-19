from yasara import *
LoadPDB('aa')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.zeros((1001,5))
data=pd.DataFrame(data)
data.iloc[:,0]=data.index/10

#sim to PDB
DelObj('All')
ana_name='BBR20-Sodium stearate'
LoadSce(ana_name+'_water.sce')

for i in range (1000):
    if i<10:
        name=ana_name+'0000'+str(i)+'.sim'
    elif i<100:
        name=ana_name+'000'+str(i)+'.sim'
    elif i<1000:
        name=ana_name+'00'+str(i)+'.sim'
    else:
        name=ana_name+'0'+str(i)+'.sim'

    LoadSim(name)
    SavePDB('1 3',ana_name+str(i)+'.pdb')
DelObj('All')

#renumber
for i in range (1000):
    name=ana_name+str(i)+'.pdb'
    LoadPDB(name)
    NumberRes('all',0)
    AddHydAll('All')
    SavePDB('1 2',name)
    DelObj('All')
        
#calculation
DelObj('All')
for i in range (0,1000):
    name=ana_name+str(i)+'.pdb'
    LoadPDB(name)
    m=[]
    n=[]
    for k in range(2,22):
        if len(ListIntRes('Res Unk '+str(0),'Res Unk '+str(k),Type='Hydrophobic',results=5))==0:
            continue
        else:
            m.append(ListIntRes('Res Unk '+str(0),'Res Unk '+str(k),Type='Hydrophobic',results=5)[4])
            m.sort(reverse = True)
            if len(m)==1:
                data.iat[i,1]=m[0]
                data.iat[i,2]=0
            else:
                data.iat[i,1]=m[0]
                data.iat[i,2]=m[1]
            
    for k in range(2,22):
        if len(ListIntRes('Res Unk '+str(1),'Res Unk '+str(k),Type='Hydrophobic',results=5))==0:
            continue
        else:
            n.append(ListIntRes('Res Unk '+str(1),'Res Unk '+str(k),Type='Hydrophobic',results=5)[4])
            n.sort(reverse = True)
            if len(n)==1:
                data.iat[i,3]=n[0]
                data.iat[i,4]=0
            else:
                data.iat[i,3]=n[0]
                data.iat[i,4]=n[1]     
        
    DelObj('All')
data.to_excel('ST-BBR-hydrophobic.xlsx')

for i in range(1000):
    data.iat[i,5]=abs(data.iat[i,1]-data.iat[i,2])
    data.iat[i,6]=abs(data.iat[i,3]-data.iat[i,4])
    
    
fig,ax=plt.subplots()
ax.hist(data.iloc[600:,5], bins=100, facecolor="red", edgecolor="black", alpha=0.75)
ax.set_xlim(-1.5,31.5)
ax.set_ylim(0,20)
ax.set_xlabel('Relative hydrophobic strength',fontsize=12)
ax.set_ylabel('Number of snapshots',fontsize=12)
ax.set_title('Sodium stearate Mol1')
ax.set_yticks([0,5,10,15,20])
plt.savefig('Sodium Stearate Mol1.png', dpi=1000)

fig,ax=plt.subplots()
ax.hist(data.iloc[600:,6], bins=100, facecolor="green", edgecolor="black", alpha=0.75)
ax.set_xlim(-1.5,31.5)
ax.set_ylim(0,20)
ax.set_xlabel('Relative hydrophobic strength',fontsize=12)
ax.set_ylabel('Number of snapshots',fontsize=12)
ax.set_title('Sodium stearate Mol2')
ax.set_yticks([0,5,10,15,20])
plt.savefig('Sodium Stearate Mol2.png', dpi=1000)
    

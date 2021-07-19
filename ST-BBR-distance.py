import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.zeros((1001,3))
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
        m.append(GroupDistance('Res Unk '+str(0),'Res Unk '+str(k)))
        n.append(GroupDistance('Res Unk '+str(1),'Res Unk '+str(k)))
    m.sort()
    n.sort()
    data.iat[i,1]=m[1]
    data.iat[i,2]=n[1]
    DelObj('All')
data.to_excel('ST-BBR-distance.xlsx')

#make a plot
fig,a=plt.subplots()
a.plot(data.iloc[:1000,0],data.iloc[:1000,1],linewidth=0.8,color='red')
a.plot(data.iloc[:1000,0],data.iloc[:1000,2],linewidth=0.8,color='green')
a.legend(['ST Mol1','ST Mol2'])
a.set_ylabel('Distance (Å)',fontsize=12)
a.set_xlabel('Time (ns)',fontsize=12)
plt.savefig('1.png', dpi=1000)

#analysis
DelObj('All')
i=19
name=ana_name+str(i)+'.pdb'
LoadPDB(name)
ColorObj('1','red')
    
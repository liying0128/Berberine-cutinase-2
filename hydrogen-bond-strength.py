from yasara import *
LoadPDB('aa')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.zeros((1001,5))
data=pd.DataFrame(data)
data.iloc[:,0]=data.index/10
DelObj('All')
ana_name='BBRcu10'
LoadSce(ana_name+'_water.sce')

for i in range (0,1000):
    if i<10:
        name=ana_name+'0000'+str(i)+'.sim'
    elif i<100:
        name=ana_name+'000'+str(i)+'.sim'
    elif i<1000:
        name=ana_name+'00'+str(i)+'.sim'
    else:
        name=ana_name+'0'+str(i)+'.sim'
    LoadSim(name)
    JoinObj('4','1')
    SavePDB('1',ana_name+str(i)+'.pdb')
    DelObj('All')
    LoadSce(ana_name+'_water.sce')
DelObj('All')

#split Mol A
for i in range (0,1000):
    name=ana_name+str(i)+'.pdb'
    LoadPDB(name)
    SplitMol('A')
    if len(ListHBoMol('A','water',results=5))==0:
        continue
    else:
        data.iat[i,1]=ListHBoMol('A','water',results=5)[1]
    DelObj('All')
data.to_excel(ana_name+'hydrogen_bond_strength_cu.xlsx')    

fig,a=plt.subplots()
a.plot(data.iloc[:1000,0],data.iloc[:1000,1],linewidth=0.8,color='red')
a.plot(data.iloc[:1000,0],data.iloc[:1000,2],linewidth=0.8,color='green')
a.legend(['BBR 10 μg/ml','BBR 10 μg/ml with ST'])
a.set_ylabel('Hydrogen bond strength (KJ/Mol)',fontsize=12)
a.set_xlabel('Time (ns)',fontsize=12)
a.set_title('Hydrogen bond between solute and solvent')
a.set_ylim(5500,7500)
plt.savefig(ana_name+'-hydrogenbond-strength.png', dpi=1000)
    
 
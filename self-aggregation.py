from yasara import *
LoadPDB('aa')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.zeros((1001,40))
data=pd.DataFrame(data)

#sim to PDB
ana_name='BBR40'
LoadSce(ana_name+'_water.sce')
bbr_number=40
denominator=bbr_number*(bbr_number-1)/2

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
    SavePDB(3,ana_name+str(i)+'.pdb')
DelObj('All')

    
#renumber
for i in range (1000):
    name=ana_name+str(i)+'.pdb'
    LoadPDB(name)
    NumberRes('all',0)
    SavePDB(1,name)
    DelObj('All')

#calculation
DelObj('All')
for i in range (0,1000):
    name=ana_name+str(i)+'.pdb'
    LoadPDB(name)    
    for k in range(bbr_number):
        m=0
        for l in range(bbr_number):
            if l==k:
                continue
            else:
                if GroupDistance('Res Unk '+str(k),'Res Unk '+str(l))<5:
                    m=m+1
            
        data.iat[i,k]=m/2/denominator
    DelObj('All')
data.to_excel(ana_name+'_self_aggregation.xlsx')       
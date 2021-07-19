from yasara import *
LoadPDB('aa')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.zeros((1001,40))
data=pd.DataFrame(data)
data.iloc[:,0]=data.index/10
DelObj('All')
ana_name='BBRcu5'
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
    data.iat[i,1]=SurfObj('Obj 1', Type='Accessible',unit='All')
data.to_excel(ana_name+'_solvent_accessible_surface.xlsx')
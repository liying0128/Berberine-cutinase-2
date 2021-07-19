from yasara import *
LoadPDB('1crn')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.zeros((1001,7))
data=pd.DataFrame(data)
data.index=data.index/10
DelObj('All')
ana_name='BBRcu20'
BBR_num=20
data.iloc[:,0]=data.index/10
#sim to Sce
for i in range (0,1000):
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
    a='Res '+str(229+BBR_num)
    b='Res '+str(230+BBR_num)
    data.iat[i,0]=GroupDistance('Res 208', 'Res 140')
    reslist=[]
    reslist.append(GroupDistance('Res 208', a))
    reslist.append(GroupDistance('Res 208', b))
    if reslist[0]<reslist[1]:
        c=a
    else:
        c=b
    data.iat[i,1]=GroupDistance('Res 208', c)
    reslist1=[]
    reslist2=[]
    reslist1=ListIntRes('Res 208',c,Type='Hydrophobic',results=5)
    reslist2=ListIntRes('Res 208','Obj 3',Type='Hydrophobic',results=5)
    if len(reslist1)==0:
        data.iat[i,2]=0
    else:
        data.iat[i,2]=reslist1[4]
    
    if len(reslist2)==0:
        data.iat[i,3]=0
    else:
        data.iat[i,3]=reslist2[4]        
        
    DelObj('All')
data.to_excel(ana_name+'H208_ST_hydrophobic inter.xlsx')







    
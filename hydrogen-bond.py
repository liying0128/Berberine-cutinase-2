import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1=pd.read_table('cu40.txt',sep=',',header=None)
data2=pd.read_table('cu40ST.txt',sep=',',header=None)
#column 2 time, colume 16and17 hydrogen bond

fig,a=plt.subplots()
a.plot(data1.iloc[:1001,2],data1.iloc[:1001,16],linewidth=0.8,color='red')
a.plot(data2.iloc[:1001,2],data2.iloc[:1001,16],linewidth=0.8,color='green')
a.legend(['BBR 40 μg/ml','BBR 40 μg/ml with ST'])
a.set_ylabel('Number of hydrogen bond',fontsize=12)
a.set_xlabel('Time (ns)',fontsize=12)
a.set_ylim(120,170)
a.set_title('Hydrogen bond of the solute')
plt.savefig('bbr-40-hydrogenbond-solute.png', dpi=1000)


fig,a=plt.subplots()
a.plot(data1.iloc[:1001,2],data1.iloc[:1001,17],linewidth=0.8,color='red')
a.plot(data2.iloc[:1001,2],data2.iloc[:1001,17],linewidth=0.8,color='green')
a.legend(['BBR 40 μg/ml','BBR 40 μg/ml with ST'])
a.set_ylabel('Number of hydrogen bond',fontsize=12)
a.set_xlabel('Time (ns)',fontsize=12)
a.set_title('Hydrogen bond between solute and solvent')
a.set_ylim(260,360)
plt.savefig('bbr-40-hydrogenbond-solu-solven.png', dpi=1000)
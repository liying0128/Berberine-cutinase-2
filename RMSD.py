import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig,a=plt.subplots()
a.plot(data1.iloc[1:1000,2],data1.iloc[1:1000,27],linewidth=1,color='red')
a.plot(data2.iloc[1:1000,2],data2.iloc[1:1000,27],linewidth=1,color='green')
a.legend(['BBR 40 μg/ml','BBR 40 μg/ml with ST'])
a.set_ylabel('RMSD (Å)',fontsize=12)
a.set_xlabel('Time (ns)',fontsize=12)
plt.savefig('RMSD-40.png', dpi=1000)
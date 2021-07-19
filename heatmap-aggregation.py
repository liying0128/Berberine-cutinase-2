data=pd.read_excel('BBR20_self_aggregation.xlsx')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots(figsize=(6,9))
sns.heatmap(data.iloc[:,1:21],cmap='coolwarm',vmax=0.005,vmin=0)
ax.set_ylabel('Time (ns)',fontsize=15)
ax.set_yticks([0,200,400,600,800,1000])
ax.set_xlabel('BBR molecule',fontsize=15)
plt.title('Control',fontsize=15)
plt.savefig('1.png', dpi=1000)
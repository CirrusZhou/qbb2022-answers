import matplotlib.pyplot as plt
import numpy as np
#load the path of bdg_loader.py 
#reference:https://blog.csdn.net/xiaomifanhxx/article/details/81537506
import sys
sys.path.append("extra_data")
from bdg_loader import load_data

Sox2=load_data("croped_D2_Sox2_R1.bdg")
Klf4=load_data("croped_D2_Klf4_treat.bdg")
D0_H3K27ac=load_data("croped_D0_H3K27ac_treat.bdg")
D2_H3K27ac=load_data("croped_D2_H3K27ac_treat.bdg")

#print(np.array(Sox2['Y']))

fig, axes = plt.subplots(nrows=4, ncols=1,figsize=(5,8))
axes[0].plot(Sox2['X'],Sox2['Y'])
axes[0].set_title('Sox2')
axes[0].set_xticks([])
axes[0].fill_between(Sox2['X'],0,Sox2['Y'])

axes[1].plot(Klf4['X'],Klf4['Y'])
axes[1].set_title('Klf4')
axes[1].set_xticks([])
axes[1].fill_between(Klf4['X'],0,Klf4['Y'])

axes[2].plot(D0_H3K27ac['X'],D0_H3K27ac['Y'])
axes[2].set_title('H3K27ac_day 0')
axes[2].set_xticks([])
axes[2].fill_between(D0_H3K27ac['X'],0,D0_H3K27ac['Y'])

axes[3].plot(D2_H3K27ac['X'],D2_H3K27ac['Y'])
axes[3].set_title('H3K27ac_day 2')
axes[3].set_xticks([])
axes[3].fill_between(D2_H3K27ac['X'],0,D2_H3K27ac['Y'])


plt.savefig("four_track.png")

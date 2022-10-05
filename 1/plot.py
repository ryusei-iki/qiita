import matplotlib.pyplot as plt
import numpy as np

#定数の宣言
DATA_RANGE=[0,1]
DATA_NUM=10
X=np.linspace(DATA_RANGE[0],DATA_RANGE[1],DATA_NUM)[:,None]
X=np.tile(X,(2))

#描画の宣言
fig=plt.figure()
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0],aspect='equal')
cmap=plt.get_cmap('viridis')

#描画開始
for index in range(X.shape[0]-1):
    ax1.plot([X[index,0],X[index+1,0]],[X[index,1],X[index+1,1]],color=cmap(index/(X.shape[0]-2)))
plt.show()

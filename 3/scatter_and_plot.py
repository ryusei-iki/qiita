import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.collections import LineCollection

#変数の宣言
DATA_NUM=100
RANGE_START=[[-2,-2],[1,1],[1,-2]]
RANGE_END=[[-1,-1],[2,2],[2,-1]]
X=np.random.uniform(RANGE_START,RANGE_END,(100,3,2))
X=X.transpose(1,0,2)
X_RECT=np.array([[[-2,-2,-1,-1,-2],[-2,-1,-1,-2,-2]],[[1,1,2,2,1],[1,2,2,1,1]],[[1,1,2,2,1],[-2,-1,-1,-2,-2]]])
X_RECT=X_RECT.transpose(0,2,1)
X_COLOR=np.linspace(0,1,3)
X_COLOR=np.repeat(X_COLOR[:,None],DATA_NUM,axis=1)
cmap=plt.get_cmap('viridis')
kar=np.linspace(0,1,3)
LABEL=[0,1,2]

#描画の宣言
fig=plt.figure()
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0],aspect='equal')

#描画スタート
ax1.scatter(X[:,:,0],X[:,:,1],c=X_COLOR)
cmap = ListedColormap(cmap(kar))
lc = LineCollection(X_RECT, cmap=cmap,linewidth=5)
lc.set_array(np.array(LABEL))
ax1.add_collection(lc)
plt.show()

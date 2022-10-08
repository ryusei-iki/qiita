import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import LineCollection

#変数の宣言
X_RECT_PLOT=np.array([[[-2,-2,-1,-1,-2],[-2,-1,-1,-2,-2]],[[1,1,2,2,1],[1,2,2,1,1]],[[1,1,2,2,1],[-2,-1,-1,-2,-2]]])
X_RECT=np.array([[[-2,-2],[-2,-1],[-1,-1],[-1,-2],[-2,-2]],
                [[ 1 ,1],[ 1 ,2],[ 2, 2],[ 2 ,1],[ 1 ,1]],
                [[ 1,-2],[ 1,-1],[ 2,-1],[ 2,-2],[ 1,-2]]])
#描画の宣言
fig=plt.figure(figsize=(19,6))
gs=fig.add_gridspec(1,3)
ax1=fig.add_subplot(gs[0,0],aspect='equal')
ax2=fig.add_subplot(gs[0,1],aspect='equal')
ax3=fig.add_subplot(gs[0,2],aspect='equal')

#描画スタート

#LineCOllection
lc = LineCollection(X_RECT)
ax1.set_title('LineCollection')
ax1.set_xlim(-3,3)
ax1.set_ylim(-3,3)
ax1.add_collection(lc)

#Rectangle
X_CENTER=[(1.5,1.5),(1.5,-1.5),(-1.5,-1.5)]
ax2.set_title('Rectangle')
ax2.set_xlim(-3,3)
ax2.set_ylim(-3,3)
for i in range(3):
    r = patches.Rectangle( xy=X_CENTER[i] , fill=False,width=1, height=1) # 四角形のオブジェクト
    ax2.add_patch(r)

#plot
X_RECT_PLOT=X_RECT_PLOT.transpose(2,0,1)
ax3.set_xlim(-3,3)
ax3.set_ylim(-3,3)
ax3.set_title('plot')
ax3.plot(X_RECT_PLOT[:,:,0],X_RECT_PLOT[:,:,1])

plt.show()

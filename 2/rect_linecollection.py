import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

#変数の宣言
X_RECT=np.array([[[-2,-2],[-2,-1],[-1,-1],[-1,-2],[-2,-2]],
                [[ 1 ,1],[ 1 ,2],[ 2, 2],[ 2 ,1],[ 1 ,1]],
                [[ 1,-2],[ 1,-1],[ 2,-1],[ 2,-2],[ 1,-2]]])
#描画の宣言
fig=plt.figure()
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0],aspect='equal')

#描画スタート

#LineCOllection
lc = LineCollection(X_RECT,color='b')
ax1.set_title('LineCollection')
ax1.set_xlim(-3,3)
ax1.set_ylim(-3,3)
ax1.add_collection(lc)

plt.show()

import numpy as np
import matplotlib.pyplot as plt

#変数の宣言
X_RECT_PLOT=np.array([[[-2,-2,-1,-1,-2],[-2,-1,-1,-2,-2]],[[1,1,2,2,1],[1,2,2,1,1]],[[1,1,2,2,1],[-2,-1,-1,-2,-2]]])
X_RECT=np.array([[[-2,-2],[-2,-1],[-1,-1],[-1,-2],[-2,-2]],
                [[ 1 ,1],[ 1 ,2],[ 2, 2],[ 2 ,1],[ 1 ,1]],
                [[ 1,-2],[ 1,-1],[ 2,-1],[ 2,-2],[ 1,-2]]])

#描画の宣言
fig=plt.figure()
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0],aspect='equal')

#描画スタート

#plot
X_RECT_PLOT=X_RECT.transpose(1,0,2)
ax1.set_xlim(-3,3)
ax1.set_ylim(-3,3)
ax1.set_title('plot')
ax1.plot(X_RECT_PLOT[:,:,0],X_RECT_PLOT[:,:,1],c='b')

plt.show()

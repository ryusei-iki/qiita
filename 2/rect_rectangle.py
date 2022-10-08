import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#変数の宣言
X_CENTER=[(1.5,1.5),(1.5,-1.5),(-1.5,-1.5)]

#描画の宣言
fig=plt.figure(figsize=(19,6))
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0],aspect='equal')

#描画スタート

#Rectangle
ax1.set_title('Rectangle')
ax1.set_xlim(-3,3)
ax1.set_ylim(-3,3)
for i in range(3):
    r = patches.Rectangle( xy=X_CENTER[i] , fill=False,width=1, height=1,color='b') # 四角形のオブジェクト
    ax1.add_patch(r)

plt.show()

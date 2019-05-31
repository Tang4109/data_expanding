# 导入NearestNeighbor包 和 numpy
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 定义一个数组
X = np.array([[-1, -1, 0], [-2, -1, -3], [-3, -2, -2],[0,0,1],[0,1,0],[1,0.6,0.8],
[1, 1, 2], [2, 1, 4], [3, 2, 6],[3,5,5],[4,5,3],[4,6,5], [5, 7, 2], [-1, -1.5, -2]])

X0=X.tolist()#数组转列表
"""
NearestNeighbors用到的参数解释
n_neighbors=5,默认值为5，表示查询k个最近邻的数目
algorithm='auto',指定用于计算最近邻的算法，auto表示试图采用最适合的算法计算最近邻
fit(X)表示用X来训练算法
"""
num1 = len(X)  # 初始元素个数
num2 = num1  # 添加元素后个数
print("初始元素个数：", num1)

#用k近邻扩充数据点
while (num2 / num1 < 11):
    nbrs = NearestNeighbors(n_neighbors=2, algorithm="auto").fit(X)
    # 返回距离每个点k个最近的点和距离指数，indices可以理解为表示点的下标，distances为距离
    distances, indices = nbrs.kneighbors(X)
    X = list(X)  # 转为list才能使用append函数
    for x in indices:
        X.append( (X[x[0]]+X[x[1]])/2)
    # 去除重复的元素
    # 删除重复行
    X = np.unique(X, axis=0)
    num2 = len(X)  # 添加元素后个数

X=X.tolist()#数组转列表
print("扩充后元素个数：",num2)
X_add = [h for h in X if h not in X0]#去除原数据，剩下扩充数据
num3=len(X_add)
print("添加的元素个数：",num3)

#绘图
#新增数据
x = []
for j in range(num3):
    x.append(X_add[j][0])
y = []
for k in range(num3):
    y.append(X_add[k][1])
z = []
for m in range(num3):
    z.append(X_add[m][1])

#原始数据
x1 = []
for j1 in range(num1):
    x1.append(X0[j1][0])
y1 = []
for k1 in range(num1):
    y1.append(X0[k1][1])
z1 = []
for m1 in range(num1):
    z1.append(X0[m1][1])


ax = plt.subplot(111,projection='3d')  # 创建一个三维的绘图工程
ax.scatter(x, y, z, c='r',s=5)  # 绘制数据点,颜色是红色
ax.scatter(x1, y1, z1, c='b',s=5)

ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()

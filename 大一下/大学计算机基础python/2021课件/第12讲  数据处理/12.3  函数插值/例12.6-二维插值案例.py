#例12.6-二维插值案例.py
"""
二维插值案例：平板表面温度插值。在Python的IDLE里运行正确，在Spyder中运行也正确
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm  

#（1）产生3*5（3行5列）的网格数据
#x,y= np.mgrid[1:5:5j, 1:3:3j] #这样写也可以，代替下面三句
x = np.linspace(0,4,5)                  #网格点x坐标值，一维数组
y = np.linspace(0,2,3)                  #网格点y坐标值
print("x=",x)
print("y=",y)
x_grid, y_grid = np.meshgrid(x, y)      #从参数（x,y）中返回2个坐标矩阵x_grid、y_grid（3行5列），存储3*5的网格坐标值
print("x_grid：\n",x_grid)
print("y_grid：\n",y_grid)
fvals = np.array([[82,81,80,82,84],[79,63,61,65,81],[84,84,82,85,86]]) # 创建二维数组，存储每个网格点上的温度值
print("fvals：\n",fvals)
#fvals = [[82,81,80,82,84],[79,63,61,65,81],[84,84,82,85,86]] # 存储每个网格点上的温度值
'''如果采用列表的嵌套存储每个网格点上的温度值，在Python的IDLE里运行正确，但在Spyder中运行会出错。
   如果采用二维数组存储，则在两个环境里运行都正确。'''

#（2）在三维坐标系画出原始数据产生的平板温度分布网线图
plt.figure(1)                           #创建图表1
ax=plt.subplot(projection = '3d')       #创建三维图形子图
surf =ax.plot_surface(x_grid, y_grid, fvals, rstride=1, cstride=1, cmap=cm.coolwarm)#绘制原始数据的3D曲面，rstride和cstride分别设置行方向的步长和列方向的步长
#也可以不赋给变量surf
#cmap可以为cm.rainbow、cm.autumn
#surf = ax.plot_surface(x_grid, y_grid, fvals, rstride=1, cstride=1, color='red') #或者不使用cmap，而是设置color参数为红色

#（3）进行二维插值
newfunc = interpolate.interp2d(x, y, fvals)  #默认采用双线性插值linear。newfunc为一个函数

#（4）建立3*5网格上的插值数据点
xnew = np.arange(0, 4, 0.1)            #插值点x坐标值，一维数组
ynew = np.arange(0, 2, 0.1)            #插值点y坐标值
#xnew = np.linspace(0,4,41)            
#ynew = np.linspace(0,2,21)            
'''在x-y平面上每0.1个单位的地方进行插值。x范围为[0,4]，则应该有(4-0)/0.1+1=41条y线；
   y范围为[0,2]，则应该有(2-0)/0.1+1=21条x线。
   采用linspace函数不如arange函数简单'''
xnew_grid, ynew_grid = np.meshgrid(xnew, ynew) #产生21*41个插值点网格数据
fnew = newfunc(xnew, ynew)              #计算插值结果，fnew为矩阵，包含21*41个值
#print('fnew =',fnew)

#（5）绘制插值后数据的3D曲面
plt.figure(2)                           # 创建图表2
ax2=plt.subplot(projection = '3d')  
surf2 = ax2.plot_surface(xnew_grid, ynew_grid, fnew,rstride=1, cstride=1,cmap=cm.coolwarm)#绘制插值后数据3D曲面
#surf2 = ax2.plot_surface(xnew_grid, ynew_grid, fnew,rstride=1, cstride=1,color='blue') #或者不使用cmap，而是设置color参数为蓝色

plt.show()

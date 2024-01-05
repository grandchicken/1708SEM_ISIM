#【例12.5】非线性最小二乘拟合案例：求血液中酒精含量的拟合曲线。
#例12.5-leastsq_fit.py
#用leastsq函数拟合

import numpy as np
import math
#scipy中的子函数库optimize已经提供了实现最小二乘拟合算法的函数leastsq
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

#（1）定义待拟合的函数
def fun(x, p):              #x是变量，p是待拟合的参数（一维数组形式）
    a, b, c = p             #数组p中的元素分别赋给a、b、c这三个变量
    return a*(x**b)*(math.e)**(c*x)

#（2）定义偏差函数：计算真实数据和拟合数据之间的误差
def residuals(p, x, y):     #p是待拟合的参数，x和y分别是对应的真实数据
    return fun(x, p) - y    #调用待拟合的函数

#（3）将真实实验数据存储于一维数组中
t=np.array([0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
h=np.array([30,68,75,82,82,77,68,68,58,51,50,41,38,35,28,25,18,15,12,10,7,7,4])

#（4）调用拟合函数leastsq，得到拟合参数
'''第一个参数是偏差函数，第二个是拟合初始值，第三个是需要拟合的实验数据'''
r = leastsq(residuals, [1,1,1], args=(t, h)) #返回值为数组，第一个值是拟合参数

#print ('拟合参数a,b,c为：',r[0]) #输出拟合参数。r[0]存储的是拟合参数，r[1]代表其他信息
a,b,c=r[0]                     #r[0]存储的是拟合参数，r[1]代表其他信息
print ('拟合参数a=%0.3f，b=%0.3f，c=%0.3f' % (a,b,c)) #输出拟合参数

#（5）绘制原始数据点和拟合曲线
plt.figure(figsize=(8,6))   #创建一个全局绘图区域
plt.scatter(t,h,color="red",label="Sample Point",linewidth=3) #绘散点图（样本点）

#生成绘制拟合曲线所需的数据（插值）
x=np.linspace(0,20,1000)
y=a*(x**b)*(math.e)**(c*x)
plt.plot(x,y,color="orange",label="Fitting Curve",linewidth=2) #绘拟合曲线
plt.legend()

plt.show()

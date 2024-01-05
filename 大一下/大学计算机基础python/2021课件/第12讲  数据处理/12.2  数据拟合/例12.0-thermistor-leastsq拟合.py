#例12.0-thermistor-leastsq拟合.py
#热敏电阻问题
'''
使用拟合函数leastsq拟合，求出拟合参数a、b。
再利用拟合模型计算60、100度时的R值
'''

import numpy as np
#scipy中的optimize模块提供了实现最小二乘拟合算法的函数leastsq
from scipy.optimize import leastsq

#（1）定义待拟合的函数。x是自变量，p是待拟合的参数（一维数组 [a, b]）
def fun(x, p):
    a, b = p
    return a*x + b #返回拟合函数的值

#（2）定义偏差函数：计算拟合数据与实验数据之间的误差。p是待拟合的参数，x和y分别是实验数据的x和y坐标值（一维数组）
def residuals(p, x, y):
    return fun(x, p) - y

#（3）将真实实验数据存储于一维数组中。使用numpy库的array函数将列表转换为一维数组
x1 = np.array([20.5,32.7,51.0,73.0,95.7], dtype=float) #温度
y1 = np.array([765, 826, 873, 942, 1032], dtype=float) #电阻值

#（4）调用最小二乘拟合函数leastsq()，求出拟合参数。第一个参数是实验数据与拟合数据之间的偏差，第二个是拟合初始值，第三个是需要拟合的实验数据
r = leastsq(residuals, [1, 1], args=(x1, y1))

#（5）输出拟合参数。数组r[0]存储的是拟合参数，r[1]、r[2]代表其他信息
a,b=r[0]
print('拟合参数a=%0.3f, b=%0.3f' % (a,b))        #保留小数点后三位

#（6）计算60度时的R值
R_at60=a*60+b
print('60度时的R值为%0.3f' % R_at60)

#（7）计算100度时的R值
#R_at100=a*100+b
#print('100度时的R值为%0.3f' % R_at100)

#验证拟合参数的正确性
R_at20_5=a*20.5+b
error1=abs((R_at20_5-y1[0])/y1[0])*100              #计算相对误差（乘以100，以转换为百分比）
print('t=20.5度时的R值为%0.3f，相对误差为%1.2f%%' % (R_at20_5,error1))
R_at95_7=a*95.7+b
error2=abs((R_at95_7-y1[-1])/y1[-1])*100
print('t=95.7度时的R值为%0.3f，相对误差为%1.2f%%' % (R_at95_7,error2))

'''
60度时的R值为906.021
100度时的R值为1041.971
'''

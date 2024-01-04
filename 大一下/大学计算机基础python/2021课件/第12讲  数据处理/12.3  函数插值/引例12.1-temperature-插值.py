#引例12.1-temperature-插值.py
'''
在一天24小时内，从零点开始每间隔2小时测得的环境温度数据分别为：12，9，9，10，18 ，24，28，27，25，20，18，15，13。
试推测中午1点的温度，并做出24小时温度变化曲线图。
'''
#使用一维插值函数interp1d()进行插值，得到多项式插值函数；再给这个函数传递某个温度值（60度），就可以计算相应的插值函数值——R。

import numpy as np  
from scipy import interpolate   #插值模块
import matplotlib.pyplot as plt
from pylab import mpl           #为了正常显示中文

#（1）绘制原始数据点及其曲线
x1 = np.linspace(0, 24, 13)                 #一组测量数据的x值，时间。默认包括终值
y1 = np.array([12,9,9,10,18,24,28,27,25,20,18,15,13], dtype=float) #一组测量数据的y值，温度。使用numpy库的array函数将列表类型数据转换为一维数组
plt.plot(x1,y1,"r--",marker="+",markeredgecolor="blue",label="原始数据")   

#（2）一维插值，得到多项式插值函数
f=interpolate.interp1d(x1,y1,kind="cubic")  #创建interp1d对象(三次样条插值) 。返回值为一个函数

#（3）绘制插值后曲线    
xnew = np.arange(0, 24, 0.5)                #建立插值数据点，一维数组。注意arange函数不包括终值
#print(xnew)
ynew=f(xnew)                                #计算插值结果 
plt.plot(xnew,ynew,"g-",label="插值后曲线")  #绿色实线

#（4）计算中午1点（即13点）的温度
T_at13=f(13) 
print('13点时的温度值为%0.2f' % T_at13)
plt.plot(13,T_at13,"k",marker="o",label="t=13") #也可以在图中绘制插值点（黑色小圆点）

#（5）美化图表
mpl.rcParams["font.sans-serif"] = ["SimHei"]  #指定默认字体为黑体
plt.title("环境温度预测")
plt.xlabel('时间')                             #设置x轴标签（x轴含义）
plt.ylabel('环境温度')                         #设置y轴标签（y轴含义）
plt.legend(loc="upper right")  

plt.show() 

#计算得到13点的温度值为27.87


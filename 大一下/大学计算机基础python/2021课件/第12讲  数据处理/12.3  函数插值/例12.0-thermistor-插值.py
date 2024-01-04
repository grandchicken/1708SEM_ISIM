#例12.0-thermistor-插值.py
#热敏电阻问题
#使用一维插值函数interp1d()进行插值，得到多项式插值函数；再给这个函数传递某个温度值（60度），就可以计算相应的插值函数值——R。

import numpy as np  
from scipy import interpolate   #插值模块
import matplotlib.pyplot as plt
from pylab import mpl           #为了正常显示中文

#（1）将真实实验数据存储于一维数组中。使用numpy库的array函数将列表类型数据转换为一维数组
x1 = np.array([20.5,32.7,51.0,73.0,95.7], dtype=float) #温度
y1 = np.array([765, 826, 873, 942, 1032], dtype=float) #电阻值
plt.plot(x1,y1,"r--",marker="+",markeredgecolor="blue",label="原始数据") 

#（2）一维插值，得到多项式插值函数
f=interpolate.interp1d(x1,y1,kind="cubic")    #创建interp1d对象(三次样条插值) 。返回值为一个函数

#（3）绘制插值后曲线    
xnew = np.arange(20.5, 95.7, 0.1)           #建立插值数据点，一维数组
ynew=f(xnew)                                #计算插值结果 
plt.plot(xnew,ynew,"g-",label="插值后曲线")  #绿色实线

#（4）美化图表
mpl.rcParams["font.sans-serif"] = ["SimHei"]    #指定默认字体为黑体  
mpl.rcParams["axes.unicode_minus"] = False      #解决将负号'-'显示为方块的问题
plt.title("三次样条插值")
plt.legend(loc="lower right")  

#（4）计算60度时的R值
R_at60=f(60) 
print('60度时的R值为%0.3f' % R_at60)
plt.plot(60,R_at60,"k",marker="o",label="t=60") 

#计算得到60度时的R值为897.874

#验证插值的正确性
R_at20_5=f(20.5)
print('20.5度时的R值为%0.3f' % R_at20_5)
R_at95_7=f(95.7)
print('95.7时的R值为%0.3f' % R_at95_7)

plt.show() 




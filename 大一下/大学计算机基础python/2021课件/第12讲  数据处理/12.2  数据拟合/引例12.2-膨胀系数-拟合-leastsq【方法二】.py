#引例12.2-膨胀系数-拟合.py
#方法二 用leastsq函数拟合
'''
某合金成分x与膨胀系数y之间的关系有如下实验数据，求膨胀系数y与成分x的拟合曲线y=P(x)。并推测合金成分为45时的膨胀系数。

使用拟合函数leastsq拟合，求出拟合参数。
再利用拟合模型计算合金成分为45时的膨胀系数。
'''

import numpy as np
#scipy中的optimize模块已经提供了实现最小二乘拟合算法的函数leastsq
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from pylab import mpl           #为使图形正常显示中文，需要导入此模块

#（1）绘制原始数据点和原始数据曲线
x1 = np.arange(37, 44, 1)       #一组测量数据，合金成分，步长为1。注意数组不包括终值
y1 = np.array([3.40, 3.00, 2.10, 1.53, 1.80, 1.90, 2.90], dtype=float) #膨胀系数。使用numpy库的array函数将列表类型数据转换为一维数组
plt.plot(x1,y1,"r--",marker="+",markeredgecolor="blue",label="原始数据")   #绘制原始数据曲线

#（2）定义待拟合的函数
def fun(x, p):                  #x是自变量，p是参数
    a2, a1, a0 = p              #p[0]对应多项式的最高次幂的系数（a2），p[2]对应多项式的常数项（a0）
    return a2*x**2 + a1*x+a0    #返回拟合函数的值

#（3）定义偏差函数：计算实验数据与拟合数据之间的误差
def residuals(p, x, y):         #p是待拟合的参数，x和y分别是实验数据的x和y坐标值
    return fun(x, p) - y

#（4）调用拟合函数，求出拟合参数
r = leastsq(residuals, [1, 1, 1], args=(x1, y1)) #第一个参数是实验数据与拟合数据之间的偏差，第二个是拟合初始值，第三个是需要拟合的实验数据
#输出拟合参数
a2, a1, a0 =r[0]                                 #r[0]存储的是拟合参数，r[1]、r[2]代表其他信息
print('拟合参数a2=%0.3f, a1=%0.3f, a0=%0.3f' % (a2, a1, a0 ))        #保留小数点后三位
print('拟合模型为：','y=%.3f*x**2+(%.3f)*x+(%.3f)' %(a2, a1, a0))
#（5）计算合金成分为45时的膨胀系数
x0=45
Result=a2*x0**2 + a1*x0+a0
print('合金成分为45时的膨胀系数为%0.3f' % Result)

#（6）生成绘制拟合曲线所需的数据（插值）
x2=np.linspace(37, 43, 50)                       #产生区间[37, 45]内等间隔的50个值。默认包括终值  
y2=np.polyval((a2, a1, a0),x2)                   #使用polyval()函数计算多项式在x2处的值y2  

#（7）绘制拟合曲线
plt.plot(x2,y2,'g-',label='拟合曲线')            #绘制拟合曲线，#绿色实线

#（8）验证拟合参数的正确性
x_37=37
y_37=np.polyval((a2, a1, a0),x_37)
print('成分为37时的膨胀系数为%0.3f' % y_37)
x_43=43
y_43=np.polyval((a2, a1, a0),x_43)
print('成分为43时的膨胀系数为%0.3f' % y_43)

#美化图表
mpl.rcParams["font.sans-serif"] = ["SimHei"]    #指定默认字体为黑体  
mpl.rcParams["axes.unicode_minus"] = False      #解决将负号'-'显示为方块的问题
plt.title("膨胀系数y与成分x的拟合曲线")
plt.legend(loc="upper right")  

plt.show()             #一定要放在最后！否则其后的print语句可能不执行

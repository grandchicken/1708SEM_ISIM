#引例12.2-膨胀系数-拟合-polyfit【方法一】.py
#方法一 用polyfit()函数拟合
'''
某合金成分x与膨胀系数y之间的关系有如下实验数据，求膨胀系数y与成分x的拟合曲线y=P(x)。并推测合金成分为45时的膨胀系数。

使用拟合函数leastsq拟合，求出拟合参数。
再利用拟合模型计算合金成分为45时的膨胀系数。
'''
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl           #为使图形正常显示中文，需要导入此模块

#（1）绘制原始数据点和原始数据曲线
x1 = np.arange(37, 44, 1)            #一组测量数据，合金成分，步长为1。注意数组不包括终值
y1 = np.array([3.40, 3.00, 2.10, 1.53, 1.80, 1.90, 2.90], dtype=float) #膨胀系数。使用numpy库的array函数将列表类型数据转换为一维数组
plt.plot(x1,y1,"r--",marker="+",markeredgecolor="blue",label="原始数据")   #绘制原始数据曲线

#（2）调用polyfit函数，求出拟合参数
p=np.polyfit(x1,y1,2)               #二次多项式：y=p[0]*x**2+p[1]*x+p[2]
a2, a1, a0 = p                      #p[0]对应多项式的最高次幂的系数（a2），p[2]对应多项式的常数项（a0）                   
print('拟合参数：a2=%0.3f, a1=%0.3f, a0=%0.3f' % (a2, a1, a0 ))        #保留小数点后三位
print('拟合模型为：','y=%.3f*x**2+(%.3f)*x+(%.3f)' %(a2, a1, a0))

#（3）调用polyval函数，计算合金成分为45时的膨胀系数
x0=45
Result=np.polyval(p,x0)            #计算插值
#Result=a2*x0**2 + a1*x0+a0        #将x0直接带入拟合模型，效果同使用polyval函数
print('合金成分为45时的膨胀系数为%0.3f' % Result)

#（4）绘制拟合曲线
#生成绘制拟合曲线所需的数据（插值）
x2=np.linspace(37, 43, 50)       #产生区间[37, 43]内等间隔的50个值
y2=np.polyval(p,x2)                 #使用polyval()函数计算多项式在x2处的值y2  
plt.plot(x2,y2,'g-',label='拟合曲线') #绿色实线

#（5）验证拟合参数的正确性
x_37=37
y_37=np.polyval(p,x_37)
print('合金成分为37时的膨胀系数为%0.3f' % y_37)
x_43=43
y_43=np.polyval(p,x_43)
print('合金成分为43时的膨胀系数为%0.3f' % y_43)

#美化图表
mpl.rcParams["font.sans-serif"] = ["SimHei"]  #指定默认字体为黑体，使中文正常显示  
plt.title("膨胀系数y与成分x的拟合曲线")
plt.xlabel('合金成分')                         #设置x轴标签（x轴含义）
plt.ylabel('膨胀系数')                         #设置y轴标签（y轴含义）
plt.legend(loc="upper right")  

plt.show()                      #一定要放在最后！否则其后的print语句可能不执行

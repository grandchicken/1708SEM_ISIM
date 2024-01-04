'''多项式拟合求解热敏电阻问题'''
#例12.0-thermistor-poly_fit.py
#热敏电阻问题

#（1）导入三方库
import numpy as np
import matplotlib.pyplot as plt

#（2）已知实验数据
x=[20.5,32.7,51.0,73.0,95.7]      #温度
y=[765, 826, 873, 942, 1032]      #电阻值

#（3）调用polyfit函数，求出拟合参数
a,b=np.polyfit(x,y,1)                        #以数组形式返回拟合多项式系数。输入参数x,y为要拟合的数据，可以为序列类型（列表，元组或数组）;参数1表示拟合多项式的次数为1 
print('拟合参数a=%0.3f, b=%0.3f' % (a,b))    #保留小数点后三位

#（4）生成绘制拟合曲线所需的数据
x0=np.linspace(20.5,95.7,50)                 #产生区间[20.5,95.7]内等间隔的50个值  
y0=np.polyval((a,b),x0)                      #使用polyval()函数计算多项式在x0处的值y0

#（5）绘制原始数据点和拟合曲线
plt.plot(x,y,'+',color='b',label='rawdata') #绘制原始数据点，蓝色
plt.plot(x0,y0,'r',label='fitline')         #绘制拟合曲线，红色

plt.legend(loc='lower right')               #在右下角添加图例

#（6）计算60度时的R值
R=a*60+b
print('60度时的R值为%0.3f' % R)
y1=np.polyval((a,b),60)                      #使用polyval()函数计算多项式在60处的值y1
print('polyval()函数计算60度时的y1值为%0.3f' % y1)

#（7）验证拟合参数的正确性
y_20,y_30=np.polyval((a,b),(20.5,95.7))      #使用polyval()函数计算多项式在一组x值处的y值
print('polyval()函数计算在一组x值(20.5,95.7)处的y值为%0.3f, %0.3f' % (y_20,y_30))

plt.show()                                  #一定要放在最后，否则不执行（6）

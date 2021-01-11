x1=float(input())
x2=float(input())
x3=float(input())
x4=float(input())
x5=float(input())
x6=float(input())
v1=(x3/100-x1/100)/0.1
v2=(x4/100-x2/100)/0.1
v3=(x5/100-x3/100)/0.1
v4=(x6/100-x4/100)/0.1
v_av=(v1+v2+v3+v4)/4
x_av=(0.1+0.05+0.15)/4
xy_av=(0.05*v2+0.1*v3+0.15*v4)/4
fenmu=(x_av*x_av-(0.0025+0.01+0.0225)/4)
a=(v_av*x_av-xy_av)/fenmu
import math
deta=math.fabs((a-9.8)/9.8)
print("{:.3f}".format(a))
print("{:.5f}".format(deta))


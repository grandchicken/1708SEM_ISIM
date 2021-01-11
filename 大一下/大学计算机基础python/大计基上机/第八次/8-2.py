from tkinter import *
from scipy.stats import poisson
from scipy import stats
from scipy.stats import poisson
from math import *
from random import *
from scipy import interpolate 
import collections
def Normal(x,miu,sigma):
    return 1.0/(sqrt(2*3.14)*sigma) * exp(-1*(x-miu)*(x-miu)/(2*sigma*sigma))
def Random_Normal(miu,sigma,Min,Max):
    while True:      
        x=randint(Min,Max)
        y=Normal(x,miu,sigma)
        dScope=uniform(0,Normal(miu,miu,sigma))    
        if(dScope<=y):
            return x
def Stat():
    miu=int(ent3.get())
    sigma=int(ent5.get())
    size=int(ent2.get())
    s=[]
    for i in range(0,size):
        s.append(Random_Normal(0,1,-2,2))
        text2.insert(INSERT,s[i])
        text2.insert(INSERT,'\t\t')        
def Poisson():
    a=int(ent4.get())
    I=int(ent1.get())    
    r=poisson.rvs(a,size=I)
    s=[]
    x=[]
    y=[]
    for i in range(I):        
        text1.insert(INSERT,r[i])
        text1.insert(INSERT,'\t\t')
    b=collections.Counter(r)
    s={}
    for c in b:
        s[c]=b[c]
    x=sorted(s)
    for i in range(len(x)):
        y.append(s[x[i]]/I)
    yy1=interpolate.spline(x,y,a+0.5)
    yy2=interpolate.spline(x,y,a+1.5)
    var1.set('λ+0.5的值为:'+str(yy1))
    var2.set('λ+1.5的值为:'+str(yy2))

def go():
    Stat()
    Poisson()
top=Tk()
label1=Label(top,text='泊松分布样本大小')
label2=Label(top,text='正态分布样本大小')
label3=Label(top,text='正态分布u')
label4=Label(top,text='泊松分布λ')
label5=Label(top,text='正态分布σ')
label6=Label(top,text='泊松分布样本')
label7=Label(top,text='正态分布样本')

var1=StringVar()
var1.set('λ+0.5的值为:')
label_left=Label(top,textvariable=var1)
var2=StringVar()
var2.set('λ+1.5的值为:')
label_right=Label(top,textvariable=var2)
ent1=Entry(top)#泊松分布样本大小
ent2=Entry(top)#正态分布样本大小
ent3=Entry(top)#正态分布u
ent4=Entry(top)#泊松分布λ
ent5=Entry(top)#正态分布σ
button1=Button(top,text='生成并统计',command=go)#go函数

text1=Text(top)
text2=Text(top)#height width 调整 pack布局
label1.grid_configure(row=1,column=1,columnspan=1,rowspan=1,sticky=W,padx=30)
ent1.grid_configure(row=1,column=1,columnspan=1,rowspan=1,sticky=N)
label4.grid_configure(row=1,column=2)
ent4.grid_configure(row=1,column=2,sticky=E,padx=20)
label2.grid_configure(row=2,column=1,columnspan=1,rowspan=1,sticky=W,padx=30)
ent2.grid_configure(row=2,column=1,columnspan=1,rowspan=1,sticky=N)
label3.grid_configure(row=2,column=1,columnspan=1,rowspan=1,sticky=E)
ent3.grid_configure(row=2,column=2,columnspan=1,rowspan=1,sticky=W)
label5.grid_configure(row=2,column=2)
ent5.grid_configure(row=2,column=2,sticky=E,padx=20)
button1.grid_configure(row=3,column=2,sticky=W,padx=20)
label6.grid_configure(row=4,column=1)
label7.grid_configure(row=4,column=2)
text1.grid_configure(row=5,column=1)
text2.grid_configure(row=5,column=2)
label_left.grid_configure(row=6,column=1)
label_right.grid_configure(row=6,column=2)
top.mainloop()


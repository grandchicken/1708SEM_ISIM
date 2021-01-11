import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
font=FontProperties(fname=r"C:\windows\fonts\simsun.ttc",size=14)


N=9
ind = np.arange(N)
width=0.18
S1=[96,56,78,87,78,56,86,65,52]
S2=[67,37,89,47,36,49,32,25,97]
S3=[89,59,67,37,34,76,23,27,75]
S4=[65,64,45,24,76,87,34,65,24]

fig,ax=plt.subplots()

rects1=ax.bar(ind,S1,width,color='blue')
rects2=ax.bar(ind+width,S2,width,color='yellow')
rects3=ax.bar(ind+2*width,S3,width,color='green')
rects4=ax.bar(ind+3*width,S4,width,color='red')

def autolabel(rects):
    for rect in rects:
        height=rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.,1.05*height,'%d'%int(height),size=7,ha='center',va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5','G6','G7','G8','G9'))
plt.ylabel(u'数值',fontproperties=font)

plt.title(u'数据分析表',fontproperties=font)
plt.yticks(np.arange(0, 110, 10))
plt.legend((rects1[0],rects2[0],rects3[0],rects4[0]),(u'数据1',u'数据2',u'数据3',u'数据4'),prop={'family':'SimHei','size':7},loc='upper right')
plt.show()

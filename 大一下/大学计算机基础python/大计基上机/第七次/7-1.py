import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
pic_font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc',size=14)
plt.figure(figsize=(8,6))

t1=np.arange(1.0,10.0,0.01)
s1=np.sin(1/t1)
s2=np.log(t1)
plt.ylim(-1.2,4.5)
l1,=plt.plot(t1,s1,color='red',linewidth=3)
l2,=plt.plot(t1,s2,color='green',linewidth=3,linestyle='--')


plt.xlabel('时间 (s)',fontproperties=pic_font)
plt.ylabel('电压 (mV)',fontproperties=pic_font)
plt.title('函数图像绘制练习',fontproperties=pic_font)
plt.legend(handles=[l1,l2,],labels=['sin(1/x)','log(x)'])
plt.show()

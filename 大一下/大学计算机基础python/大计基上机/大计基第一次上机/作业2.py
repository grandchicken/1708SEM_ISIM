x1,x2,x3=[float(x) for x in input().split()]
x_av=(x1+x2+x3)/3
import math
x_tot=((x1-x_av)*(x1-x_av)+(x2-x_av)*(x2-x_av)+(x3-x_av)*(x3-x_av))/2
s=math.sqrt(x_tot)
print("{:.2f} {:.2f}".format(x_av,s))


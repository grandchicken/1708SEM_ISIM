n=int(input())
x=[0]*1000
h=[0]*1000
gpa=[0]*1000
fenmu=0
fenzi=0
for i in range(1,n+1):
    x[i]=int(input())
for i in range(1,n+1):
    h[i]=eval(input())
    fenmu+=h[i]
    if(x[i]>=60):
        gpa[i]=4-3*(100-x[i])*(100-x[i])/1600
    if(x[i]<60):
        gpa[i]=0
    fenzi=fenzi+gpa[i]*h[i]
result=fenzi/fenmu
print("%.3f"%result)

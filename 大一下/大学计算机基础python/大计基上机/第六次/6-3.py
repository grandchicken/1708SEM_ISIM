
n=int(input())
A1,A2=[int(x) for x in input().split()]
a=[0]*10000
b=[0]*10000
c=[0]*10000
for i in range(n):
    a[i],b[i]=[int(x) for x in input().split()]
    c[i]=a[i]*b[i]
for i in range(n-1,-1,-1):
    for j in range(i):
        if(c[j]>c[j+1]):
            c[j],c[j+1]=c[j+1],c[j]
            a[j],a[j+1]=a[j+1],a[j]
            b[j],b[j+1]=b[j+1],b[j]
d=[0]*10000
m=[A1]*10000
d[0]=int(A1/b[0])

for i in range(1,n):
    for j in range(0,i):
        
        m[i]*=a[j]
    d[i]=int(m[i]/b[i])
final=max(d)
print(final)

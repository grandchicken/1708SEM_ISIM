n=int(input())
f=[[0]*100 for i in range(100)]
tot=0
s=[int(x) for x in input().split()]
for j in range(n):
    f[0][j]=1
    f[1][j]=1
for i in range(1,n):
    for j in range(0,i):
        
        if(s[i]>s[j]):
            f[0][i]=max(f[0][i],f[0][j]+1)
for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        
        if(s[i]>s[j]):
            f[1][i]=max(f[1][i],f[1][j]+1)
for i in range(0,n):
    tot=max(f[0][i]+f[1][i]-1,tot)
print(n-tot)

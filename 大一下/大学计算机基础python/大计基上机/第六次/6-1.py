n=int(input())
a=[[0]*3 for i in range(300)]
b=[0]*1000
for i in range(n):
    a[i]=[int(x) for x in input().split()]
    b[i]=i+1
tot=[0]*300
for i in range(n):
    for j in range(3):
        tot[i]+=a[i][j]    
for i in range(n-1,0,-1):
    for j in range(0,i):
        if(tot[j]<tot[j+1]):
            tot[j],tot[j+1]=tot[j+1],tot[j]            
            a[j][0],a[j+1][0]=a[j+1][0],a[j][0]
            b[j],b[j+1]=b[j+1],b[j]
        elif(tot[j]==tot[j+1]):
            if(a[j][0]<a[j+1][0]):
                tot[j],tot[j+1]=tot[j+1],tot[j]
                b[j],b[j+1]=b[j+1],b[j]
                a[j][0],a[j+1][0]=a[j+1][0],a[j][0]
            elif(a[j][0]==a[j+1][0]):
                if(b[j]>b[j+1]):
                    tot[j],tot[j+1]=tot[j+1],tot[j]
                    b[j],b[j+1]=b[j+1],b[j]
                    a[j][0],a[j+1][0]=a[j+1][0],a[j][0]
for i in range(5):
    print(b[i],tot[i])

        

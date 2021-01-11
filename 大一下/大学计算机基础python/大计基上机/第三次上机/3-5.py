sum1=0
a,b=[int(x) for x in input().split()]
from math import sqrt
save=[0]*500001
for i in range(2,b+1):
    if(i%2==0) or (i==1):
        save[i]=0
    if(i%2==1) or (i==2):
        save[i]=1


for i in range(3,b+1,2):
    if(save[i]==1):
        for j in range(2*i,b+1,i):
            save[j]=0

for i in range(a,b+1):
    if(save[i]==1):
        sum1+=i
        
print(sum1)


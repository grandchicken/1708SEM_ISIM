n=int(input())
dp={}
data=[]
name=[]
s=[0]*10000
for i in range(0,n):
    data.append(input())
    name.append(input())
    dp[data[i]]=name[i]
k=int(input())
for j in range(0,k):
    s[j]=input()
for j in range(0,k):
    print(dp.get(s[j],"Not Found!"))

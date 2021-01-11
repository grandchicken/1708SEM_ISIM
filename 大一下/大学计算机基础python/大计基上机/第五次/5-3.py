def go(x,y,i,s):
    if(x==y and s[i][x]=='-'):
        return 1
    elif s[i][x:y+1]=='-'*(y-x+1):
        return go(x,y-1,i+1,s)
    else:
        return 0
n=int(input())
s=[0]*100
m=0
for i in range(n):
    s[i]=input()
    s[i]=s[i].strip( )
for i in range(n):
    print(s[i])
for i in range(n):
    for x in range(n-i):
        for y in range(n-i,x,-1):
            if go(x,y,i,s)==1:
                m=max(m,y-x+1)
                break
print(m)
    

'''for i in range(n):
    for j in range(n-i):    
        if(judge(i,j)):
            m[i]+=1
for i in range(n):
    for j in range(n-i):    
        if(judge(i,j)):
            k[j]+=1
for i in range(n):
    print(m[i])
for i in range(n):
    print(k[i])'''

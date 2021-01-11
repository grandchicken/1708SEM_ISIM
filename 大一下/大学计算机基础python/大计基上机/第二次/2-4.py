n=int(input())
for i in range(1,n+1):
    if(n>=2*i-1):
        k=2*i-1
    elif(n<2*i-1):
        k=2*(n-i)+1
    space=(n-k)//2
    for j in range(space):
        print(" ",end="")
    for p in range(k):
        print("*",end="")
    print(" ")
        
        

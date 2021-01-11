N=int(input())
while(N>1):
    if(N%2==1):
        N=3*N+1
        print(N)
    elif(N%2==0):
        N//=2
        if(N!=1):
            print(N)
        
print(N)

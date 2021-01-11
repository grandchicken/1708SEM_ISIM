x=int(input())
n=[0]*1000
m=[0]*1000
for i in range(2,x+1):
    while(x%i==0):       
        x=x//i
        
        m[i]=i
        if(x!=1):
            
            print(m[i],"*"" ",end="")
        if(x==1):
            print(m[i])
        
        
  

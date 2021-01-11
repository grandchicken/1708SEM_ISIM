N=int(input())
x=[0]*100
for i in range(N):
    x[i]=int(input())
N_rest=15-N
tot=0
for i in range(N):
    tot+=x[i]
rest=48-tot
if(rest>N_rest*10):
    print("gg")
elif(rest<=N_rest*10):
    if(rest%N_rest!=0):
        day=rest//N_rest+1
    elif(rest%N_rest==0):
        day=rest/N_rest    
    print(int(day))
    
    

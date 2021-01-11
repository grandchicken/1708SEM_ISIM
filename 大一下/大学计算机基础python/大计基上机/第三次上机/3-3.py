s=input()
save=[]
save=list(s)
long=len(save)
save[0]=chr(ord(save[0])+32)

for i in range(0,long):
    if(ord(save[i])<=90 and ord(save[i])>=65):
        save[i]='_'+chr(ord(save[i])+32)
     

t=""
s=t.join(save)
print(s)
    

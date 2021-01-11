n = int(input())
def lch(i,j):  
    if i == 1 or j == 1:  
        return 1
    elif i == j:  
        return lch(i,j-1)+1
    elif i < j:  
        return lch(i,i)  
     
    else:  
        return lch(i-j,j)+lch(i,j-1)  
  
print(lch(n,n)) 

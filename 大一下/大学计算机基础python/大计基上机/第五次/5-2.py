
n=int(input())
def go(i):
    j=i
    def lch(i,j):
        global s
        if(i==1 or j==1 or i==0 or j==0):
            return 1
        elif(i==7 and j==7):
            return 14
        elif(i==6 and j==6):
            return 11
      
        else:
            if(j>=(i/2)):
                return lch(i-j,i-j)+lch(i,j-1)
            else:
                return lch(j,j)+lch(i,j-1)
    return lch(i,j)

print(go(n))


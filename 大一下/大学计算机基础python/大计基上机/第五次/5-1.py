n=int(input())
def go(i):
    if i==1 or i==0:
        return 1
    else:
        return go(i-1)+go(i-2)
print(go(n))

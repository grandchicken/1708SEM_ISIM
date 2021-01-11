n=int(input())
s=[9]
i=0
while 1:
    a=s[i]
    i+=1
    s.append(10*a)
    s.append(10*a+9)
    if not a%n:
        print(a)
        break
    


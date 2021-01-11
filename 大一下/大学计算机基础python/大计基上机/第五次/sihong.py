def f(matrix,i,x,y):#martix是存输入的列表 i是第i行 x,y分别表示从x开始到y结束
    if y==x and matrix[i][x]=='-':
        return True
    if matrix[i][x:y+1]=='-'*(y-x+1):
        return f(matrix,i+1,x+1,y)
    else:
        return False
n=int(input())
out=0 #out是输出的数
#初始化输入
matrix=[]
for i in range(n):
    matrix.append(input())
for j in range(n):
    for x in range(n):
        for y in range(n,x,-1):
            if matrix[j][x:y+1]=='-'*(y-x+1):
                if f(matrix,j,x,y)==True:
                    out=max(out,y-x+1)
                    break
print(out)

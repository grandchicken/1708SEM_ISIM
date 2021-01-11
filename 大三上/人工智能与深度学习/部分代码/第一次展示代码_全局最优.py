import copy

class step():
    def __init__(self,x):
        self.ma=x #matrix
        self.fa=None #father
        self.dep=0
        self.score=None

def score(temp_com,end):
    sco=0
    count=0
    sco=sco+temp_com.dep
    for i in range(0,3):
        for j in range(0,3):
            if temp_com.ma[i][j]!=end[i][j]:
                count=count+1
    sco=sco+count
    return sco



def input_matrix():
    x=input('Please input the state in the order of 1,2,3 row:')
    temp=[[0]*3 for i in range(3)]
    temp[0][0],temp[0][1],temp[0][2],temp[1][0],temp[1][1],temp[1][2],\
        temp[2][0],temp[2][1],temp[2][2]=map(int,x.split())
    return temp

def extend_node(i,j,temp_com,M,end):
    nodes=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    for node in nodes:
        if 0<= node[0]<=2 and 0 <= node[1] <= 2:
            temp_1_com=step(copy.deepcopy(temp_com.ma))
            temp_1_com.ma[i][j],temp_1_com.ma[node[0]][node[1]]=temp_1_com.ma[node[0]][node[1]],temp_1_com.ma[i][j]
            temp_1_com.fa=temp_com
            temp_1_com.dep=temp_com.dep+1
            M.append(temp_1_com)
    
    return M

def depth_first_search(origin,end):
    #给定了始态和终态
    G=[]
    T=0
    open=[]
    closed=[]
    origin_com=step(origin)
    origin_com.dep=0
    origin_com.score=100
    open.append(origin_com)
    G.append(origin_com)
    while(1):
 
        M=[]
        closed_del=[]
        o_del=[]
        c_del=[]
        if len(open)==0:
            break
        temp_com=open[0]
    
        open.remove(temp_com)
        temp=temp_com.ma
        closed.append(temp_com)

        if temp_com.ma==end:

            print("搜索效率为：",temp_com.dep/(T-t+1))
            print(temp_com.ma)
            while(temp_com.fa!=None):
                print(temp_com.fa.ma)
                temp_com=temp_com.fa
            print("This is G.The length is {}".format(len(G)))

            temp_fa = [G[0]]
            print(G[0].ma)
            print("------------")
            G.remove(G[0])
            while (len(G)):

                del_g = []
                fa_del = []
                for fa in temp_fa:
                    fa_del.append(fa)
                    for node in G:
                        if node.fa == fa:
                            del_g.append(node)
                for g in del_g:
                    print(g.ma)
                    temp_fa.append(g)
                    G.remove(g)
                for f in fa_del:

                    temp_fa.remove(f)
                print('---------')
            print("This is closed.The length is {}".format(len(closed)))
            for c in closed:
                print(c.ma)
            break

        for i in range(0,3):
            for j in range(0,3):
                if temp[i][j]==0:
                    extend_node(i,j,temp_com,M,end)
        for m in M:
            m.score=score(m,end)
        for m in M:
            if temp_com.fa!=None:
                if m.ma==temp_com.fa.ma:
                    M.remove(m)
        for m in M:
            if m not in G:
                G.append(m)
        for m in M:
            for o in open:
                if m.ma==o.ma:
                    o_del.append(m)
                    if m.score<o.score:
                        o.score=m.score
                        o.fa=m.fa
        for o in o_del:
            M.remove(o)
        for m in M:
            for c in closed:
                if m.ma==c.ma:
                    c_del.append(m)
                    if m.score<c.score:
                        c.fa=m.fa
                        c.score=m.score

        for c in c_del:
            M.remove(c)
            
        
        T=T+len(M)
        t=len(M)
        if len(M)!=0:
            for m in M:
                open.append(m)
            for p in range(0,len(open)-1):
                for q in range(0,len(open)-p-1):
                    if open[q].score > open[q+1].score:
                        a=open[q]
                        open[q]=open[q+1]
                        open[q+1]=a
        

#origin=input_matrix()
origin=[[2, 8, 3], [1, 0, 4], [7, 6, 5]]
end=[[1, 2, 3], [8, 0, 4], [7, 6, 5]]
#end=input_matrix()
depth_first_search(origin,end)
#print(open,closed)
#2 8 3 1 0 4 7 6 5
#1 2 3 8 0 4 7 6 5
#extend是检查是否可以扩展
#出现了锁死的现象，互为父节点


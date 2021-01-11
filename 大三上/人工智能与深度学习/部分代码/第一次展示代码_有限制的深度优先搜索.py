import copy

class step():
    def __init__(self,x):
        self.ma=x #matrix
        self.fa=None #father
        self.dep=0


def input_matrix():
    x=input('Please input the state in the order of 1,2,3 row:')
    temp=[[0]*3 for i in range(3)]
    temp[0][0],temp[0][1],temp[0][2],temp[1][0],temp[1][1],temp[1][2],\
        temp[2][0],temp[2][1],temp[2][2]=map(int,x.split())
    return temp

def extend_node(i,j,temp_com,M):
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
    T=0
    #给定了始态和终态
    G=[]

    open=[]
    closed=[]
    origin_com=step(origin)
    origin_com.dep=0
    open.append(origin_com)
    G.append(origin_com)
    while(1):


        M=[]
        del_c=[]
        del_o=[]
        if len(open)==0:
            break
        temp_com=open[0]
        
        while temp_com.dep>4 and len(open)>0:
            open.remove(temp_com)
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

            temp_fa=[G[0]]
            print(G[0].ma)
            print("------------")
            G.remove(G[0])

            while(len(G)):
                del_g = []
                fa_del=[]
                for fa in temp_fa:
                    fa_del.append(fa)
                    for node in G:
                        if node.fa==fa:
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
                        #    print(node.ma
            break

        for i in range(0,3):
            for j in range(0,3):
                if temp[i][j]==0:
                    extend_node(i,j,temp_com,M)

        if len(M)!=0:#在节点是可扩展的情况下
            if temp_com.fa != None:#讨论子节点不是父节点
                for m in M:
                    if m.ma==temp_com.fa.ma:
                       M.remove(m)
            for m in M:
                if m not in G:
                    G.append(m)
            if len(M)!=0 and len(open)!=0:
                for m in M:
                    for o in open:
                        if m.ma==o.ma:
                            if m.dep<o.dep:
                                o.fa=ma.fa

                            del_o.append(m)
            for o in del_o:
                M.remove(o)
                
 
            if len(M)!=0 and len(closed)!=0:
                for m in M:
                    for c in closed:
                        if m.ma==c.ma:
                            if m.dep<c.dep:
                                c.fa=m.fa
                            del_c.append(m)
            for c in del_c:
                M.remove(c)

            T=T+len(M)
            t=len(M)
            if len(M)!=0:
                for m in M:
                    open.append(0)
                    for k in range(len(open) - 1):
                        open[len(open) - 1 - k] = open[len(open) - k - 2]
                    open[0] = m

#origin=input_matrix()
origin=[[2, 0, 3], [1, 8, 4], [7, 6, 5]]
end=[[1, 2, 3], [8, 0, 4], [7, 6, 5]]
#end=input_matrix()
depth_first_search(origin,end)
#print(open,closed)
#2 8 3 1 0 4 7 6 5
#1 2 3 8 0 4 7 6 5
#extend是检查是否可以扩展
#出现了锁死的现象，互为父节点

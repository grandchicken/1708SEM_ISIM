#include<stdio.h>
#include<stdlib.h>
#define MaxNum 100
struct edge{
	int adjvex;
	int weight;
	struct edge *next;
}; 
struct ver{
	int vertex;
	struct edge *link;
};
int k,vi,vj,weight;
struct edge *p,*q;

struct ver G[MaxNum];

void Print(int n,struct ver G[MaxNum]);
void Delete(struct ver G[MaxNum],int *n,int item);
int main(){
	printf("请输入顶点个数:");
	int n;
	scanf("%d",&n);
	printf("请输入边的个数:");
	int e;
	scanf("%d",&e);
	for(k=1;k<=n;k++){
		G[k].vertex = k;
		G[k].link = NULL;
	}
	for(k=1;k<=e;k++){
		printf("请输入顶点偶对及其权值:");
		scanf("%d%d%d",&vi,&vj,&weight);
		p = (struct edge*)malloc(sizeof(struct edge));
		p->adjvex = vj;
		p->weight = weight;
		p->next  = NULL;
		if(G[vi].link == NULL){
			G[vi].link = p;
		} 
		else{
			q = G[vi].link;
			while(q->next!=NULL){
				q = q->next;
			}
			q->next = p;
		}
//		
		p = (struct edge*)malloc(sizeof(struct edge));
		p->adjvex = vi;
		p->weight = weight;
		p->next  = NULL;
		if(G[vj].link == NULL){
			G[vj].link = p;
		} 
		else{
			q = G[vj].link;
			while(q->next!=NULL){
				q = q->next;
			}
			q->next = p;
		}
//
	}
	Print(n,G);
	int item;
	printf("请输入要删除的元素标号:");
	scanf("%d",&item);
	Delete(G,&n,item);
	Print(n,G);
}
//
void Print(int n,struct ver G[MaxNum]){
	int i,j,k;
	struct edge *p;
	for(i=1;i<=n;i++){
		printf("%d ",G[i].vertex);
		if(G[i].link != NULL){
			p = G[i].link;
			while(p!=NULL){
				printf("%d:%d ",p->adjvex,p->weight);
				p = p->next;
			}
			printf("\n");
		}
	}
}
void Delete(struct ver G[MaxNum],int *n,int item){
	int i,k=-1;
	struct edge *p,*q,*r;
	for(i=1;i<=*n;i++){
		if(G[i].vertex == item){
			k = i;
			break;
		} 
	}
	if(k!=-1){
		p = G[k].link;
		for(i=k+1;i<=*n;i++){
			G[i-1].vertex = G[i].vertex;
			G[i-1].link= G[i].link;
		}
		*n = *n - 1;//注意不能用*n--; 
		while(p!=NULL){
			r = p;
			p = p->next;
			free(r);
		}
		for(i=1;i<=*n;i++){
			p = G[i].link;
			while(p!=NULL){
				if(p->adjvex == k){
					if(G[i].link == p){
						G[i].link = p->next;
					}
					else{
						q->next = p->next;
					}
				r = p;
				p = p->next;
				free(r);
				}else{
					if(p->adjvex>k)
						p->adjvex--;
					q = p;
					p = p->next;
					}
				}
			}
		}
	
}


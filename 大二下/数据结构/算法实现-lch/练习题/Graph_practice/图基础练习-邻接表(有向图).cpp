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

void print(int n,struct ver G[MaxNum]);
void Calculate_Du(int n,struct ver G[MaxNum]);//计算出度入度 
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
	}
	//print(n,G);
	Calculate_Du(n,G);
}

void print(int n,struct ver G[MaxNum]){
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
void Calculate_Du(int n,struct ver G[MaxNum]){
	int Chu_D[MaxNum];
	int Ru_D[MaxNum];
	int i;
	struct edge *p,*q;
	for(i=1;i<=n;i++){
		Chu_D[i] = 0;
		Ru_D[i] = 0;
	}
	for(i=1;i<=n;i++){
		if(G[i].link != NULL){
			p = G[i].link;
			while(p!=NULL){
				Ru_D[p->adjvex]++;
				p = p->next;
				Chu_D[i]++; 
			}
		}
	}
	printf("顶点出度分别是:");
	for(i=1;i<=n;i++){
		printf("%d ",Chu_D[i]);	
	}
	printf("顶点入度分别是:");
	for(i=1;i<=n;i++){
		printf("%d ",Ru_D[i]);
	}
}

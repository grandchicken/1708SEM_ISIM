#include<stdio.h>
#include<stdlib.h> 
struct node{
	int data;
	struct node * link;
};

struct node *H = NULL; 
int n;
void creat(struct node **H,int n);

int main(){
	int n,m,k;
	printf("请分别输入n，m，k:"); 
	scanf("%d%d%d",&n,&m,&k);
	creat(&H,n);
	struct node *p,*q;
	p = H;
	int i;
	printf("输出为：");
  	for (i=1; i<k; i++) p = p->link;  
  	while (p->link != p){ 
    	for (i=1; i<m; i++) {
    		q=p;
			p = p->link; 
			}
    	printf("%d ",p->data); 
    	q->link = p->link;  
    	p = q->link;
  	} 
  	printf("%d \n",p->data);  
  	return 0;
}


void creat(struct node **H,int n){
	struct node *p,*r;
	int i = 1;
	while(i<=n){
		p = (struct node *)malloc(sizeof(struct node)); 
		p->data = i;
		p->link = NULL;
		if(*H == NULL){
			*H = p;
		}else{
			r->link = p;
		}
		r = p;
		i++;
	}
	r->link=*H;
} 

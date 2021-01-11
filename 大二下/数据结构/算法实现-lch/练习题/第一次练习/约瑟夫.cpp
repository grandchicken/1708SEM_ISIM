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
	scanf("%d%d%d",&n,&m,&k);
	creat(&H,n);
	struct node *p;
	p = H;
	int i;
	
  	for (i=1; i<k-1; i++) p = p->link;  
  	while (p->link != p){ 
    	for (i=1; i<m; i++) {
			p = p->link; 
			}
    	printf("%d ",p->link->data); 
    	p->link = p->link->link;  
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

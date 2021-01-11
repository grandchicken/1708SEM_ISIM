#include<stdio.h>
#include<stdlib.h>
struct node{
	int coef;
	int exp;
	struct node *link;
};

struct node *HA = NULL,*HB = NULL,*HC = NULL; 
struct node *d = NULL;

void creat(struct node **H, int *A_exp,int *A_coef,int n);
void add(struct node **H,struct node **d,int exp,int coef);
void PLUS(struct node *HA,struct node *HB,struct node **HC,struct node **d);
int A_exp[1024];
int A_coef[1024]; 

int B_exp[1024] ;
int B_coef[1024] ;

int main(){
	int i ;
	int n , m , k; 
	printf("请输入A多项式共有几项：");
	scanf("%d",&n);
	printf("请依次输入A多项式各项的指数：");
	for(i=0;i<n;i++){
	scanf("%d",&k);
	A_exp[i] = k;
	}
	printf("请依次输入A多项式各项的指系数：");
	for(i=0;i<n;i++){
		scanf("%d",&k);
		A_coef[i] = k;
	}
	printf("请输入B多项式共有几项：");
	scanf("%d",&m);
	printf("请依次输入B多项式各项的指数：");
	for(i=0;i<m;i++){
	scanf("%d",&k);
	B_exp[i] = k;
	}
	printf("请依次输入B多项式各项的系数：");
	for(i=0;i<m;i++){
		scanf("%d",&k);
		B_coef[i] = k;
	}
	
	
	creat(&HA,A_exp,A_coef,n);
	creat(&HB,B_exp,B_coef,m);
	
	
	
	PLUS(HA,HB,&HC,&d);
	
	struct node* M = NULL,*N = NULL;
	M = HC;
	N = HC;
	if(M==0){
		printf("1");
	} 
	printf("多项式C各项的指数为：");
	while(M!=0){
		printf("%d ",M->exp);
		M = M->link;
	}
	printf("多项式C各项的系数为："); 
	while(N!=0){
		printf("%d ",N->coef);
		N = N->link;
	}
	
	return 0;
}
void creat(struct node **H,int *A_exp,int *A_coef ,int n){
	struct node *p =NULL,*r = NULL;
	int i;
	for (i=0;i<n;i++){
	p = (struct node*)malloc(sizeof(struct node));
	p->exp = A_exp[i];
	p->coef = A_coef[i];
	p->link = NULL;
	
	//r = p;
	
	if((*H) == NULL){
		*H = p;
	}else{
		r->link = p;
	}
	r = p;
	}	
}

void add(struct node **H,struct node **d,int exp,int coef){
	struct node *p = NULL;
	p = (struct node*)malloc(sizeof(struct node));
	p->link = NULL;
	p->exp = exp;
	p->coef = coef;
	if(*H == NULL){
		*H = p;
	}else{
		(*d)->link = p;
	}
	*d = p;
}
void PLUS(struct node *HA,struct node *HB,struct node **HC,struct node **d){
	struct node *p = NULL,*q = NULL;
	p = HA; q = HB;
	while(p!=0 && q!=0){
		if(p->exp > q->exp){
			add(HC,d,p->exp,p->coef);
			p = p->link;
		}
		else if(p->exp < q->exp){
			add(&(*HC),&(*d),q->exp,q->coef);
			q = q->link;
		}else{
			if(p->coef + q->coef !=0){
				add(&(*HC),&(*d),q->exp,q->coef+p->coef);
			}
			p = p->link;q = q->link;
		}
	}
	while(p!=0){
		add(&(*HC),&(*d),p->exp,p->coef);
		p = p->link;
	}
	while(q!=0){
		add(&(*HC),&(*d),q->exp,q->coef);
		q = q->link;
	}
}



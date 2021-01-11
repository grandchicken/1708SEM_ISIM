#include<stdio.h>
#include<stdlib.h>
struct node{
	int data;
	struct node *Lchild;
	struct node *Rchild;
};
struct node *p ,*q;
struct node *T = NULL; 
void Setup(int A[],int n);
void MidOrder_TD(struct node *T);
int main(){
	int n;
	printf("请输入树中元素的个数:");
	scanf("%d",&n);
	int A[n];
	int i;
	printf("请分别输入树中元素:");
	for(i=0;i<n;i++){
		scanf("%d",&A[i]);
	}
	printf("树建立完成!\n");
	Setup(A,n);
	printf("中序遍历结果为:");
	MidOrder_TD(T);
	
}
void Setup(int A[],int n){
	struct node *x;
	int i;
	for(i=0;i<n;i++){
		x = (struct node*)malloc(sizeof(struct node));
		x->Lchild = NULL;
		x->Rchild = NULL;
		x->data = A[i];
		if(T == NULL){
			T = x;
		}
		else{
			p = T;	
			while(p!=NULL){
				q = p;
				if(x->data < p->data) p = p->Lchild;
				else p = p->Rchild;
			}
				if(x->data < q->data) q->Lchild = x;
				else q->Rchild = x;
		}
	}
}
void MidOrder_TD(struct node *T){
	if(T!=NULL){
		MidOrder_TD(T->Lchild);
		printf("%d ",T->data);
		MidOrder_TD(T->Rchild);
	}
}

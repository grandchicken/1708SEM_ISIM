//创建一个链表 
#include<stdio.h>
#include<stdlib.h> 
struct chain{
	int data;
	struct chain *next;
};
struct chain *p,*q;
struct chain *head = NULL;

int n = 10;
int main(){
	int i;
	for(i=1;i<=n;i++){
		p = (struct chain*)malloc(sizeof(struct chain));
		p->data = i;
		p->next = NULL;
		if(head == NULL){
			head = p;
		}else{
			q->next = p;
		}
		q = p;
	}
	while(head!=0){
	
	printf("%d",head->data);
	head = head->next;
}
} 

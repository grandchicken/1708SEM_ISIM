#include<stdio.h>
int Stack[100]; 
int Top = -1;
int main(){
	int n ;
	scanf("%d",&n);
	while(n>0){
		int i;
		i = n%16;
		Top++;
		Stack[Top] = i;
		
		n = n/16;
	}
	while(Top > -1){
		if(Stack[Top] == 10){
			printf("A");
		}
		else if(Stack[Top] == 11){
			printf("B");
		}
		else if(Stack[Top] == 12){
			printf("C");
		}
		else if(Stack[Top] == 13){
			printf("D");
		}
		else if(Stack[Top] == 14){
			printf("E");
		}
		else if(Stack[Top] == 15){
			printf("F");
		}
		else if(Stack[Top]>=0 || Stack[Top]<=9){
			printf("%d",Stack[Top]);
		}
		Top--;
	}
} 

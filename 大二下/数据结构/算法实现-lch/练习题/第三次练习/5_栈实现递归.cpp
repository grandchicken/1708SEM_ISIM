#include<stdio.h>
int Stack[100]; 
int Top = -1;

int main(){
	int n ;
	int m = 1,sum = 1 ;
	scanf("%d",&n);
	while(Top>=-1){
		if(n!=0){
			Top++;
			Stack[Top] =n;
			n = n/2;
		}else{
			sum = sum*m;
			if(Top>=0){
				m = Stack[Top];
				
			}
			Top--;
		}
	}
	printf("%d",sum);
}

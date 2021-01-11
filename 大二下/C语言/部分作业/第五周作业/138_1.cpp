#include<stdio.h>
int main(){
	int numYrs;
	printf("请输入存款年数:");
	scanf("%d",&numYrs);
	float r;
	if(numYrs>5){
		r = 0.075;
	}else{
		r = 0.054;
	}
	printf("%f",r);
} 

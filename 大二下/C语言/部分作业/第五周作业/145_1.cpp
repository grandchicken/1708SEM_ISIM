#include<stdio.h>
int main(){
	int i;
	printf("请输入你的分数:");
	scanf("%d",&i);
	printf("你的等级为:");
	if(i>=90){
		printf("A");		
	}
	else if(i>=80 && i<90){
		printf("B");
	}
	else if(i>=70 && i<80){
		printf("C");
	}
	else if(i>=60 && i<70){
		printf("D");
	}
	else if(i<60){
		printf("F");
	}	
	
}

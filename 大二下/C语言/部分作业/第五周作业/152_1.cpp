#include<stdio.h>
int main(){
	int i;
	printf("请输入一个代码:");
	scanf("%d",&i);
	switch(i){
		case 1:printf("3M公司");break;
		case 2:printf("万胜公司");break;
		case 3:printf("索尼公司");break;
		case 4:printf("威宝公司");break;
		default:printf("input error"); 
	}
} 

#include<stdio.h>
int main(){
	char s;
	printf("请输入一个字符:");
	scanf("%c",&s);
	if(s<='Z'&& s>='A'){
		printf("%d",s-'A'+1);
	}else{
		printf("不是大写字符！");
	}
} 

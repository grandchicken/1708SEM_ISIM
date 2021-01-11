#include<stdio.h>
int main(){
	char s;
	printf("请输入一个字符:");
	scanf("%c",&s);
	if(s<='z'&& s>='a'){
		printf("%d",s-'a'+1);
	}else{
		printf("不是小写字符！");
	}
} 

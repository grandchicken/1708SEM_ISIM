#include<stdio.h>
int main(){
	int m;
	printf("输入一个待反转的正整数:"); 
	scanf("%d",&m);
	if(m<=0){
		printf("ERROR INPUT!");
		return -1;
	} 
	printf("结果为:");
	while(m!= 0){
		printf("%d",m%10);
		m = m/10;
	}
}

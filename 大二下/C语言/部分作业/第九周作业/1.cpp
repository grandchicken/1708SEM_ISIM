//1
#include<stdio.h>
void inverse(int n);

int main(){
	int n;
	printf("请输入一个正整数:");
	scanf("%d",&n);
	printf("结果是:");
	inverse(n);
} 
void inverse(int n){
	
	if(n/10 == 0){
		printf("%d",n);
	}else{
		printf("%d",n%10);
		inverse(n/10);
	}
}

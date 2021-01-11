//4.286_6 
#include<stdio.h>
int gcd(int a,int b);
int main(){
	int a,b;
	printf("请输入两个正整数:");
	scanf("%d%d",&a,&b);
	if(a>b){
		printf("最大公因数为:%d",gcd(a,b));
	}else{
		printf("最大公因数为:%d",gcd(b,a));
	} 
}
int gcd(int a,int b){
	if(a%b == 0){
		return b;
	}
	else{
		return gcd(b,a%b);
	}
}

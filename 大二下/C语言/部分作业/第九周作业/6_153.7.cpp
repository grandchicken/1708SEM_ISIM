//6.153_7
#include<stdio.h>
double Power(double x,int n);
int main(){
	double x;int n;
	printf("请输入要计算的x值和幂次:"); 
	scanf("%lf%d",&x,&n);
	printf("%lf",Power(x,n));
} 
double Power(double x,int n){
	if(n==0){
		return 1;
	}
	if(n%2==1){
		return x*Power(x,n-1);
	}
	if(n%2==0){
		return Power(x,n/2)*Power(x,n/2);
	}
}

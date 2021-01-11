#include<stdio.h>
#include<math.h>
int main(){
	float A,X,R,N;
	printf("输入初始存款额:");
	scanf("%f",&X);
	printf("输入存期:");
	scanf("%f",&N);
	printf("输入年利率(百分比前的数字):");
	scanf("%f",&R);
	A = X*pow((1.0+R/100),N);
	printf("%f",A);
	
}

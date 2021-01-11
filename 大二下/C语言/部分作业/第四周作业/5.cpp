#include<stdio.h>
#include<math.h>
int main(){
	float a,b;
	printf("输入一个数:");
	scanf("%f",&a);
	b = pow(a,0.25);
	printf("四次方根为：%f",b);
	return 0;
}

//7
#include<stdio.h>
void larger_of(double *x,double *y);
int main(){
	double x,y;
	printf("请输入x:");
	scanf("%lf",&x);
	printf("请输入y:");
	scanf("%lf",&y);
	larger_of(&x,&y);
	printf("修改后的两数值为:x=%lf,y=%lf",x,y);
	 
} 
void larger_of(double *x,double *y){
	if(*x > *y){
		*y = *x;
	}else{
		*x = *y;
	}
}

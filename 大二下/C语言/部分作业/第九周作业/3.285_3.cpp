//3.285_3
#include<stdio.h>
float function(float a,float b,int n);
float sum_function(float a,float d,int n);
int main(){
	float a,d;
	int n; 
	printf("请分别输入首项a,公差d和要计算的项数n:");
	scanf("%f%f%d",&a,&d,&n);
	printf("第n项为:%f\n",function(a,d,n));		
	printf("前n项和为:%f",sum_function(a,d,n));
}
float function(float a,float d,int n){
	static float temp = a;
	if(n == 1){
		float re;
		re = temp;
		temp = a;
		return re;
	}else{
		temp = temp+d;
		return function(a,d,n-1);
	}
}

float sum_function(float a,float d,int n){
	static float sum = function(a,d,1);
	if(n == 1){
		float re;
		re = sum;
		sum = function(a,d,1);
		return re;
	}else{
		sum = function(a,d,n)+sum;
		return sum_function(a,d,n-1);
	}
}


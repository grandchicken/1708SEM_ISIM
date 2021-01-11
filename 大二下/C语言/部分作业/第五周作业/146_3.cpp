#include<stdio.h>
int main(){
	printf("请输入一个温度值和它对应的单位，中间空一格:");
	float i;
	char s;
	float Celsius,Fahrenheit;
	scanf("%f %c",&i,&s);
	
	if(s == 'f'){
		printf("输入的华氏温度为:%f\n",i);
		Fahrenheit = i;
		Celsius = (5.0/9.0)*(Fahrenheit-32.0);
		printf("转化为摄氏温度为:%f",Celsius);
	}
	else if(s == 'c'){
		printf("输入的摄氏温度为:%f\n",i);
		Celsius = i;
		Fahrenheit = (9.0/5.0)*Celsius+32.0;
		printf("转化为华氏温度为:%f",Fahrenheit);
	}else{
		printf("输入的程序不正确");
	}
} 


#include<stdio.h>
int main(){
	float x1,y1,x2,y2;
	printf("x1:");
	scanf("%f",&x1);
	printf("y1:");
	scanf("%f",&y1);
	printf("x2:");
	scanf("%f",&x2);
	printf("y2:");
	scanf("%f",&y2);
	float x_m,y_m;
	x_m = (x1+x2)/2;
	y_m = (y1+y2)/2;
	printf("%f %f",x_m,y_m);
	return 0;
} 

#include<stdio.h>
#include<math.h>
#define Pi 3.1415926
int main(){
	double rad = 22.8*Pi/180;
	double t=0;
	double x,y; 
	printf("Ê±¼ä(s)  x(Ó¢³ß)  y(Ó¢³ß)\n");
	while(t<=10){
		x = 500*t*cos(rad);
		y = 500*t*sin(rad);
		printf("%4.1f%10.3f%10.3f\n",t,x,y);
		t+=0.5;
	}
}

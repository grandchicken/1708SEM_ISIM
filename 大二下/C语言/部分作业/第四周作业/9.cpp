#include<stdio.h>
#include<math.h>
int main() {
	float h;
	float g = 1.67;
	printf("请输入下落高度:"); 
	scanf("%f",&h);
	float v;
	int i;
	for(i=0;i<=2;i++){
	v = sqrt(2*g*h);
	printf("第%d次下落:\n",i+1); 
	printf("v = %f\n",v);
	h = h*2/3;
	printf("h = %f\n",h);
	}
}

#include<stdio.h>
#include<math.h>
int main(){
	int x,y;
	printf("请分别输入x与y的值：");
	scanf("%d",&x);
	scanf("%d",&y);
	float d;
	d = sqrt(x*x+y*y);
	int e;
	e = round(d); 
	printf("距离为:%d",e);
}

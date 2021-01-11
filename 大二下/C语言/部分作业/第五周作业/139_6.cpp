#include<stdio.h>
#include<math.h> 
int main(){
	float a,b,c,area;
	printf("请分别输入三角形的三边:");
	scanf("%f%f%f",&a,&b,&c);
	float s;
	s = (a+b+c)/2;
	area = sqrt(s*(s-a)*(s-b)*(s-c));
	if(area<=0){
		printf("所输入三边无法组成一个三角形");
	}else{
		printf("面积为:%f",area);
	}
}
//书上给的海伦公式错了吧！！ 

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>
#define pi 3.1415926
#define loops 50000
#define lanbuda 3//这里改变参数lanbuda的值 
double Exp(double theta);
int main(){
	double A[loops];
	int i = 0;
	double sum = 0;

	srand(time(NULL));
	while(i<loops){
		A[i] = Exp(lanbuda);
		sum+=A[i];
		i++;
	}
	printf("生成%d个服从EXP(%d)的随机数:",loops,lanbuda);
	for(i=0;i<loops;i++){
		printf("%f ",A[i]);
	}
	printf("\n以下为对该分布的检验:\n");
	double E;
	E = 1.0*sum/loops;
	printf("参数为%d的指数分布的数学期望为:%f",lanbuda,E);
	
	
}
double Exp(double theta){
	double x;
	double m;
	m = (double)(rand()%1000)/1000;
	while(m==0){
		m = (double)(rand()%1000)/1000;
	}
	x = (-1.0/theta)*(log(1-m));
	return x;
}

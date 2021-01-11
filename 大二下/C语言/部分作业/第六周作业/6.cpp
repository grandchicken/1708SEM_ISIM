#include<stdio.h>
#define MAXNUM 100000
#define MIN 0
#define MAX 10000000.0
int main(){
	double A[MAXNUM];
	int i=0;
	double min = MAX;
	double max = MIN;
	while (true){
		printf("请输入一个正数：");
		scanf("%lf",&A[i]);
		if(A[i]<=0){
			break;
		}
		if(A[i]<min) min = A[i];
		if(A[i]>max) max = A[i];
		i++;
	}
	printf("最大非负数为:%f",max);
	printf("最小非负数为:%f",min);
	
	
	
} 

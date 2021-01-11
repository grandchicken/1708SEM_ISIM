#include<stdio.h>
#include<math.h>
double calculate(int n);
int main(){
	printf("请输入n的值:");
	int n;
	scanf("%d",&n);
	printf("计算得到Π值为:%f",calculate(n));
}
double calculate(int n){
	double sum = 0;
	int i;
	for(i=1;i<=n;i++){
		sum = sum + pow(i,-2);
	}
	double re;
	re = sqrt(6*sum); 
	return re;
	
}

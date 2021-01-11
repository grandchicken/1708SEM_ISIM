//5
#include<stdio.h>
#include<math.h>
int main(){
	printf("Please enter n:");
	int n;
	scanf("%d",&n);
	int i;
	int top = 1;
	int bottom = 2;
	int top_pre = 1;
	int	bottom_pre = 1;
	int top_temp,bottom_temp; 
	double sum = 1;
	for(i=1;i<=n-1;i++){
		sum += 1.0*pow(-1,i)*top/bottom;
		top_temp = top_pre;
		bottom_temp = bottom_pre; 
		top_pre = top;
		bottom_pre = bottom;
		top = top+top_temp;
		bottom = bottom+bottom_temp;
	}
	printf("%f",sum);
} 

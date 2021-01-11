#include<stdio.h>

#define out_loop 7
#define in_loop 10

int main(){
	int i,j;
	double initial_rate = 0.06;
	double basic[out_loop];
	printf("年份：      ");
	for(i=1;i<=in_loop;i++){
		 printf("第%d年      ",i);
	}
	printf("\n");
	int m=6; 
	for(i=1;i<=out_loop;i++){
		basic[i-1] = 1000;
		printf("利率为%%%2d ",m+i-1);
		for(j=1;j<=in_loop;j++){
			basic[i-1] = basic[i-1] * (1+(initial_rate+double(i-1)/100));
			printf("%10.3f ",basic[i-1]);
		}
		printf("\n");
	}	
}

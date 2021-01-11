//1.49_6
#include<stdio.h>
int main(){
	int j_1,j_2,j_3,j_4,j_5,j_6,j_7,j_8;
	int j_9,j_10,j_11,j_12;
	printf("Enter the first 12 digits of EAN:");
	scanf("%1d%1d%1d%1d%1d%1d%1d%1d%1d%1d%1d%1d",
	&j_1,&j_2,&j_3,&j_4,&j_5,&j_6,&j_7,&j_8,&j_9,
	&j_10,&j_11,&j_12);
	int sum_1,sum_2;
	sum_1 = j_2+j_4+j_6+j_8+j_10+j_12;
	sum_2 = j_1+j_3+j_5+j_7+j_9+j_11;
	int re_3;
	re_3 = 9-((sum_1*3+sum_2)-1)%10;
	printf("Check digit:%d",re_3);
} 

#include<stdio.h>
#define blank 12
int main(){
	int i;
	for(i=0;i<blank;i++){
		printf(" ");
	}
	printf("DEPRECIATION SCHEDULE\n");
	for(i=0;i<blank;i++){
		printf(" ");
	}
	printf("---------------------\n");
	printf("\n");
	for(i=0;i<blank+6;i++){
		printf(" ");
	}
	printf("END-OF-YEAR ACCUMULATED\n");
	printf("YEAR DEPRECIATION    VALUE    DEPRECIATION\n");
	printf("---- ------------    -----    ------------\n");
	int const_money = 4000;
	int total = 28000;
	for(i=1;i<=7;i++){
		printf("%d%11d%14d%11d\n",i,const_money,total-i*const_money,const_money);
	}
	
}

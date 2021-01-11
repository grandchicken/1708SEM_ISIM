//6.281-5
#include<stdio.h>
void yrCalc(long tot,int *year,int *month,int *day);
int main(){
	printf("请输入从1900年到目前的总天数:");
	long tot;
	int year,month,day;
	scanf("%ld",&tot);
	yrCalc(tot,&year,&month,&day);
	printf("当前为%d年%d月%d日",year,month,day);
	
}
void yrCalc(long tot,int *year,int *month,int *day){
	*year = 1900 + tot/365;
	tot = tot%365;
	*month = 1+tot/30;
	tot = tot%30;
	*day = 1+tot;
}

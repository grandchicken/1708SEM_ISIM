//4.275-6
#include<stdio.h>
void Date(int yyyymmdd,int *year,int *month,int *date);
int main(){
	int yyyymmdd;
	printf("输入一个yyyymmdd的日期:");
	scanf("%d",&yyyymmdd);
	int year,month,date;
	Date(yyyymmdd,&year,&month,&date);
	printf("year:%d month:%d date:%d",year,month,date);
	
}
void Date(int yyyymmdd,int *year,int *month,int *date){
	*year = yyyymmdd/10000;
	*month = (yyyymmdd%10000)/100;
	*date = yyyymmdd%100;
}

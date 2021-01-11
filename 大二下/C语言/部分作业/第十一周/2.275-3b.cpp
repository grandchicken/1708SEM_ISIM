//2.275-3b
#include<stdio.h>
void sec(int a,int b,int c,int *totSec);
int main(){
	printf("请输入以小时、分钟、秒数确定的时间，格式为*h*min*s:");
	int a,b,c;
	scanf("%dh%dmin%ds",&a,&b,&c);
	int totSec;
	sec(a,b,c,&totSec);
	printf("总秒数为:%ds",totSec); 
} 
void sec(int a,int b,int c,int *totSec){
	*totSec = 3600*a+60*b+c;
}

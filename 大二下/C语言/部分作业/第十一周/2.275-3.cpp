//2.275-3a 
#include<stdio.h>
int sec(int a,int b,int c);
int main(){
	printf("请输入以小时、分钟、秒数确定的时间，格式为*h*min*s:");
	int a,b,c;
	scanf("%dh%dmin%ds",&a,&b,&c);
	int totSec;
	totSec = sec(a,b,c);
	printf("总秒数为:%ds",totSec); 
} 
int sec(int a,int b,int c){
	return 3600*a+60*b+c;
}

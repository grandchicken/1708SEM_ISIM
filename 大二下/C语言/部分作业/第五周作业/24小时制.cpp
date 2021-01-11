#include<stdio.h>
int main(){
	int i,j;
	printf("请输入当前时间，注意冒号用英文冒号:");
	scanf("%d:%d",&i,&j);
	if(i>12 && i<=24){
		if(j<10 && j>=0){
			printf("%d:0%dPM",i-12,j);
		} 
		else
		printf("%d:%dPM",i-12,j);
	}
	else if(i==12){
		if(j<10 && j>=0){
			printf("%d:0%dPM",i,j);
		}
		else
		printf("%d:%dPM",i,j);
	}
	else if(i<12 && i>=0){
		if(j<10 && j>=0){
			printf("%d:0%dPM",i,j);
		}
		else
		printf("%d:%dAM",i,j);
	}else{
		printf("ERROR,请输入合法的时间值");
	}

	
} 

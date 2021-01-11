#include<stdio.h>
#include<stdlib.h> 
#include<time.h>
int main(){
	srand(time(NULL));
	int m;
	int i = 0;
	int a = 0;
	int out_home = 0;
	int in_home = 0;
	while(i<500){
		while (1){
			m = rand()%2;
			if(m==0){
				a-=1;
			}else{
				a+=2;
			}
			if(a==0){
				out_home+=1;
				break;
			}
			if(a>=10){
				in_home+=1;
				break;
			}
		}
		i++;
		a = 0;
	}
	
	double rate;
	rate = 1.0*in_home/500;
	printf("狗回到家的概率为：%f",rate);
	
	return 0;
	
} 

//5.286_7
#include<stdio.h>
#define time 5 //模拟五个用户输入 
int inverse(int n);

int main(){
	int n;
	int i;
	printf("在下面的%d次输入中，如果是回文数则返回1，不是则返回0\n",time); 
	for(i=0;i<time;i++){
		printf("请输入一个正整数:");
		scanf("%d",&n);
		if(n == inverse(n)){
			printf("1\n");
		}else{
			printf("0\n");
		}
	}
}
int inverse(int n){
	static int temp = 0;
	if(n/10 == 0){
		int re;
		re = temp;
		temp = 0; 
		return re*10+n;
	}else{
		temp = temp*10+n%10;
		return inverse(n/10);
	}
}

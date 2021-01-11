#include<stdio.h>
int num_digits(int n,int k);
int main(){
	int n,k;
	printf("请输入正整数n和需要返回的第k位数字\n");
	printf("n = ");
	scanf("%d",&n);
	printf("k = ");
	scanf("%d",&k);
	if(k<=0 || n<=0) {
		printf("INPUT ERROR!");
		return -1;
	}
	printf("结果是:%d",num_digits(n,k));
}
int num_digits(int n,int k){
	int i = 0;
	int re;
	while(i<k){
		if(n!=0) re = n%10;
		else re = -1;
		n = n/10;
		i++;
	}
	return re;
}

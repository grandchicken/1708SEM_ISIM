#include<stdio.h>
#include<stdlib.h>
int main(){
	int n0,m0,m,n;
	printf("请输入待约简的分数:");
	scanf("%d/%d",&m0,&n0);
	int i = 2;
	int flag = 1;
	if(n0==0){
		printf("错误：分母不能为0");
		return 0;
	}
	printf("约简后的分数为:");
	if(m0*n0<0) printf("-");
	if(m0==0){
		printf("0");
		return 0;
	}
	m = abs(m0);
	n = abs(n0);
	if(m>n){
		while (flag ==1){
			if(n==1) flag = 0;
			for(i=2;i<=n;i++){
				if(n%i==0 && m%i==0){
					m = m/i;
					n = n/i;
					break;
				}
				if( i==n) flag = 0;
			}
		}
		if(n==1){
			printf("%d",m/n);
		}else{
			printf("%d/%d",m,n);
		}
	}
	else if(m<n){
		while (flag ==1){
			if(n==1) flag = 0;
			for(i=2;i<=n;i++){
				if(n%i==0 && m%i==0){
					m = m/i;
					n = n/i;
					break;
				}
				if( i==n) flag = 0;
			}
		}
		printf("%d/%d",m,n);
	}
	else if(m==n){
		printf("1");
	}
}

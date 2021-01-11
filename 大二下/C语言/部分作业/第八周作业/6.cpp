//6
#include<stdio.h>
#include<stdlib.h>
void simplify(int m0,int n0);
int main(){
	int a1,a2,b1,b2;
	printf("请输入两个分数加和的形式:");
	scanf("%d/%d+%d/%d",&a1,&a2,&b1,&b2);
	int top,bottom;
	top = a1*b2+a2*b1;
	bottom = a2*b2;
	printf("结果为:");
	simplify(top,bottom);
}
void simplify(int m0,int n0){
	int i,m,n;
	int flag = 1;
	if(m0*n0<0) printf("-");
	if(m0==0){
		printf("0");
		return;
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

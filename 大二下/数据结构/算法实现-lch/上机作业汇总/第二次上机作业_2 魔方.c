#include<stdio.h>
int main(){
	int n ;
	printf("请输入矩阵阶数n(n为奇数)：");
	scanf("%d",&n);
	int A[n][n];
	int i,j;
	for(i=0;i<=n-1;i++){
		for(j=0;j<=n-1;j++){
			A[i][j] = 0;
		} 
	}
	i = 0;
	j = (n-1)/2;
	int num;
	for(num = 1;num<=n*n;num++){
		if(A[i][j]!=0){
			i = i+2;
			j = j+1;
			
		}
		A[i][j] = num;
		i--;j--;
		
		if(i<0&&j<0){
			i=i+2;
			j++;
		}
		if(j<0 &&i>=0){
			j = n+j;
		}
		if(i<0 &&j>=0){
			i = n+i;
		}
		
	}
	printf("输出幻方为：\n");
	for(i=0;i<=n-1;i++){
		for(j=0;j<=n-1;j++){
			printf("%d ",A[i][j]);
		}
		printf("\n");
	}
 	
}

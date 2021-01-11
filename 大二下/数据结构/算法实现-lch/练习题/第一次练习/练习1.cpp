//删除所有数字2 
#include<stdio.h>
int main(){
	int A[6] = {1,2,3,2,4,5};
	int n = 5;
	int i = 0;
	while (i <= n){
		if(A[i] == 2){
			for(int j = i;j<5;j++){
				A[j] = A[j+1];
				
			}
			n = n-1;
		}else{
			i++;
		}
		
	}
/* 输出检验 
	for(int i = 0;i<=n;i++){
		printf("%d ",A[i]);
	}
	*/ 
	return 0;
} 

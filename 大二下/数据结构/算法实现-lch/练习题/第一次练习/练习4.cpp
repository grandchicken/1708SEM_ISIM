//删除开始时序号是奇数的元素，从0开始 
#include<stdio.h>
int main(){
	int A[11] = {12,3124,453,4,5,6,7,8,9,10,12};
	int n = 11;
	for(int i = 0;i<=(n-1)/2;i++){
		A[i] = A[2*i];
	}
	if(n%2==0){
		n = n/2;
	}else{
		n = (n+1)/2;
	}
	for(int i = 0;i<=n-1;i++){
		printf("%d ",A[i]);
	}
} 

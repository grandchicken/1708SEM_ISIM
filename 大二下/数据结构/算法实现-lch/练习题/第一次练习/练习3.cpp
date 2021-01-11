//B整体插入到A的第四个元素和第五个元素之间 
#include<stdio.h>
int main(){
	int A[15] = {1,2,3,4,5,6,7,8,9,10};
	int num = 15;
	int n = 10;
	int B[5] = {1,2,3,4,5};
	int m = 5;
	
	for(int i =num-1;i>=4+m;i--){
		A[i] = A[i-5];
}	
	for(int i = 4;i<=4+m-1;i++){
		A[i] = B[i-4];
	}
	for(int i = 0;i<=n+m-1;i++){
		printf("%d ",A[i]);
	}
} 

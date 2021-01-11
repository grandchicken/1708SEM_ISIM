//用最小交换次数让奇数处于下标低的一端，偶数处于下标高的一端 
#include<stdio.h>
int main(){
	int A[10] = {1,2,3,4,5,6,7,8,9,10};
	int m = 0;
	int n = 9;
	for (int i = 0;i<=n;i++){
		if(A[i]%2==1){
			int temp;
			temp = A[m]; 
			A[m] = A[i];
			A[i] = temp;
			m++; 
		}
	}
	for(int i=0;i<=n;i++){
		printf("%d ",A[i]);
	}
	return 0;
} 

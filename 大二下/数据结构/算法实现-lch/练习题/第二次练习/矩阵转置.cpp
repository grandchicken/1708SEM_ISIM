#include<stdio.h>
int main(){
	int n = 3; 
	int A[3][3] = {{1,2,4},{5,6,2},{1,4,2}};
	int B[3][3];
	int i,j;
	for(j=0;j<=n-1;j++){
		for(i=0;i<=n-1;i++){
			B[j][i] = A[i][j];
		} 
	}
	for(i=0;i<=n-1;i++){
		for(j=0;j<=n-1;j++){
			printf("%d ",B[i][j]);
		}
		printf("\n");
	}
	
}

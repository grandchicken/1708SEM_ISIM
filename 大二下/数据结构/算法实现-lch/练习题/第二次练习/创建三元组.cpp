#include<stdio.h>
int A[3][4] = {{0,1,2,0},{0,0,0,3},{2,2,0,0}};
int B[12][3];
int main(){
	int i,j;
	int m = 3;
	int n = 4;
	int k = 0;
	B[0][0] = m;
	B[0][1] = n;
	for(i=0;i<=m-1;i++){
		for(j=0;j<=n-1;j++){
			if(A[i][j]!=0){
				B[k+1][0] = i+1;
				B[k+1][1] = j+1;
				B[k+1][2] = A[i][j];
				k++;	
			}
		}
	}
	B[0][2] = k;
	for(i=0;i<=k;i++){
		for(j=0;j<=2;j++){
			printf("%d ",B[i][j]);
		}
		printf("\n");
		
	}
}

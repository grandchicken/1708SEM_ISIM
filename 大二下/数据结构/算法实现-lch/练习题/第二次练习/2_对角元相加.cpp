#include<stdio.h>
int A[3][3]={{1,2,3},{4,5,6},{7,8,9}};
int n = 3;
int main(){
	int i,j;
	int sum = 0;
	for(i = 0;i<=n-1;i++){
		for(j=0;j<=n-1;j++){
			if(j == i || j+i ==n-1){
				sum+=A[i][j];
			}
		} 
	}
	printf("%d",sum);
}

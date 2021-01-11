#include<stdio.h>

int A[3][3] = {{9,2,3},{2,0,5},{2,3,1}};
int m =3;
int n =3;
int main(){
	int min[m][3];
	int i,j;
	for(i=0;i<=m-1;i++){
		min[i][2] = A[i][0];
		min[i][0] = 0;
		min[i][1] = 0;
		for(j=0;j<=n-1;j++){
			if(A[i][j]<min[i][2]){
				min[i][2] = A[i][j];
				min[i][0] = i;
				min[i][1] = j;	
			}
		}
	}
	for(i=0;i<=m-1;i++){
		for(j=0;j<=2;j++){
			printf("%d ",min[i][j]);
		}
		printf("\n");
	}
} 

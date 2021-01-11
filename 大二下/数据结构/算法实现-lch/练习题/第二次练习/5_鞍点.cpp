#include<stdio.h>
int main(){
	int A[3][4] = {{2,1,3,4},{1,0,6,3},{2,-1,0,1}};
	int m =3;
	int n =4;
	int i,j,k;
	int min[m][3];
	
	for(i=0;i<=m-1;i++){
		min[i][0] = 0; 
		min[i][2] = A[i][0];
		min[i][1] = 0;
		
		for(j=0;j<=n-1;j++){
			if(A[i][j]<min[i][2]){
				min[i][1] = j; 
				min[i][2] = A[i][j];
				min[i][0] = i;
				
			}
			
		}
	}
	int flag[m];
	int mark = 0;
	for(k=0;k<=m-1;k++){
		flag[k] = 0;
		for(i=0;i<=m-1;i++){
			j = min[k][1];
			if(A[i][j]>min[k][2]){
				flag[k] = 1;
				
			}
		}
		if(flag[k] == 0){
			printf("%d %d %d ",min[k][0],min[k][1],min[k][2]);
			mark = 1;
		}
	}
	if(mark == 0){
		printf("%d",0);
	}
	
	
}

#include<stdio.h>
int main(){
	printf("请输入三元组的第一行，分别为矩阵总行数，总列数和非0元素个数：\n");
	int TA[100][3];	//原三元组 
	int TB[100][3];//转置后三元组 
	scanf("%d",&TA[0][0]);
	scanf("%d",&TA[0][1]);
	scanf("%d",&TA[0][2]);
	int i = 1;
	printf("请输入三元组第2到最后一行：\n"); 
	while(i<=TA[0][2]){
		scanf("%d",&TA[i][0]);
		scanf("%d",&TA[i][1]);
		scanf("%d",&TA[i][2]);
		i++;
	} 
	
	printf("矩阵形式为：\n");
	int j,k;
	int pointer = 1;
	for(j=0;j<TA[0][0];j++){
		for(k=0;k<TA[0][1];k++){
			if((j==TA[pointer][0]-1) && (k==TA[pointer][1]-1)){
				printf("%d ",TA[pointer][2]);
				pointer++;
			}else{
				printf("%d ",0);
			}
		}
		printf("\n");
	}

	TB[0][0] = TA[0][1];
	TB[0][1] = TA[0][0];
	TB[0][2] = TA[0][2];
	
	int m = 1;
	for(i=1;i<=TA[0][1];i++){
		for(j=1;j<=TA[0][2];j++){
			if(TA[j][1] == i ){
				TB[m][0] = TA[j][1];
				TB[m][1] = TA[j][0];
				TB[m][2] = TA[j][2]; 
				m++;
			}
		}
	
	}
	printf("转置后的三元组：\n");
	for(i=0;i<=TB[0][2];i++){
		for(j=0;j<=2;j++){
			printf("%d ",TB[i][j]);
		}
		printf("\n");
	}
	
	
	
	
	
	
	
	
	printf("转置后矩阵为：\n");
	pointer = 1;
	for(j=1;j<=TB[0][0];j++){
		for(k=1;k<=TB[0][1];k++){
			if((j==TB[pointer][0]) && (k==TB[pointer][1])){
				printf("%d ",TB[pointer][2]);
				pointer++;
			}else{
				printf("%d ",0);
			}
		}
		printf("\n");
	}

	
	
} 

#include<stdio.h>
int main(){
	printf("请输入三元组TA的第一行，分别为矩阵总行数，总列数和非0元素个数：\n");
	int TA[100][3];	
	int TB[100][3];
	scanf("%d",&TA[0][0]);
	scanf("%d",&TA[0][1]);
	scanf("%d",&TA[0][2]);
	int i = 1;
	printf("请输入三元组TA第2到最后一行：\n"); 
	while(i<=TA[0][2]){
		scanf("%d",&TA[i][0]);
		scanf("%d",&TA[i][1]);
		scanf("%d",&TA[i][2]);
		i++;
	}
	
	printf("请输入三元组TB的第一行，分别为矩阵总行数，总列数和非0元素个数(要求与TA行列数相同)：\n");
	scanf("%d",&TB[0][0]);
	scanf("%d",&TB[0][1]);
	scanf("%d",&TB[0][2]);
	i = 1;
	printf("请输入三元组TB第2到最后一行：\n"); 
	while(i<=TB[0][2]){
		scanf("%d",&TB[i][0]);
		scanf("%d",&TB[i][1]);
		scanf("%d",&TB[i][2]);
		i++;
	}
	
	int TC[100][3];
	TC[0][0] = TA[0][0];
	TC[0][1] = TA[0][1];
	int j = 1,k = 1;
	i = 1;
	while(j<=TA[0][2] && k<=TB[0][2]){
		if(TA[j][0] == TB[k][0]){
			if(TA[j][1] == TB[k][1]){
				if(TA[j][2]+TB[k][2]!=0){
					TC[i][0] = TA[j][0];
					TC[i][1] = TA[j][1];
					TC[i][2] = TA[j][2]+TB[k][2];
					i++;j++;k++; 
				}
				else{
					j++;k++;
				}
			}
			
			else if(TA[j][1] <= TB[k][1]){
				TC[i][0] = TA[j][0];
				TC[i][1] = TA[j][1];
				TC[i][2] = TA[j][2];
				j++;i++;
			}
			else if(TA[j][1] >= TB[k][1]){
				TC[i][0] = TB[k][0];
				TC[i][1] = TB[k][1];
				TC[i][2] = TB[k][2];
				k++;i++;
			}
		}
		else if(TA[j][0] >= TB[k][0]){
			TC[i][0] = TB[k][0];
			TC[i][1] = TB[k][1];
			TC[i][2] = TB[k][2];
			k++;i++;
		}
		else if(TA[j][0] <= TB[k][0]){
			TC[i][0] = TA[j][0];
			TC[i][1] = TA[j][1];
			TC[i][2] = TA[j][2];
			j++;i++;
		}
	}
	while(j<=TA[0][2]){
		TC[i][0] = TA[j][0];
		TC[i][1] = TA[j][1];
		TC[i][2] = TA[j][2];
		j++;i++;
	}
	while(k<=TB[0][2]){
		TC[i][0] = TB[k][0];
		TC[i][1] = TB[k][1];
		TC[i][2] = TB[k][2];
		k++;i++;
	}
	
	TC[0][2] = i-1;
	printf("输出的三元组为：\n");
	for(i=0;i<=TC[0][2];i++){
		for(j=0;j<=2;j++){
			printf("%d ",TC[i][j]);
		}
		printf("\n");
	}	
}

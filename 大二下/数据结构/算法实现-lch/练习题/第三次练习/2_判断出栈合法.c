#include<stdio.h>
int main(){
	char a[4];
	scanf("%s",&a);
	
	int i,j;
	char min;
	int flag = 0;
	for(i=0;i<=3;i++){
		min = a[i];
		for(j=i;j<=3;j++){
			
			if(a[j]<a[i]){
				if(a[j]<min){
					min = a[j];
				}else{
					flag = 1;
				}
			}
		}
	}

	if(flag == 1){
		printf("¸ÃÊäÈëË³Ðò´íÎó");
	}
	
	 
} 

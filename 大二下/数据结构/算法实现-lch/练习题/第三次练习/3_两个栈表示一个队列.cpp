#include<stdio.h>
int Stack_in[100];
int Stack_out[100];
int main(){
	int Top_in = -1;
	int Top_out = -1;
	int A[3] = {1,2,3};
	int i,j;
	//入队 
	for(i=0;i<=2;i++){
		Top_in++;
		Stack_in[Top_in] = A[i];
	}
	//出队
	if(Top_out > -1){
		while(Top_out>-1){
			printf("%d",Stack_out[Top_out]);
			Top_out--;
	}
	} else if(Top_out == -1){
		while(Top_in > -1){
			Top_out ++;
			Stack_out[Top_out] = Stack_in[Top_in];
			Top_in --;
		}
		while(Top_out>-1){
			printf("%d",Stack_out[Top_out]);
			Top_out--;
		}
	}
}

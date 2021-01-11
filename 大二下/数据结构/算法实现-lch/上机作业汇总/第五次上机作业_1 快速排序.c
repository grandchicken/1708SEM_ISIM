#include<stdio.h>
void Quick_sort(int A[],int low,int high);
int main(){
	int n;
	printf("请输入你要排序的元素个数:");
	scanf("%d",&n);
	printf("请输入要排序的序列:");
	int A[n];
	int i;
	for(i=0;i<n;i++){
		scanf("%d",&A[i]);
	}
	printf("快速排序结果为:");
	Quick_sort(A,0,n-1);
	for(i=0;i<n;i++){
		printf("%d ",A[i]);
	}
}
void Quick_sort(int A[],int low,int high){
	int i,j;
	int temp;
	if(low<high){
		i = low; j = high; temp = A[i];
		while(i<j){
			while(i<j && temp<=A[j]){
				j--;
			}
			if(i<j){
				A[i] = A[j];
				i++; 
			}
			while(i<j && temp>A[i]){
				i++;
			}
			if(i<j){
				A[j] = A[i];
				j--;
			}
		}
		A[i] = temp;
		Quick_sort(A,low,i-1);
		Quick_sort(A,i+1,high);	
	}
}

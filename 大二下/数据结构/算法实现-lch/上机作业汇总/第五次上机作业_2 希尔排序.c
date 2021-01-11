#include<stdio.h>
void Shell_arrange(int A[],int n);
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
	printf("希尔排序结果为:");
	Shell_arrange(A,n);
	for(i=0;i<n;i++){
		printf("%d ",A[i]);
	}
}
void Shell_arrange(int A[],int n){
	int i,j;
	int d,temp;
	d = n;
	while(d>1){
		d = d/2;
		for(i=d;i<n;i++){
			temp = A[i];
			j = i-d;
			while(j>=0 && temp>A[j]){
				A[j+d] = A[j];
				j = j - d;
			}
			A[j+d] = temp;
		}
	}
} 

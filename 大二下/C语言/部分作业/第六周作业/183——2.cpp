#include<stdio.h>
int main(){
	int count;
	float num,total;
	int n;
	printf("Please type in the total number of data values to be added:");
	scanf("%d",&n);
	printf("\n");
	if(n<0){
		printf("Error input!!");
		return 1;
	}
	count = 1;
	total = 0.0;
	
	while(count<=n){
		printf("Enter a number:");
		scanf("%f",&num);
		total += num;
		printf("The total is now %f\n",total);
		count++; 
	} 
	printf("\n\nThe final total of the %d numbers is %f\n",n,total);
	
	return 0;
}

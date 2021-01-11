#include<stdio.h>
int main(){
	float per,num,rate;
	printf("请输入单价:");
	scanf("%f",&per);
	printf("请输入数量:");
	scanf("%f",&num);
	printf("请输入折扣率:");
	scanf("%f",&rate);
	
	float sum,sum_after_discount,tax,payment;
	sum = per * num ;
	sum_after_discount = sum - sum*rate;
	tax = sum * 0.06;
	payment = sum + tax;
	printf("总价格%f\n",sum);
	printf("折扣后总价格%f\n",sum_after_discount);
	printf("应付税额%f\n",tax);
	printf("应付款额%f\n",payment);
}

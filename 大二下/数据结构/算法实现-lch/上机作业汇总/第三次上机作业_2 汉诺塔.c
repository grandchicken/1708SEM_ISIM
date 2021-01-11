#include<stdio.h>
void move(int n,char X,char Y);
void Hanoi(int n,char X,char Y,char Z);
int main(){
	int n ;
	char X ='X',Y='Y',Z='Z';
	printf("请输入盘子的个数:"); 
	scanf("%d",&n);
	Hanoi(n,X,Y,Z);
} 
void move(int n ,char X,char Y){
	printf("将%d号盘从%c移到%c上\n",n,X,Y);
}
void Hanoi(int n,char X,char Y,char Z){
	if(n==1){
		move(1,X,Z);
	}else{
		Hanoi(n-1,X,Z,Y);
		move(n,X,Z);
		Hanoi(n-1,Y,X,Z);
	}
}

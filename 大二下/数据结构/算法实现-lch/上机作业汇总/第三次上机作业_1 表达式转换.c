#include<stdio.h>
#include<stdlib.h>
int isp(char x);
int icp(char x);
int main(){
	char a[200];
	char s;
	int l = 0;
	char Stack[100];
	printf("请输入中缀表达式，以#号结尾:\n");
	while(1){
		scanf("%c",&s);
		a[l] = s;
		if(a[l] == '#'){
		break;
	}
		l++; 
	}
	
	int i = 0;
	int top = 0;
	printf("输出为：");
	while(a[i] != '#'){
		switch(a[i]){
			case '(':{
				top++;
				Stack[top] = a[i];
				break;
			}
			case ')':{
				while(top>=0 && Stack[top]!='('){
					printf("%c",Stack[top]);
					top--;
				}
				top--;
				break; 
			}
				
				
			case '+':{
				while(top>=0 && isp(Stack[top])>=icp(a[i])){
					printf("%c",Stack[top]);
					top--;
				}
				top++;
				Stack[top] = a[i];
				break;
			}
			case '-':{
				while(top>=0 && isp(Stack[top])>=icp(a[i])){
					printf("%c",Stack[top]);
					top--;
				}
				top++;
				Stack[top] = a[i];
				break;
			}

			case '*':{
				while(top>=0 && isp(Stack[top])>=icp(a[i])){
					printf("%c",Stack[top]);
					top--;
				}
				top++;
				Stack[top] = a[i];
				break;
			}
			case '/':{
				while(top>=0 && isp(Stack[top])>=icp(a[i])){
					printf("%c",Stack[top]);
					top--;
				}
				top++;
				Stack[top] = a[i];
				break;
			}
			case '%':{
				while(top>=0 && isp(Stack[top])>=icp(a[i])){
					printf("%c",Stack[top]);
					top--;
				}
				top++;
				Stack[top] = a[i];
				break;
			}
			case '^':{
				while(top>=0 && isp(Stack[top])>=icp(a[i])){
					printf("%c",Stack[top]);
					top--;
				}
				top++;
				Stack[top] = a[i];
				break;
			}
			default:printf("%c",a[i]);
		}
		i++;
	}
	while(top>=0){
		printf("%c",Stack[top]);
		top--;
	}
}
//栈内优先级 
int isp(char x){
	switch(x){
		case'+':return 1;
		case '-':return 1;
		case'*':return 2;
		case'/':return 2;
		case'%':return 2;
		case'^':return 3;
		case'(':return 0;
		default:return 0;
	} 
}

//栈外优先级 
int icp(char x){
	switch(x){
		case'+':return 1;
		case'-':return 1;
		case'*':return 2;
		case'/':return 2;
		case'%':return 2;
		case'^':return 4;
		case'(':return 5;
		default:return 0;
	}
} 

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void Print(int n);
int main(){
	srand(time(NULL));
	int n;
	int i;
	int memory[6];
	for(i=0;i<6;i++){
		memory[i] = 0;
		}
	int total = 0;
	printf("ºï×ÓÇÃ»÷¼üÅÌÖÐ:");
	while(true){
		n = rand()%26+1;
		Print(n);
		total+=1;
		if((n==20&&memory[0]==1)||(n==19&&memory[2]==1)||(n==5&&memory[5]==1 )|| (n==5&&memory[1]==1 )|| (n==14&&memory[3]==1)|| (n==16&&memory[4]==1)){
			break;
		}
		if(n==1){
			memory[0] = 1;
		}else if(n==8){
			memory[1] = 1;
		}else if(n==9){
			memory[2] = 1;
		}else if(n==15){
			memory[3] = 1;
		}else if(n==21){
			memory[4] = 1;
		}else if(n==23){
			memory[5] = 1; 
		}else{
			for(i=0;i<6;i++){
				memory[i] = 0;
			}
		}
		
		
	}	
	printf("\n¹²ÇÃ»÷ÁË%d¸ö×ÖÄ¸",total);

	
}

void Print(int n){
	printf("%c",'a'+n-1);
}

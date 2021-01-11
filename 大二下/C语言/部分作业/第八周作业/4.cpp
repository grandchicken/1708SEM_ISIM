//4
#include<stdio.h>
int main(){
	int x,y,z;
	for(x=1;x<=9;x++){
		for(y=1;y<=9;y++){
			for(z=1;z<=9;z++){
				if(x*100+y*10+z+y*100+z*10+z == 532){
					printf("x=%d y=%d z=%d",x,y,z);
				}
			}
		}
	}
}

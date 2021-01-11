//3
#include<stdio.h>
#define apple_p 4
#define pear_p 0.4
#define melon_p 0.2
int main(){
	int apple,pear,melon;
	for(apple=1;apple<=100;apple++){
		for(pear=1;pear<=100-apple;pear++){
			for(melon=1;melon<=100-apple-pear;melon++){
				if(apple*apple_p+pear*pear_p+melon*melon_p<=40 && apple+pear+melon==100){
					printf("apple:%dkg pear:%dkg melon:%dkg\n",apple,pear,melon);
				}
			}
		}
	}
}

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>
#define pi 3.1415926
#define loops 50000
double GaoS(double miu,double theta);
int main(){
	double A[loops];
	int i = 0;
	int sum[3];
	int j;
	for(j=0;j<3;j++){
		sum[j] = 0;
	}
	srand(time(NULL));
	while(i<loops){
		A[i] = GaoS(0,1);
		//printf("%f ",A[i]);
		if(A[i]!=-9999){
			if(A[i]>=-1 && A[i]<=1) {
				sum[0]++;	
			}
			if(A[i]>=-2 && A[i]<=2) {
				sum[1]++;	
			}
			if(A[i]>=-3 && A[i]<=3) {
				sum[2]++;	
			}
			i++;
		}
		
	}
	printf("生成%d个服从高斯分布N(0,1)随机数:",loops);
	for(i=0;i<loops;i++){
		printf("%f ",A[i]);
	}
	printf("\n以下为对该分布的检验:\n");
	double rate[3];
	for(j=0;j<3;j++){
		rate[j] = 1.0*sum[j]/loops;
		printf("%d倍σ%f\n",j+1,rate[j]);
	}
	
	
} 
double GaoS(double miu,double theta){
	
	double p0,p;
	double m;
	m = (double)(rand())/RAND_MAX*100-50;
	p0 = 1.0/sqrt(2.0*pi*theta*theta)*exp(-(m-miu)*(m-miu)/(2.0*theta*theta));
	p = (double)(rand())/RAND_MAX*1.0/sqrt(2.0*pi*theta*theta); 
	if(p0>p){
		return m;
	}else{
		return -9999;
	}
}

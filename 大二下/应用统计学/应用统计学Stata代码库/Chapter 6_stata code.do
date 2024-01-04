***********************************************************************
****************第六章  参数估计 Stata code****************************
***********************************************************************



************************************************************************
********************计算置信区间 Confidence interval********************
************************************************************************
help ci

************************************************************************
//计算正态总体 N(15, 4)中抽样获得的不同样本容量的样本, 均值的置信区间

//generate 10 random numbers from N(15, 2^2)
clear
set obs 10
gen x=rnormal(15,2)
ci means x, level(90)
ci means x, level(50)

// generate 100 random numbers from N(15, 2^2)
clear
set obs 100
gen x=rnormal(15,2)
ci means x, level(90)
ci means x, level(50)

// generating 10000 random numbers from N(15, 2^2)
clear
set obs 10000
gen x=rnormal(15,2)
ci means x, level(90)
ci means x, level(50)

// 对比不同样本容量, 不同置信水平下的置信区间, 你可以得到什么结论?




************************************************************************

// 如何计算方差的置信区间？ How to calculate the conficence intervals of \sigma^2 of  N(15, 2^2)?

help ci
ci variances x
ci variances x, level(90)


************************************************************************
// 从一个正态分布N(15，4)中抽样形成100个样本，每个样本观察数是10，计算每个样本均值的置信区间，最后把所有置信区间划到一张图上。
clear

cap prog drop myprog
prog def myprog, rclass
 clear
 set obs 10
 gen x = rnormal(15, 2)
 ci mean x, level(90) 
 ret scalar mean = r(mean)
 ret scalar ub = r(ub)
 ret scalar lb = r(lb)
end 

simulate mean = 15 ub = r(ub) lb = r(lb), reps(100): myprog

gen x = _n 
tw rspike ub lb x, yline(`=mean[1]') 











****************************非正态总体区间估计*****************************
//如果对1000名随机抽样的居民调查对一项政策的支持程度, 平均得到80%的支持度, 政策支持的点估计是多少? 样本标准差是多少? 95%置信区间是多少?


// 解法一 (利用两点分布性质)}： 点估计: 0.8
//  样本标准差求法1:
di sqrt((0.8*0.2)) //得出   0.4


//95%置信区间求法1:
di 0.8-1.96*sqrt((0.8*0.2)/1000)  // 得出   .775

di 0.8+1.96*sqrt((0.8*0.2)/1000) //得出    .824

//所以 [.775, .825]



// 解法二 (利用大样本渐近分布)

clear 
set obs 1000
gen var1=1
replace var1=0 if _n<=200
sum, de // 得出 标准差0.4

//95\%置信区间求法2：

di 0.8-1.96*0.4/sqrt(1000) // 得出  .775

di 0.8+1.96*0.4/sqrt((0.8*0.2)/1000) //得出 .825

//所以 [.775, .825]
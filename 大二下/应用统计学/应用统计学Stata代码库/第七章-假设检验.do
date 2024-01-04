***********************************************************
********************第七章-假设检验************************
***********************************************************




**********************势函数*************************
// power function g(\theta)

twoway function g=normal((1.5- x)/0.8), range(0 5)

				



************************ 正态总体的均值检验**************************

// sigma 已知
help ztest
sysuse auto
sum mpg
ztest mpg==20, sd(6)

// sigma 未知

help ttest
ttest mpg==20

ttest mpg==20 if foreign==1
ttest mpg==20 if foreign==0

// 双总体情况
clear 
webuse fuel
ttest mpg1==mpg2
ttest mpg1==mpg2, unpaired

//总体方差检验

help sdtest


***************** Stata数值计算示例： 分位数计算, p值计算 (对应教材例7.2.2）****************

//Stata 计算自由度为4的t分布的0.975分位数     t_{0.975}(4)= 2.776

help invt

invt(df,p)
/*
Description:  the inverse cumulative 
Student's t distribution: if t(df,t) = p, 
then invt(df,p) = t
   Domain df:    2e-10 to 2e+17 (may be nonintegral)
    Domain p:     0 to 1
    Range:        -8e+307 to 8e+307
*/


di invt(4, 0.975)
 

// 2.7764451


// 用STATA计算p值： P(t >= 2.795):

help t

//t(df,t)
//Description: the cumulative Student's 
//t distribution with df degrees of freedom
//Range: 0 to 1

 di 2*(1-t(4, 2.795))
// .04906106





********************皮尔逊(Pearson) Chi^2拟合优度检验********************

ssc install tab_chi

help chitest

chitesti 315 108 101 32 \ 556*9/16 556*3/16 556*3/16 556*1/16

********************列联表 contingency table     卡方独立性检验**********

help tabulate twoway
//  卡方独立性检验例1： 教材7.4.4 色盲
clear
set obs 1000

gen male=1 if _n<=(535+65)

replace male=0 if  _n>(535+65)

gen colorblind=0 if male=1 & _n<=535

replace colorblind=1 if male=1 & _n>535

replace colorblind=0 if male=0 & _n<=(535+65+382)

replace colorblind=1 if male=0 & _n>(535+65+382)

tabulate male colorblind, chi



//  卡方独立性检验例2
clear
sysuse auto
keep if _n<10
tabulate make foreign, chi
tabulate length weight, chi

********************QQ plot******************************************
clear
sysuse nlsw88.dta
help pnorm

help qnorm

hist wage

pnorm wage

gen lnwage=ln(wage)

hist lnwage

pnorm lnwage
qnorm lnwage

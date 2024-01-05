*************************************************************************
****************Chapter B1-相关系数**************************************
*************************************************************************

*************Pearson 相关系数(Pearson's correlation coefficient)与相关性假设检验*****

/*
1. 仅看相关系数
corr x y

2. 既想知道相关系数, 又想知道显著水平(significance level)p-value
pwcorr x y, sig

*/



// Setup
sysuse auto

// original data 

list price weight mpg headroom in 1/10


// Estimate all pairwise correlations
pwcorr price weight mpg headroom

//  Add significance level to each entry
pwcorr price weight mpg headroom, sig

//  Add stars to correlations significant at the 1% level
 pwcorr price weight mpg headroom, star(.01) sig 

 
 
 
 
 
*************Spearman秩相关系数及其假设检验*************
sysuse auto
// Two variables; output displayed in tabular form by default
spearman price  weight
// Two variables; output displayed in matrix form
spearman price  weight mpg headroom, matrix
// Use all nonmissing observations between a pair of variables
 spearman price  weight mpg headroom, pw
// Star all correlation coefficients significant at the 5% level or lower
spearman price  weight mpg headroom, pw star(.05)



 *************Kendall tau 相关系数及三种相关系数的Stata 实现*************
 

clear 
set obs 100
gen x=_n
gen x2=x*x


corr x x2

spearman x x2

ktau x x2

//ktau will produce ktau_a and ktau_b which are both right, 
// formula given in accompanied pdf file.
 
 


*************************************************************************
****************Chapter B1-Simple linear regression**********************
*************************************************************************







**********************例1: 股价-股息*******************************
clear

 
use "股价-股息.dta"

reg y x

predict e, residuals

scatter e x

predict standardized_e, rstandard

scatter standardized_e x



**********************例2: 收入-工作年限*******************************

clear 

sysuse nlsw88

reg wage grade

predict e, residuals

scatter e grade

predict standardized_e, rstandard

scatter standardized_e grade





clear 

sysuse nlsw88

gen lnwage=ln(wage)

reg lnwage grade

predict e, residuals

scatter e grade

predict standardized_e, rstandard

scatter standardized_e grade


*************Stata 中画$y$的预测值与预测区间************

help graph twoway lfitci

sysuse auto, clear

reg mpg weight

//预测区间
twoway lfitci mpg weight, stdf || scatter mpg weight




*****************************************************************************
****************第五章  统计量及其分布 Stata code****************************
*****************************************************************************





********************简单随机样本抽取********************
clear
sysuse auto,replace
//sample:  sampling without replacement
//bsample: sampling with replacement (bootstrap)

sample 20, count  //draw a sample of 20 observations from
                  //the current data set
				  
clear
sysuse auto,replace
//sample:  sampling without replacement
//bsample: sampling with replacement (bootstrap)			  
sample 20         //draw a sample of 20%  observations




********************用Stata给出有序样本, 做经验分布函数图********************
clear
ssc install cdfplot, replace
help cdfplot
sysuse auto,replace
keep length foreign
//produce ordered sample
sort length
    
// produce empirical distribution plot
sum length
    cdfplot length
    cdfplot length, normal
    cdfplot length, by(foreign)
    cdfplot length, by(foreign) norm saving(mygraph,replace)


********************画直方图********************
clear 
help hist
webuse systolic 
hist systolic
hist systolic, width(10) start(-10) //default: 密度(即 频率/组距, density)
hist systolic, width(10) start(-10) fraction //频率(fraction)
hist systolic, width(10) start(-10) frequency //频率(fraction)

********************画茎叶图********************
clear 
webuse systolic 
stem systolic , lines(1)
stem systolic if drug==1, lines(1)
stem systolic if drug==2, lines(1)



****************用STATA计算样本均值和样本方差*********************

clear
sysuse auto.dta
sum price

****************用STATA计算样本分位数与样本中位数、峰度偏度*********************

sum price, de

****************用stata做箱线图*********************
clear 
webuse systolic 
graph box systolic

****************用STATA计算$\chi^{2}(n)$的分位数$\chi_{1-\alpha}^{2}(n)$*********************

help function
help invchi2// the inverse of cumulative chi-square distribution
// chi2(): if chi2(df,x) = p,  then invchi2(df,p) = x

//calculating the 0.005 percentile of chi(5)
di invchi2(5,0.005)



****************用STATA计算$ F_{1-\alpha}(m,n)$分位数*********************

help function
help invF// the inverse cumulative F distribution:
//  if F(df1,df2,f) = p, then invF(df1,df2,p) = f
// 计算自由度为(10, 5)的F分布的0.95分位数
di invF(10, 5, 0.95)

****************用STATA计算$t_{1-\alpha}(n)$ 分位数：*********************


help function
help invt // the inverse cumulative Student's t distribution:
// if t(df,t) = p, then invt(df,p) = t
// 计算自由度为11的t分布的0.95分位数
di invt(11, 0.95)




**************样本均值分布问题****************
****************验证总体分为均匀分布的样本均值的抽样分布*********************

//可以用样本均值经验分布逼近样本均值分布去验证


clear 
foreach samp in 10 100 1000 {
clear
set obs `samp'
set seed 12345678
ge mean = .

forvalues i = 1/`samp'{
 gen u = runiform()  //生成（0,1）之间均匀分布的伪随机数, 均值为0.5，方差为1/12
 egen temp = mean(u)
 replace mean = temp if _n == `i'
 drop u temp
}

sum mean
twoway function y = normalden(x, `r(mean)', `r(sd)'), range(0.4 0.6) || kdensity mean, ///
 legend(label(1 "Normal Densities") label(2 "Sample Densities")) ///
 note("Sample Size: `samp'") 
 graph export "normal_sample`samp'.pdf",replace
 
}



*********************************绘制概率密度分布图***********************


/* Plot several normal distributions */
help normalden
#delimit ;
graph twoway (function y=normalden(x,1,1), range(-10 20) lw(medthick))
             (function y=normalden(x,1,2), range(-10 20) lw(medthick))
			 (function y=normalden(x,5,1), range(-10 20) lw(medthick)),
  title("Normal distribution comparison")
  xtitle("Normal", size(medlarge)) ytitle("p.d.f. p(x)")
  xlabel(-10(2)20)
  xscale(lw(medthick)) yscale(lw(medthick))
  legend(label(1 "{&mu}=1 {&sigma}=1") label(2 "{&mu}=1 {&sigma}=2") 
		label(3 "{&mu}=5 {&sigma}=1"))
  graphregion(fcolor(white));
 #delimit cr
 graph export normal2.png, as(png) replace

/* Stata code ends */


/* Plot several t distributions and compare with standard normal distribution*/
help normalden
help tden

#delimit ;
graph twoway (function y=tden(5,x), range(-10 10) lw(medthick))
             (function y=tden(20,x), range(-10 10) lw(medthick))
			 (function y=normalden(x,0,1), range(-10 10) lw(medthick)),
  title("Normal distribution comparison")
  xtitle("Normal", size(medlarge)) ytitle("p.d.f. p(x)")
  xlabel(-10(2)10)
  xscale(lw(medthick)) yscale(lw(medthick))
  legend(label(1 "student t distribution, degree of freedom=5") label(2 "student t distribution, degree of freedom=20") 
		label(3 "{&mu}=0 {&sigma}=1"))
  graphregion(fcolor(white));
 #delimit cr
 graph export t_distribution.png, as(png) replace

/* Stata code ends */



//plot of chi square pdf

help chi2den
help fden
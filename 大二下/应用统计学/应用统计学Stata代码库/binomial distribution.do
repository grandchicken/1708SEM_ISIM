// Binomial pdf

// b(10,0.2) b(10,0.5) b(10,0.8)

//Zhuang Hao 9/1/2019
clear
set obs 11
help binomialp
gen b1_pdf=binomialp(10,_n-1,.2) //for each ob from 1 to 11 (indicated by _n), gen pdf.
gen b2_pdf=binomialp(10,_n-1,.5)
gen b3_pdf=binomialp(10,_n-1,.8)
gen x=_n-1



twoway dropline b1_pdf x, xlabel(#15) ytitle(P(X)) title( b(10,0.2) 右偏（高峰偏左）)
twoway dropline b2_pdf x, xlabel(#15) ytitle(P(X)) title( b(10,0.5) 对称)
twoway dropline b3_pdf x, xlabel(#15) ytitle(P(X)) title( b(10,0.8) 左偏（高峰偏右）)

twoway (dropline b1_pdf x) (dropline b2_pdf x) (dropline b3_pdf x) 

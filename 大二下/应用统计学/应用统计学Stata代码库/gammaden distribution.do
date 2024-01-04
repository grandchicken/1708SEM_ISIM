

/* Plot several normal distributions */
#delimit ;
graph twoway (function y= gammaden(0.5,0.5,0,x), range(0 3) lw(medthick))
             (function y= gammaden(1,0.5,0,x), range(0 3) lw(medthick))
			 (function y= gammaden(2,0.5,0,x), range(0 3) lw(medthick)),
  title("Gamma distribution")
  xtitle("Gamma distribution", size(medlarge)) ytitle("p.d.f. p(x)")
  xlabel(0(0.5)3)
  xscale(lw(medthick)) yscale(lw(medthick))
  legend(label(1 "{&alpha}=0.5,{&lambda}=0.5") label(2 "{&alpha}=1,{&lambda}=0.5") label(3 "{&alpha}=2,{&lambda}=0.5"))
  graphregion(fcolor(white));
 #delimit cr
 graph export "D:\teaching\Probability Theory_Fall 2019\slides\chapter 2\gamma.png", as(png) replace

/* Stata code ends */


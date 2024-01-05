

/* Plot several normal distributions */
#delimit ;
graph twoway (function y= exponentialden(0.5, x), range(0 10) lw(medthick))
             (function y= exponentialden(1,x), range(0 10) lw(medthick))
			 (function y= exponentialden(2,x), range(0 10) lw(medthick)),
  title("exponential distribution")
  xtitle("exponential distribution", size(medlarge)) ytitle("p.d.f. p(x)")
  xlabel(0(1)10)
  xscale(lw(medthick)) yscale(lw(medthick))
  legend(label(1 "{&lambda}=2") label(2 "{&lambda}=1") label(3 "{&lambda}=0.5"))
  graphregion(fcolor(white));
 #delimit cr
 graph export  exponential.png , as(png) replace

/* Stata code ends */


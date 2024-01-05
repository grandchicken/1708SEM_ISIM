
********************************************************************
******************Stata Anova****************************
*******************************************************************


*******************方差分析ANOVA*******************
help anova

use https://www.stata-press.com/data/r16/apple

tabulate treatment, summarize(weight)

anova weight treatment

*******************参数估计****************
margins treatment

regress, baselevels

regress weight b2.treatment

regress weight i.treatment

*******************多重比较 multiple comparison****************

help oneway
use https://www.stata-press.com/data/r16/apple
anova weight treatment
oneway weight treatment, noanova scheffe








********************************************************************
******************Stata 描述性统计图简介-Zhuan Hao*******************
********************************************************************


*******************条形图 Bar chart*******************

use https://www.stata-press.com/data/r16/nlsw88, clear

graph bar (mean) wage, over(collgrad) ///
	title("平均小时工资, 1988, 女性 34-46岁") ///
	subtitle("大学毕业与否")

graph bar (mean) wage, over(smsa) over(married) over(collgrad) ///
	title("Average Hourly Wage, 1988, Women Aged 34-46") ///
	subtitle("by College Graduation, Marital Status, and SMSA residence") ///
	note("Source: 1988 data from NLS, U.S. Dept. of Labor, Bureau of Labor Statistics")

*******************饼图 Pie chart*******************

//输入数据 某公司2002年各部门支出
clear
set obs 1
gen sales =12
gen marketing=14
gen research=2
gen development=8


label var sales "Sales"
label var market "Marketing"
label var research "Research"
label var develop  "Development"

graph pie sales marketing research development, ///
	plabel(_all name, size(*1.5) color(white)) ///
	legend(off)                                ///
	plotregion(lstyle(none))                   ///  
	title("Expenditures, XYZ Corp.")             ///
	subtitle("2002")                            ///
	note("Source:  2002 Financial Report (fictional data)")

	
	
********************画直方图********************
clear 
help hist
webuse systolic 
hist systolic
hist systolic, width(10) start(-10) //default: density
hist systolic, width(10) start(-10) fraction
hist systolic, width(10) start(-10) frequency



********************画茎叶图********************
clear 
webuse systolic 
stem systolic , lines(1)
stem systolic if drug==1, lines(1)
stem systolic if drug==2, lines(1)



****************用stata做箱线图*********************
clear 
webuse systolic 
graph box systolic


****************用stata做线图*********************

//美国人期望寿命(U.S. life expectancy, 1900-1940)
use https://www.stata-press.com/data/r16/uslifeexp2

list in 1/8

twoway line le year

twoway connected le year, ytitle("美国人期望寿命") xtitle("年份")



****************用stata做雷达图*********************

ssc install radar

help radar

sysuse auto

radar make  mpg if foreign, aspect(1) scale(0.7)

radar make weight if foreign, aspect(1)



****************用stata做散点图*********************

//美国人期望寿命(U.S. life expectancy, 1900-1940)
use https://www.stata-press.com/data/r16/uslifeexp2

list in 1/8

twoway line le year

twoway scatter le year, ytitle("美国人期望寿命") xtitle("年份")


****************用stata做热力图*********************

ssc install heatplot
ssc install palettes, replace
ssc install colrspace, replace

help heatplot


  //  Bivariate histogram of weight and height:

 webuse nhanes2, clear
heatplot weight height, ylabel(25(25)175)

//    Trivariate distributions 
// The following graph displays the gender distribution (proportion female) by weight and height:

heatplot female weight height, hexagon ylabel(25(25)175) cuts(0(.05)1)

****************用stata做气泡图*********************
clear
sysuse census
scatter death medage [w=pop65p], msymbol(circle_hollow)


 
/*************************************用stata做地图 map data******************************************/
//prepare command: maptile    (https://michaelstepner.com/maptile/)
ssc install maptile
ssc install spmap
help maptile 
maptile_install using "http://files.michaelstepner.com/geo_county1990.zip"
maptile_geolist
maptile_geohelp county1990

























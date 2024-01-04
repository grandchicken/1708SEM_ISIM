*****************************************************************************
****************应用统计II 第4讲- 聚类分析 Stata code************************
*****************************************************************************


*****************************************************************************
********************K-Means 案例: 身体指标分类与针对性锻炼方案***************
*****************************************************************************

help cluster kmeans

// 体育课上对80个学生身体指标的测量, 包括柔韧度, 速度, 力量 flexibility、speed和strength 三个指标. 利用这三个指标, 对学生进行分组, 用于制定针对性的体育锻炼方案. You have measured the flexibility, speed, and strength of the 80 students in your physical education class. You want to split the class into four groups, based on their physical attributes, so that they can receive the mix of flexibility, strength, and speed training that will best help them improve.

use http://www.stata-press.com/data/r13/physed.dta, clear

*or

use 身体指标.dta, clear

********************描述数据********************
sum 
graph matrix flex speed strength
graph twoway scatter flex speed 


// As you expected, based on what you saw the first day of class, the data indicate a wide range of levels of performance for the students. The graph seems to indicate that there are some distinct groups, which leads you to believe that your plan will work well. You decide to perform a cluster analysis to create four groups, one for each of your class assistants. You have had good experience with kmeans clustering in the past and generally like the behavior of the absolute-value distance.

********************K-means clustering********************
//You do not really care what starting values are used in the cluster analysis, but you do want to be able to reproduce the same results if you ever decide to rerun your analysis. You decide to use the krandom() option to pick k of the observations at random as the initial group centers. You supply a random-number seed for reproducibility. You also add the keepcenters option so that the means of the four groups will be added to the bottom of your dataset.

cluster k flex speed strength, k(4) name(g4abs) s(kr(385617)) mea(abs) keepcen
cluster list g4abs

tab g4abs

// drop those with missing infomation
list flex speed strength in 81/L, abbrev(12)
drop in 81/L

//各组指标有什么特点? check stats by group. What do can you learn from these statistics? 

tabstat flex speed strength, by(g4abs) stat(min mean max)

//Group 1, with 15 students, is already doing well in flexibility and speed but will need extra strength training. Group 2, with 20 students, needs to emphasize speed training but could use some improvement in the other categories as well. Group 3, the smallest, with 10 students, needs help with flexibility and strength. Group 4, the largest, with 35 students, has serious problems with both flexibility and speed, though they did well in the strength category.

//数据可视化 visulization
//Because you like looking at graphs, you decide to view the matrix graph again but with group numbers used as plotting symbols.
graph matrix flex speed strength, m(i) mlabel(g4abs) mlabpos(0)

//how about divide them into 2 groups
cluster k flex speed strength, k(2) name(g2abs) s(kr(385617)) mea(abs) keepcen
graph matrix flex speed strength, m(i) mlabel(g2abs) mlabpos(0)

//how about divide them into 3 groups
cluster k flex speed strength, k(3) name(g3abs) s(kr(385617)) mea(abs) keepcen
graph matrix flex speed strength, m(i) mlabel(g3abs) mlabpos(0)




*****************************************************************************
********************系统聚类/分层聚类法案例： 推销员问题*********************
*****************************************************************************

use 推销员问题.dta, clear
//所有聚类方法
help cluster 
// 系统聚类方法
help cluster linkage

// 测度聚合指数：linkage  测度样本点距离: measure
// 最短距离测度聚合指数， 绝对值距离测度样本点距离
cluster s 销售量 回收款项, measure(L1) // or measure(absolute)
cluster tree


// 最短距离测度聚合指数， 欧式距离测度样本点距离
cluster s 销售量 回收款项 //default is Euclidean or L(2). You can also write cluster s 销售量 回收款项, measure(Euclidean), which gives the same results
cluster s 销售量 回收款项, measure(Euclidean)
cluster tree


*****************************************************************************
********************系统聚类案例2: 定性变量或哑变量聚类分析***************
*****************************************************************************


help cluster linkage

use https://www.stata-press.com/data/r16/homework, clear

cluster s a1-a60, measure(matching)
cluster tree

cluster generate grp3 = group(3)
table grp3 truegrp

cluster generate grp2 = group(2)
table grp2 truegrp


cluster s a1-a60, measure(Euclidean)
cluster tree

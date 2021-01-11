-- 6.3 数据分页
--公用表达式 CTE
with CTE_Test as  (select *  from stock_YJY where 交易日期 = '2020-01-01')
select * from CTE_Test where 代码 like '001%'     /* CTE 有效 */
select * from CTE_Test where 代码 like '001%'     /* CTE 失效 */

-- row_number+公用表达式：即席分页
declare @PageSize int, @Page_Num int
select @PageSize=10, @Page_Num=4;
with SN_T as  (select ROW_NUMBER() over(order by 最新价) row_num, *
                 from stock_YJY)
select * from SN_T where row_num between @PageSize * (@Page_Num-1) + 1 and  @PageSize * @Page_Num
GO

-- row_number+临时表：多页访问
select ROW_NUMBER() over(order by 最新价) row_num, *
  into #SN_T2 from stock_YJY
create unique clustered index idx_rn on #SN_T2(row_num)
declare @PageSize int, @Page_Num int;
select @PageSize=10, @Page_Num=8;
select * from #SN_T2 
 where row_num between @PageSize * (@Page_Num-1) + 1 and  @PageSize * @Page_Num
  order by row_num                    
go     

--6.4 数据统计与聚合
-- 1、中值计算
-- 观察奇数个元组的50% (count(*)+1)/2
select count(*) from stock_YJY where 交易流水 > 1
select top(50) percent * from stock_YJY where 交易流水 > 1 

-- 中值计算, 使用了子查询嵌套与赋值
declare @ZZ1 int, @ZZ2 int
set @ZZ1 = (select min(t1.成交量) from (select top(50) percent * from stock_YJY order by 成交量 desc, 交易流水 asc) t1)
Set @ZZ2 = (select max(t2.成交量) from (select top(50) percent * from stock_YJY order by 成交量 asc, 交易流水 desc) t2)
select (@ZZ1+@ZZ2)/2  
go

-- 2、集基函数与窗口函数
-- 交易明细与汇总统计
select 交易流水, 代码, 交易日期, 
       最新价, avg(最新价) OVER(PARTITION BY 代码) AS 均价,
	   成交量, sum(成交量) OVER(PARTITION BY 代码) AS 累计成交
from stock_YJY
order by 代码, 交易日期

-- 价格差异统计
select 交易流水, 代码, 交易日期, 最新价, 
       avg(最新价) OVER(PARTITION BY 代码) AS 均价, 
	   最新价 - avg(最新价) OVER(PARTITION BY 代码) AS diff,
	   100 * 最新价 / avg(最新价) OVER(PARTITION BY 代码) AS pct
from stock_YJY
order by 代码, 交易日期
   
-- 3、数据聚合统计
-- 累计聚合：窗口框架
select 交易流水, 代码, 交易日期, 成交量,
       sum(成交量) over(partition by 代码 order by 交易日期
	                    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) 累计至今
  from stock_YJY order by 代码,交易日期 
   
-- 滑动聚合：7天成交量滑动均值
select 交易流水, 代码, 交易日期, 成交量,
       avg(成交量) over(partition by 代码 order by 交易日期
	                    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as '7天滑动均值'
  from stock_YJY order by 代码,交易日期 
go
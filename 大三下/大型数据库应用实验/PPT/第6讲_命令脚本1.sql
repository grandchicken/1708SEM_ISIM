-- 6.1 数据排名
-- 1、全局排序
select row_number() over(order by 最新价) as row_num, 交易日期, 代码,最新价 from stock_YJY

-- 2、分区排序   
select row_number() over(partition by 交易日期 order by 最新价) as row_num, 交易日期, 代码,最新价 from stock_YJY 	  
 
-- 3、数据排名
select row_number() over(order by 最低价近似) as row_num,
       rank() over(order by 最低价近似) as rank_num,  
       dense_rank() over(order by 最低价近似) as dense_rank_num,
       交易日期, 代码, 最低价近似 from stock_YJY where 代码 like '60%' and 交易日期 = '2020-01-01'
   
-- 4、分区数据排名
select row_number() over(partition by 交易日期 order by 最低价近似) as row_num,
       rank() over(partition by 交易日期 order by 最低价近似) as rank_num,  
       dense_rank() over(partition by 交易日期 order by 最低价近似) as dense_rank_num,
       交易日期, 代码, 最低价近似 
  from stock_YJY
 where 代码 like '6001%' and 交易日期 between '2020-01-01' and  '2020-01-05' and 最低价近似 between 10 and 20
 go
 
-- 6.2 top 查询
-- 1、选择top 数据
declare @ii int
set @ii = 1
select top (@ii+3) *  from stock_YJY order by 成交量 desc
select top ((@ii-0.4)*0.001) percent  *  from stock_YJY order by 成交量 desc 
select top 0.001 percent  *  from stock_YJY order by 成交量 desc 

-- top 确定性问题
select top 3 *  from stock_YJY order by 最低价近似
select top 3 *  from stock_YJY order by 最低价近似, 交易流水
select top 3 with ties  *  from stock_YJY order by 最低价近似

-- 2、top 与修改
select * into stock_YJY2 from stock_YJY 
go
set nocount on    --阻止返回“受T-SQL语句影响的行数”信息
declare @cnt int
while 1=1
begin
   select @cnt = count (*) from  stock_YJY2
   if @cnt = 0 
      break
   print '剩余' + cast(@cnt as varchar(10)) + '条记录'
   delete top(10000) from stock_YJY2 
end
select COUNT(*) from stock_YJY2
set nocount off
go
drop table stock_YJY2
go

-- 3、分区提取top数据
-- 方案1：top + 子查询
-- Top 1：每天均价最高的一条股票
select * from stock_YJY t1 where 交易流水 =
        (select top 1 交易流水 from stock_YJY t2 
                      where t2.交易日期 = t1.交易日期 order by 成交量 desc, 代码)
 order by 交易日期

-- Top N：每天均价最高的N条股票
select * from stock_YJY t1 where 交易流水 in
        (select top 3 交易流水 from stock_YJY t2 
                      where t2.交易日期 = t1.交易日期 order by 成交量 desc, 代码)
 order by 交易日期, 成交量 desc, 代码
go

-- 方案2：top N + Row_Number() + 临时表
select row_number() over(partition by 交易日期 order by 成交量 desc, 代码) as row_num, * 
 into #tb_top from stock_YJY
select * from #tb_top Where row_num < 4
order by 交易日期, row_num
go
drop table  #tb_top
go

-- 方案3：cross apply
-- cross apply + 子查询
select t1.* from  stock_YJY  t1  cross apply
    (select  top(3)  *  from  stock_YJY  t2 where  t2.交易日期 = t1.交易日期 order  by 成交量 desc, 代码) t3
    where t1.交易流水 = t3.交易流水 
    order by t1.交易日期, t1.成交量 desc, t1.代码
go

-- cross apply + 表值函数
-- 表值函数定义
create function GetTopJY(@JY_Date date, @nn int)
returns table
as
return select top (@nn) 交易流水,代码, 成交量, 交易日期  from stock_YJY  
        where 交易日期 = @JY_date order by 成交量 desc
go
-- 表值函数调用
select t1.交易流水, t1.代码, t1.成交量, t1.交易日期
  from stock_YJY t1 cross apply GetTopJY(t1.交易日期, 3) t3
    where t1.交易流水 = t3.交易流水 
     order by t1.交易日期, t1.成交量 desc, t1.代码
go
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
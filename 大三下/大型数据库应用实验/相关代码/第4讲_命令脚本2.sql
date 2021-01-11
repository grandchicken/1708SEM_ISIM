-- 4.4 流程控制代码示例
-- 分支语句: 示例1
Declare @JY_QTY int, @JY_Money int
If exists (select * from stock_JY where 代码 = '600356')
Begin
       Select @JY_QTY = 成交量, @JY_Money = 成交额 from stock_JY  where  代码 = '600356'
	   Print '-----stock 600536 成交信息-------'
       Print  '成交量' + convert(varchar(20), @JY_QTY)
       Print  '成交额' + convert(varchar(20), @JY_Money)
End
Else
       Print '没有该股票！'
go 

-- 分支语句: 示例2
INSERT stock_JY(代码, 名称) VALUES ('999999', '测试名称')
go
IF @@error <> 0 
      PRINT '我出现错误'
ELSE 
      PRINT '我插入记录成功'
go
select * from stock_JY where 名称 like '测试%'
delete  FROM stock_JY where 名称 = '测试名称'
go

-- case语句
SELECT 代码, 名称, 成交量, 最新价, 价位 =  CASE
    WHEN 最新价 IS NULL THEN '信息缺失'
    WHEN 最新价 < 10  THEN '低价'
    WHEN 最新价 between 10 and  20  THEN '中价'
    WHEN 最新价 > 20 THEN '高价'
  END
FROM stock_JY
go

-- 循环结构
-- 示例1：计算1+2+3+……+100的和
DECLARE  @ii  Int,  @sum  Int
SELECT  @ii=1,  @sum =0
WHILE  @ii<=100
    SELECT @sum=@sum+@ii,  @ii=@ii+1
PRINT  @sum
go

-- 示例2：求1-100之间被7整除的整数和
Declare @number smallint, @sum smallint
Set @number = 1
Set @sum = 0
While @number <= 100
Begin
   If @number % 7 = 0
   Begin
      Set @sum = @sum + @number
      Print @number
   End
   Set @number = @number + 1
End
Print '1到100之间能被7整除的整数和为'+str(@sum)
go

-- 错误处理:
Begin try
       Select 8/2
       select 8/0
       print 'aa'
End try
Begin catch
       Select Error_number() as 错误号,  Error_severity() as 错误等级,
              Error_state() as 错误状态, Error_procedure() as 错误过程,
              Error_line() as 错误行,    Error_message() as 错误信息
End catch
go

-- goto语句
Declare @price float
select @price = 最新价 from stock_JY where 代码 = '600356'                                             
If @price < 10
    Goto print1
Else
    Goto print2
print1:
    Print '低价' 
    Goto theEnd
print2:
    Print '高价' 
    Goto theEnd
theEnd:
    return
go

-- 暂停语句 waitfor
Waitfor delay '00:00:05'
update stock_JY set 最新价 = 19.99 where 代码 = '600356'
select * from stock_JY where 代码 = '600356'
go
Waitfor time '15:26'
update stock_JY set 最新价 = 1.00 where 代码 = '600738'
select * from stock_JY where 代码 = '600738'
go


--4.5 T-SQL函数代码示例

-- 1）日期函数
-- 返回表示指定日期的年份、月份、日期的整数 
select year(getdate()) 年份, month(getdate()) 月份, day(getdate()) 日期  
select year(getdate()) +  month(getdate()) + day(getdate()) 
go

-- 返回指定日期的指定部分的整数 
select datepart(year,getdate()) 年, datepart(month,getdate()) 月, datepart(day,getdate()) 日 , datepart(week,getdate()) 周
select datepart(hour,getdate()) 时, datepart(minute,getdate()) 分, datepart(second,getdate()) 秒
select datepart(hour,getdate()) + datepart(minute,getdate()) + datepart(second,getdate()) 
go

select datepart(week, getdate()), datepart(week, getdate()) + datepart(week, getdate())
select datepart(weekday, getdate()), datepart(weekday, getdate()) + datepart(weekday, getdate())
go

-- 返回表示指定日期的年份、月份、日期的字符串数据 
declare @Yname char(4), @Mname char(2), @Dname char(2) 
select @Yname = datename(year,getdate()), @Mname = datename(Month, getdate()), @Dname = datename(day,getdate())
print @Yname + '年' + @Mname + '月' + @Dname + '日' 
go
declare @Hour_name varchar(10), @Minute_name  varchar(10), @Second_name varchar(10) 
select @Hour_name  = datename(hour,getdate()), @Minute_name = datename(minute, getdate()), @Second_name = datename(second,getdate())
print @Hour_name  + '点' + @Minute_name  + '分' + @Second_name+ '秒' 
go
select datename(week, getdate()), datename(weekday, getdate())

-- 日期数据运算，可以用来自动生成日期数据
select dateadd(year,4,getdate()) 加4年,  dateadd(month,14,getdate()) 加14个月, dateadd(day,300,getdate()) 加300天 
go
select datediff(day,getdate(), dateadd(month,14,getdate()))    --后面日期 减去 前面日期
select datediff(week,getdate(), dateadd(month,12,getdate()))    
select datediff(hour, getdate(), dateadd(day,2,getdate()))    
select datediff(minute, getdate(), dateadd(day,2,getdate()))    
select datediff(second, getdate(), dateadd(day,2,getdate()))    

go

declare @dt1 date
set @dt1 = '1997-05-19'
SELECT datediff(year,@dt1, getdate())as 年龄 , datediff(day,@dt1, getdate())as 天数 
GO


-- 数学函数
-- 取近似值
select Ceiling(3.1415926) 上限, Floor(3.1415926) 下限, Round(3.1415926, 2) 二位小数精度 ,Round(3.1415926, 3) 三位小数精度
-- 生成0至99之间的随机整数
select cast( floor(rand()*100) as int)

-- 生成1至100之间的随机整数
Select cast(ceiling(rand() * 100) as int)

-- 字符串函数
select ascii('abc'), ascii('a'),  ascii('b')
select Ltrim(Rtrim(str(45))) + Rtrim(ltrim(str(12)))+ char(100)
select Str (3.1415926,10, 4)
select left('I am a student', 6)
select subString('I am a student', 6, 10)    
select charIndex('student', 'I am a student')    
select replace('I am a student，you are a student', 
                            'student',  'teacher')
go

-- 统计函数
select AVG(最新价) AS '均值' , STDEV(最新价) AS '标准偏差' , VAR(最新价) AS '方差' ,
       MAX(最新价) AS '最大值' , MIN(最新价) AS '最小值' , COUNT(最新价) AS '数量',
	   MAX(最新价) - MIN(最新价) AS '极差值' , STDEV(最新价) / AVG(最新价) AS '变异系数' 
from stock_JY 

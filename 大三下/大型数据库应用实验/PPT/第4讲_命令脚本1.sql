-- 第4讲 脚本文件

-- 4.1 语言基础
-- Print语句
Print 'Hello！'
print 55
declare @rr datetime
set @rr = '2020-03-11'
print @rr            
print @@version
select * FROM Stock_JY  where 代码 >  '60050'
print '我查询到了'+CAST(@@rowcount as varchar(5))+'条记录'
go


-- 4.2 数据类型
-- 十六进制类型举例
declare @rr binary
set @rr = 0x4A
print @rr            
print CAST(@rr as int)
go

-- date、money类型举例
declare @rr1 date
set @rr1 = '2020/03/11'
print @rr1 

declare @rr2 decimal(6,4)
set @rr2 = 13.12
print @rr2

declare @rr1 money, @rr2 money
set @rr1 = 13.122323
set @rr2 = 13.128989
print @rr1
print @rr2
go

-- 位类型举例
declare @rr1 bit
set @rr1 = 1
print @rr1
print CAST(@rr1 as int)

declare @rr2 int
set @rr2 = 0
print @rr2
print CAST(@rr2 as bit)
go

-- 时间戳类型举例
create table SF_rec (ts_field timestamp not null,
                     sno char(8) not null,
                     fee money) 
insert into SF_rec(sno, fee) values ('s001', 100)
insert into SF_rec(sno, fee) values ('s002', 200)
select * from SF_rec
go


-- 数据类型转换

--Cast函数
select '股票' + CAST(代码 as char(10)) +
       '的成交价为：' + CAST(最新价 as varchar(20)) +
       '元' AS 成交信息  
  from stock_JY
go
  
--convert函数和转换样式
select  CONVERT(VARCHAR(19),GETDATE()) as '缺省',    
        CONVERT(VARCHAR(10),GETDATE(),110) as '110',
        CONVERT(VARCHAR(11),GETDATE(),106) as '106',  
        CONVERT(VARCHAR(24),GETDATE(),113) as '113'
go
 
--自动类型转换 
declare @unitprice float, @unitsinstock int
select @unitprice = 12.234, @unitsinstock = 18
SELECT @unitprice * @unitsinstock AS je
go      

declare @unitprice float, @unitsinstock char(2)
select @unitprice = 12.234, @unitsinstock = '18'
SELECT @unitprice * @unitsinstock + 600 AS je
go 

declare @unitprice float, @unitsinstock datetime
select @unitprice = 12.234, @unitsinstock = '2019-03-30'
SELECT @unitprice * @unitsinstock AS je
go 


-- 4.3 常量、变量和表达式

-- 全局变量
select * FROM stock_JY  where name > '600500'
go
print '输出错误编号：' + convert(varchar(20),@@ERROR)
go


select * FROM stock_JY  where 代码 > '600500'
go
print '输出影响行数：' + convert(varchar(20),@@ROWCOUNT)
go

-- 赋值
declare @tt1  varchar(20),  @tt2  varchar(20)
declare @price_L float, @price_C int
Select @price_C = 1
print '输出常数' + convert(varchar(10), @price_C)
set @tt1 = (select min(代码) from stock_JY)
print '最小股票代码' + @tt1
set @tt2 = (select max(代码) from stock_JY)
print '最大股票代码' + @tt2
select @price_L = min(最低价)+3 from stock_JY 
print '最低成交价' + convert(varchar(30), @price_L)
go

-- 运算符
select 24%5
declare @b1 bit, @b2 bit
select @b1 = 0, @b2 = 1
select @b1 & @b2 as 与,   @b1 | @b2 as 或,
       ~@b1 as 非,        @b1 ^ @b2 as 互斥
go

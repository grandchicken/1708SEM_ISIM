-- 5.1 存储过程
-- 1、默认值参数
if object_id('SpStockById') is not null
drop proc SpStockById
go

create proc SpStockById
@Stock_id nvarchar(10) = null     -- 设置参数和默认值
as
if  (@Stock_id is not null)              -- 判断参数是否为空
    select * from stock_JY  where 代码 = @Stock_id
else
    select * from stock_JY
go

exec SpStockByID	             --使用默认值
exec SpStockById '600356'     --使用参数
go

-- 2、带Return参数的存储过程 
if object_id('query_qty') is not null
drop proc query_qty
go

create proc query_qty @s_id char(8)
as
declare @JY_qty int
select @JY_qty = Ceiling(成交量) from stock_JY 
              where 代码 = @s_id
return @JY_qty
go

declare @rtn_qty int
exec @rtn_qty = query_qty '600356'
print @rtn_qty
go
 
-- 3、递归调用  
if object_id('UpFactorial') is not null
drop proc UpFactorial
go
Create proc UpFactorial
@Value_In int,  @Value_Out int OUTPUT    -- 输入、输出参数
as
declare @D_In int,  @D_Out int                    -- 传入、接收变量
if @Value_In > 1
begin
    select @D_In = @Value_In - 1;  
    exec UpFactorial @D_In, @D_out OUTPUT          -- 递归调用
    select @Value_Out = @Value_In * @D_Out
end
else
    select @Value_Out =1  
print cast(@Value_In as varchar) + 
         ' factorial is '+ cast(@Value_Out as varchar);
Return
GO

declare @WorkingOut int
exec UpFactorial 5, @WorkingOut OUTPUT
print @WorkingOut
 
-- 5.2 临时表和表变量

-- 1、本地临时表
if object_id('Test1') is not null
drop proc Test1
go
Create Procedure Test1
AS
Create table #t1 (TC1 int  PRIMARY KEY)
Insert into #t1 values (99)
Exec Test2
go

if object_id('Test2') is not null
drop proc Test2
go
Create Procedure Test2
AS
Insert into #t1 values (88)
Create table #t2 (TC2 int PRIMARY KEY)
Insert into #t2 values (11)
SELECT * from #t1
SELECT * from #t2
go

Create table #t3 (TC3 int PRIMARY KEY)
Insert into #t3 values (555)
Create table #t1 (TC1 int PRIMARY KEY)
Insert into #t1 values (444)
Exec Test1
Select * from #t1
Select * from #t3
Select * from #t2
go

drop table #t3
drop table #t1
go

-- 2、全局临时表
if object_id('FindTemptable') is not null
drop proc FindTemptable
go
create proc FindTemptable   
@View_userID varchar(20),              --输入参数：操作员账号
@outResult int out                     --输出参数（0没有登录，1已经登录）
as   
declare @View_sql varchar(100)  
if object_id ('tempdb.dbo.##' + @View_userID) is null  
begin   
   set @View_sql = 'create table ##' + @View_userid + ' (userid char(20)) '  
   exec(@View_sql)
   set @View_sql = 'insert into ' + '##'+@View_userID + ' values (1)'  
   exec(@View_sql)   
   set @outResult =0
   print '可以登陆'  
end   
else
begin   
    set @outResult =1  
    print '已经登陆'
end
Return
go

declare @dl_state int
exec FindTemptable  'stu1', @dl_state output
print @dl_state
go

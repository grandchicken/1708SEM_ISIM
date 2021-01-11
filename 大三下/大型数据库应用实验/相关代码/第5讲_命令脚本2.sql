--第5讲 脚本2
-- 5.3 自定义函数  UDFs
--1、标量函数
create function stock_code (@stock_name char(20))
returns varchar(10)
as 
begin
      declare @stock_code varchar(10)
      select @stock_code = 代码  from stock_JY 
			    where  名称 = @stock_name 
      return @stock_code 
end
go
select * from stock_JY where 代码 = dbo.stock_code('恒丰纸业')
go

declare @s_code1 varchar(10), @s_code2 varchar(10)
Set  @s_code1 = dbo.stock_code('恒丰纸业')
set  @s_code2 = dbo.stock_code('东方电子')
select '恒丰纸业'   股票名称, @s_code1  股票代码
select '东方电子'  股票名称, @s_code2   股票代码
go

--2、内联表值函数
create function TabDmess(@stock_name varchar(50))
returns table 
as 
return (select 代码, 名称, 最新价 from stock_JY            
         where 名称 like '%' + @stock_name+'%')
Go
select * from TabDmess('电子')
go

-- 3、多语句表值函数
create function StockCJ(@Lmt_P money)
returns @StockMess table (s_id char(6),
                          s_name char(20),
                          s_price money,
                          qty int)
as
begin
   insert into @StockMess
      select stock_JY.代码, 名称, 最新价, 成交量
        from stock_JY 
       where 最新价 > @Lmt_P
	insert into @StockMess values ('000111', 'My Stock', '155.55', '1000')
   return
end
go
select * from StockCJ(100)
go

-- 5.4  自定义函数应用
-- （1）提取中文字符串
create function fun_getCN(@str nvarchar(1000))
returns nvarchar(1000)    
as   
begin   
     declare @word nchar(1), @CN nvarchar(1000)     --@str存储原始字符串
     set  @CN = ''   
     while len(@str) > 0    
     begin   
         set @word = left(@str,1)    
         if unicode(@word) between 19968 and  19968 + 20901  
              set  @CN = @CN + @word                  --@CN存储返回的中文字符串
         set  @str = right(@str, len(@str) - 1)    
     end   
     return  @CN
end   
go
select dbo.fun_getCN('ASKG论as坛KDL'),  dbo.fun_getCN('ASDKG論y壇KDL'),
       dbo.fun_getCN('AS中DK国DL'), dbo.fun_getCN('ASKG北京ll34热爱aKDL')
go

-- （2）提取数字
create function get_number(@s varchar(100))
returns varchar(100)
as
begin
      while patindex('%[^0-9]%', @S) > 0
            set @s=stuff(@S, patindex('%[^0-9]%', @s), 1, '')
       return  @S
end 
Go
select DBO.GET_NUMBER('练习A1B2C3ABC')
go

-- （3）过滤重复字符
CREATE FUNCTION DBO.DISTINCT_STR2(@S varchar(8000)) 
 RETURNS VARCHAR(100)
 AS
 BEGIN
       IF @S  is NULL  Return NULL
       Declare  @New  Varchar(50)
       While  Len(@S)>0
       BEGIN
            SET @New=ISNULL(@New, '') + LEFT(@S,1)
            SET @S=Replace(@S, LEFT(@S, 1), '')
       END
       RETURN @NEW
 END
 GO
SELECT DBO.DISTINCT_STR2('ABabdcCDfgrabcbABCacdf')
SELECT DBO.DISTINCT_STR2('ABabABab')
go

-- 5.4 游标
create procedure S_PLevel @s_name varchar(20) As
Declare @s_id varchar(10), @price money, @cje money
Declare @AB_cje money, @CD_cje money, @E_cje money
Declare @AB_cnt int, @CD_cnt int, @E_cnt int
Declare @L_tb1 table (Lev_type varchar(20), s_id varchar(10), price money, cje money, Lev_desc varchar(50))
Declare @L_tb2 table (Lev_type varchar(20), stock_cnt int, stock_cje money)
Declare s_cur cursor for  Select 代码, 最新价,成交额 from stock_JY where 名称 like '%' + @s_name + '%'
select @AB_cje=0,  @CD_cje=0,  @E_cje=0
select @AB_cnt=0,  @CD_cnt=0,  @E_cnt=0
Open s_cur
Fetch s_cur into @s_id, @price, @cje
While (@@fetch_status = 0)
 Begin
      if (@price >= 50)
      begin
     	 insert into @L_tb1 (Lev_type, s_id, price, cje, Lev_desc)
     	     values ('AB', @s_id, @price,@cje, '高价位')
         select @AB_cje = @AB_cje + @cje
		 select @AB_cnt = @AB_cnt + 1
      end  
      else if (@price  >= 20)
      begin
          insert into @L_tb1 (Lev_type, s_id, price, cje, Lev_desc)
	          values ('CD', @s_name, @price, @cje, '中价位')
          select @CD_cje = @CD_cje + @cje
		  select @CD_cnt = @CD_cnt + 1
      end
      else
      begin
          insert into @L_tb1 (Lev_type, s_id, price, cje, Lev_desc)
	       	  values ('E', @s_name, @price, @cje, '低价位')
          select @E_cje = @E_cje + @cje
		  select @E_cnt = @E_cnt + 1
      end
      Fetch s_cur into @s_id, @price, @cje
end
Close s_cur
Deallocate s_cur
insert into @L_tb2 values ('AB', @AB_cnt, @AB_cje)
insert into @L_tb2 values ('CD', @CD_cnt, @CD_cje)
insert into @L_tb2 values ('E', @E_cnt, @E_cje)
select * from @L_tb1
select * from @L_tb2
return
go

exec S_PLevel '电子'

-- 5.5 数据准备
-- 1. 创建表
CREATE TABLE stock(
	代码 varchar(10) NOT NULL PRIMARY KEY,
	名称 varchar(20) NOT NULL,
	描述 ntext NULL)
go
drop TABLE stock_YJY
go
CREATE TABLE stock_YJY(
	交易流水 int Identity(1,1) NOT NULL PRIMARY KEY,
	代码 varchar(10) NOT NULL,
	最新价 money NULL,
	最高价 money NULL,
	最低价 money NULL,
	最低价近似 money NULL,
	成交量 int NULL,
	成交额 money NULL,
	交易日期 date NULL)
go

-- 2、生成数据
-- （1）插入股票基本信息
insert into stock(代码, 名称) select 代码, 名称 FROM stock_JY

-- (2) 插入股票100天交易数据
insert into stock_YJY (代码, 最新价,最高价, 最低价, 成交量, 成交额, 交易日期)
   select 代码, 最新价,最高, 最低价, 成交量, 成交额, '2020-01-01' from stock_JY order by 代码
declare @ii int 
select @ii = 1
while (@ii<= 100)
begin
  insert into stock_YJY (代码, 最低价, 成交量, 交易日期)
     select 代码, 最低价*(0.5+rand()), 成交量*(0.5+rand()), 
	        DateAdd(day, @ii, '2020-01-01')
	   from stock_JY order by 代码  
   set @ii = @ii + 1
end
update stock_YJY
  set  最高价 = 最低价*(1+rand()),  最低价近似 = ceiling(最低价)
update stock_YJY
  set 最新价 = 最低价+(最高价-最低价)*rand(),
      成交额 = 成交量*(最高价+最低价)/2
go

--3、查看数据
select * from stock
select * from stock_YJY order by 代码, 交易日期

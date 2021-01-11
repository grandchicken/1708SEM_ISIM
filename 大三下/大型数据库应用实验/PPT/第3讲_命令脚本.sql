-- 第3讲脚本  --数据导入导出

-- 1、参数配置
EXEC sp_configure 'show advanced options', 1 
go
RECONFIGURE 
go
EXEC sp_configure 'xp_cmdshell', 1 
go
RECONFIGURE
go 

-- 2、BCP 数据导出

--（1）数据导出——可信连接
EXEC master..xp_cmdshell 
'bcp T_demo2020.dbo.Stock_JY out E:\BUAA\stock_exchange_data.txt -T -c'

--（2）数据导出——账号连接
EXEC master..xp_cmdshell 
'bcp T_demo2020.dbo.Stock_JY out E:\BUAA\stock_exchange_data2.txt -c -Usa -Psa'

--（3）数据导出——查询导出
EXEC master..xp_cmdshell 
'bcp "SELECT 代码, 名称 FROM T_demo2020.dbo.Stock_JY" queryout E:\BUAA\stock_exchange_data3.txt -T -c'

-- 3、BCP 数据导入
-- （1）准备数据表
select * into Stock_JY2 from Stock_JY
go
delete from Stock_JY2
go
select * from Stock_JY2
go

-- （2）导入数据
EXEC master..xp_cmdshell 
'bcp T_demo2020.dbo.Stock_JY3 in E:\BUAA\stock_exchange_data.txt -c -T'
go
select * from Stock_JY2
go

-- 4、BCP 格式文件导出
EXEC master..xp_cmdshell 
'BCP T_demo2020.dbo.Stock_JY format nul -f E:\BUAA\stock_exchange_fmt.xml -x -c -T' 
go

-- 5、BULK 数据导入
-- （1）准备数据表
select * into Stock_JY3 from Stock_JY
go
delete from Stock_JY3
go
select * from Stock_JY3
go

--（2）数据导入
BUlk insert  T_demo2020.dbo.Stock_JY3 from 'E:\BUAA\stock_exchange_data.txt'
	with (formatfile = 'E:\BUAA\stock_exchange_fmt.xml')
go
select * from Stock_JY3
go

--（3）按需选取字段 
select 代码,名称,成交额 into T_demo2020.dbo.Stock_JY4
    FROM OpenRowSet(BULK N'E:\BUAA\stock_exchange_data.txt',                   
    FORMATFILE=N'E:\BUAA\stock_exchange_fmt.xml') 
    AS new_table_name 
go
select * from Stock_JY4
go

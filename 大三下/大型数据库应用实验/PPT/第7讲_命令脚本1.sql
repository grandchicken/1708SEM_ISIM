-- 7.1 大对象访问

-- 1、增加大对象数据列
alter table stock add s_profile text
alter table stock add s_photo image
alter table stock add s_photo_type nchar(10)
go

-- 2、环境设置
sp_configure 'show advanced options',1
go
sp_configure 'Ad Hoc Distributed Queries',1
go
sp_tableoption N'dbo.stock', 'text in row', 'off'
go
reconfigure
go

-- 3、使用 SELECT、UPDATE 和 INSERT 引用大对象数据列
select * from stock   where 描述 = 'good stock'
go
delete from stock   where 描述 = 'good stock'
go
select * from stock   where 描述 like  '%good%'
go

--4、使用 OPENROWSET 插入带有大对象数据
Insert Into stock (代码, 名称, 描述, s_photo)
select 'ss99991' as 代码, 'zzzz' as 名称, *
    from OPENROWSET(BULK 'E:\buaa\A3_DataAndCode\ss99991.txt', SINGLE_CLOB) as 描述, 
         OPENROWSET(BULK 'E:\buaa\A3_DataAndCode\ss99991.jpg', SINGLE_BLOB) as s_photo
                   
select 代码, 名称, 描述, s_photo from stock where 代码 like 'ss%'
go
/*
--4、操纵小规模数据
select * from stock where s_id like 'ss%'  and s_profile is not null
select * from stock where s_id like 'ss%'  and s_profile is null

select * from stock where s_id like 'ss%'  and s_profile like '%促进%'
update stock set s_desc = 'aqwszx' where s_id ='ss001'

select * from stock where s_id like 'ss%'  and s_desc = 'aqwszx'     --报错
select * from stock where s_id like 'ss%'  and s_desc like 'aqwszx%'
*/

--5、使用 WriteText 函数, 写入文本内容
DECLARE @ptr_val binary(16)
SELECT @ptr_val = TextPtr(描述) From stock Where 代码 = 'ss99991'
WriteText  stock.描述  @ptr_val 
'2019年4月更新后__维数约简是计算机视觉、机器学习与模式识别等领域的一种重要研究课题．数据转换是维数约简的一种重要方法，
它将高维数据按一定要求转换到相对低维空间中，使得数据在低维空间中能使用现有的方法解决问题'
select 代码, 名称, 描述 from stock where 代码 like 'ss%'
go

--6、使用UpdateText函数，局部更新文本
DECLARE @ptr_val  binary(16)
SELECT @ptr_val = TEXTPTR(描述)  From stock  Where 代码 = 'ss99991'
UpdateText stock.描述 @ptr_val 0 3 '所谓的'		   --描述是ntext类型
SELECT *  From stock  Where 代码 = 'ss99991'
go

--7、读大文本数据
DECLARE @ptr_val binary(16)
SELECT @ptr_val = TEXTPTR(描述)  From stock  Where 代码 = 'ss99991'
READTEXT stock.描述 @ptr_val 4 6									

SELECT 代码, SUBSTRING(描述, 3, 6) AS 描述 From stock  Where 代码 = 'ss99991'

SELECT * From stock  Where 代码 = 'ss99991'
go
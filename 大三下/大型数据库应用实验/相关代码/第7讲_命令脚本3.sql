-- 7.3 XML数据访问
-- 一、XML 数据类型
-- 1、创建表带有XML数据的数据表
Create Table S_inf (
           s_id char(5) not null primary key,
           xml_name  char(20) null,
           xml_content xml null )
go

-- 2、定义XML类型的变量并赋值
declare @doc xml
select @doc = N'<note>
                   <to> wang </to>
				   <from age = "20"> zhang </from>
				   <heading> Reminder </heading>
				   <body> Do not forget me this weekend! </body>
				   <number> 12 </number>
			   </note>'
select @doc 
go

-- 二、XML 数据写入
-- 1、以字符串形式向表S_inf 插入一个包含XML数据的元组
INSERT INTO S_inf 
     VALUES('ss001', 'note.xml', '<note>
									<to>wang</to>
							 		<from age="20">zhang</from>
									<heading>Reminder</heading>
									<body>Do not forget me this weekend!</body>
							      </note>')
INSERT INTO S_inf 
     VALUES('ss002', 'stu.xml', '<school>
									<class>
						 				<student number="081101">
											<name>王林</name>
											<sex>男</sex>
											<age>20</age>
										</student>
										<student number="6666666">
											<name>sdfgh返回</name>
											<sex>女</sex>
											<age>21</age>
										</student>
									</class>
								</school>')
go

-- 2、使用 OpenRowSet 函数将 XML 文件导入到数据表
INSERT INTO S_inf(s_id, xml_name, xml_content)
 SELECT 'ss003', 'note' AS xml_name, * 
		FROM OpenRowSet(BULK N'E:\buaa\A3_DataAndCode\note.xml', SINGLE_CLOB)  AS note_content
go

-- 三、XML查询
-- 1、query()方法
SELECT  s_id, xml_content.query('/note/body') from S_inf
SELECT  s_id, xml_content.query('/note') from S_inf
go

DECLARE @xmldoc xml
Select @xmldoc = xml_content from S_inf where s_id = 'ss003'
SELECT @xmldoc.query('/note') 
SELECT @xmldoc.query('/note/from') AS 信息 
SELECT @xmldoc.query('.') AS 信息
go

DECLARE @xmldoc xml
SET @xmldoc = 
'<school>
    <class>
      <student>
         <name>王林</name>
         <gender>男</gender>
        <age>20</age>
      </student>
      <student>
         <name>何丽</name>
         <gender>女</gender>
         <age>21</age>
      </student>
    </class>
 </school>'
 select @xmldoc.query('/school/class/student/name')
go

-- 2、value()方法
--（1）元素值查询
INSERT INTO S_inf 
VALUES('ss004', 'aaa.xml',
'<school>
    <class>
      <student>
         <name>王林</name>
         <gender>男</gender>
        <age>20</age>
      </student>
      <student>
         <name>何丽</name>
         <gender>女</gender>
         <age>21</age>
      </student>
    </class>
    <class>
      <student>
         <name>王芳</name>
         <gender>女</gender>
        <age>18</age>
      </student>
    </class>
 </school>')
 go
  
select s_id,xml_name,xml_content.value('(/school/class)[1]', 'varchar(50)') 
from S_inf where s_id = 'SS004'

select s_id,xml_name,xml_content.value('(/school/class)[2]', 'varchar(50)') 
from S_inf where s_id = 'SS004'

select s_id,xml_name,xml_content.value('(/school/class/student)[3]', 'varchar(50)') as XML值
from S_inf where s_id = 'SS004'

select s_id,xml_name,xml_content.value('.', 'varchar(50)') as XML值
from S_inf  where s_id = 'SS004'
go

--（2）value()方法：属性值检索
INSERT INTO S_inf VALUES ('ss005', 'zz.xml', 
N'<school>
	<class>
	   <student number="081101">
	  	   <name>王林</name>
		   <sex>男</sex>
		   <age>20</age>
	   </student>
	   <student number="081102">
		  <name>何丽</name>
		  <sex>女</sex>
		  <age>21</age>
	   </student>
    </class>
	<class>
	   <student number="020101">
	  	  <name>王芳</name>
		  <sex>女</sex>
		  <age>18</age>
	   </student>
   </class>
</school>')
go

select s_id,xml_name,xml_content.value('(/school/class/student/@number)[1]','char(6)')
from S_inf where s_id = 'ss005'

select s_id,xml_name,xml_content.value('(/school/class/student/@number)[3]','char(6)')
from S_inf where s_id = 'ss005'
go

-- 3、exists 查询
select s_id, xml_content, xml_content.exist('/school/class/student/name') 元素判断,       
       xml_content.exist('/school/class/student/@number') 属性判断
  from S_inf 
go              

-- 四、XML数据更新：modify()方法
-- 1、插入数据

-- （1）插入单个元素
update S_inf
   set xml_content.modify
       ('insert <birthday> 1997-02-10 </birthday> after 
         (/school/class/student/age)[2]')
where s_id = 'ss005'
go

-- （2）插入同级节点，包含多个元素
update S_inf
   set xml_content.modify
       ('insert <class>
                   <student>
                       <name>赵名</name>
                       <age>20</age>
                       <gender>男</gender>
                   </student>
                </class> 
         before (/school/class)[1]')
where s_id = 'ss005'

SELECT * from S_inf where s_id = 'ss005'
go

-- （3）插入子节点，包含多个元素
DECLARE @xmldoc xml
SET @xmldoc = '<school>
					<class>
						<student> <name>王林</name>  <sex>男</sex> <age>20</age> </student>
						<student> <name>张明</name>  <sex>男</sex> <age>18</age> </student>
					</class>
					<class>
						<student> <name>王林</name> <sex>男</sex>  <age>20</age> </student>
					</class> 
				</school>'
SET @xmldoc.modify('insert <student>
								<name>孙梅</name>
								<sex>女</sex> 
								<age>21</age> </student>
					as last into (/school/class)[2]')
SELECT @xmldoc 插入节点后数据
go

-- 2、删除数据
SELECT  s_id, xml_content.query('/school') from S_inf where s_id = 'ss005'
update S_inf
set xml_content.modify('delete (/school/class/student/gender)[1]')
where s_id = 'ss005'
   
DECLARE @xmldoc xml
SET @xmldoc= '<student><name>王林</name><sex>男</sex> <age>20</age> </student>'
SET @xmldoc.modify('delete (/student/age)[1]')
select @xmldoc
go

-- 3、更新数据
SELECT  s_id, xml_content.query('/school') from S_inf where s_id = 'ss005'
update S_inf
SET xml_content.modify('replace value of 
       (/school/class/student/name/text())[2] with "mmmmmmm"')
where s_id = 'ss005'

update S_inf
SET xml_content.modify('replace value of 
       (/school/class/student/@number)[2] with "6666666"')
where s_id = 'ss005'

DECLARE @xmldoc xml
SET @xmldoc= '<student>
                  <name number="081101">王林</name>
                  <sex>男</sex>
                  <age>20</age>
              </student>'
SELECT @xmldoc AS 更新节点前数据
SET @xmldoc.modify('replace value of (/student/name/@number)[1] with "091101" ')
SET @xmldoc.modify('replace value of (/student/name/text())[1] with "张林"')
SELECT @xmldoc 更新节点后数据
go

-- 五、关系数据和XML数据转换
-- 1、关系数据 到 XML数据
-- （1）FOR XML RAW

select 代码, rtrim(名称) as 名称 from stock  where 代码 like 'ss%'	
   FOR XML RAW

--自定义元素名称
select 代码, rtrim(名称) as 名称 from stock  where 代码 like 'ss%'	
  FOR XML RAW('股票')
go

--（2）FOR XML AUTO
-- FOR XML AUTO：单表自动模式
select 代码, rtrim(名称) as 名称 from stock  where 代码 like 'ss%'	
 FOR XML AUTO
 
-- FOR XML AUTO：双表自动模式
SELECT stock.代码, rtrim(stock.名称) as 名称, 交易流水, 交易日期, 成交量 from stock, stock_YJY  
where stock.代码 = stock_YJY.代码 and stock.代码 < '000006' and 交易流水 < 8000
  order by stock.代码, 交易日期
 FOR XML AUTO
  
--（3）FOR XML PATH
-- FOR XML PATH：简单应用
select 代码, rtrim(名称) as 名称 from stock  where 代码 like 'ss%'	FOR XML PATH

-- FOR XML PATH：定义元素属性
select 代码 AS '@股票编号', rtrim(名称) as 名称 from stock  where 代码 like 'ss%'	FOR XML PATH

-- FOR XML PATH：定义层次元素
SELECT stock.代码 as '@股票编号', 名称 as '基础信息/公司名称', 描述 as '基础信息/公司描述',
       交易流水 as '交易记录/交易编号', 交易日期 as '交易记录/交易日期', 成交量 as '交易记录/成交量'
   FROM stock, stock_YJY  
   where stock.代码 = stock_YJY.代码 and stock.代码 < '000003' and 交易流水 < 4000
   order by stock.代码, 交易日期
   FOR XML Path ('股票信息')
 go

-- 2、XML到关系数据
--（1）创建xml文档
declare @mydoc xml
set @mydoc='<Person>
				<row FirstName="Gustavo" LastName="Achong" />
				<row FirstName="Catherine" MiddleName="R." LastName="Abel" />
			</Person>'
 
--（2）获得XML文档的句柄
declare @docHandle int
exec sp_xml_preparedocument @docHandle OUTPUT, @mydoc

--（3）写入Table
SELECT * into GenXML FROM OPENXML(@docHandle,'/Person/row',1)   
    WITH (FirstName nvarchar(50),
          MiddleName nvarchar(50),
          LastName nvarchar(50))
go
select * from GenXML

--不同参数示例
declare @mydoc xml
set @mydoc='
<Products>
  <Product Category="Book">
    <Name>Windows 2008</Name>
    <Vendor>Vendor1</Vendor>
  </Product>
  <Product Category="Book">
    <Name>SQL2008</Name>
    <Vendor>Vendor2</Vendor>
  </Product>
</Products>'

declare @docHandle int
Exec sp_xml_preparedocument @docHandle OUTPUT,@mydoc

SELECT * into GenXML21 FROM  OPENXML(@docHandle,'/Products/Product',1)
WITH (Category nvarchar(50),Name nvarchar(50),Vendor nvarchar(50))

SELECT * into GenXML22 FROM  OPENXML(@docHandle,'/Products/Product',2)
WITH (Category nvarchar(50),Name nvarchar(50),Vendor nvarchar(50))

SELECT * into GenXML23 FROM  OPENXML(@docHandle,'/Products/Product',3)
WITH (Category nvarchar(50),Name nvarchar(50),Vendor nvarchar(50))
go
select * from GenXML21
select * from GenXML22
select * from GenXML23
go

drop table GenXML
drop table GenXML21
drop table GenXML22
drop table GenXML23
go


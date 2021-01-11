-- 7.2 全文检索
-- 1、启用全文索引
sp_fulltext_database 'enable';
go
Reconfigure
go

-- 2、contains
-- （1）简单搜索
select * from stock where 代码 like 'ss%'
select * from stock where contains(描述, '计算机')
select * from stock where contains(描述,'"计算机" or "区块链"')
go

-- （2）同源词检索
update stock set s_profile = 'I am running  I ran yesterday' where 代码 = '000006'        
update stock set s_profile = 'He runs everyday' where 代码 = '000007'     
insert into stock(代码,名称, s_profile) values('ss99992', 'ssss', 'He will run to school tomorrow')

select * From stock where contains(s_profile, 'formsof(inflectional, run)')
go
 
-- （3）加权搜索
SELECT * from  ContainsTable(stock, 描述,   
                'isabout ("数据" weight(0.3), "计算机" weight(0.6), "研究" weight(0.1))', 2)    --取top 2数据
                             
SELECT t2.rank, t1.* 
  from stock as t1, ContainsTable(stock, 描述,   
                    'isabout ("数据" weight(0.3), "计算机" weight(0.6), "研究" weight(0.1))', 2)  as t2
 where t1.代码 = t2.[KEY]
go

-- 3、使用FREETEXT的查询：拆分搜索、同源词搜索、非精确搜索结果不精确
--（1）contains的查询局限
SELECT * FROM stock where contains(s_profile, 'I am')      --报错，应该是单词、而非句子
go

--（2）FreeText查询
SELECT * FROM stock WHERE FREETEXT(描述, '计算机技术发展')   --非精确查询
SELECT * FROM stock WHERE FREETEXT(s_profile, 'ran')				--同源词查询
SELECT * FROM stock WHERE FREETEXT(s_profile, 'I ran')				--非精确句子查询
go
         
-- 4、使用FreeTextTable搜索
SELECT * FROM FreeTextTable(stock, s_profile, 'running yesterday', 2) 

SELECT t2.rank, t1.* 
  from stock as t1, 
       FREETEXTTABLE(stock, s_profile, 'running yesterday', 4) as t2
 where t1.代码 = t2.[key]
 go

 --5、Image数据检索示例
Insert Into stock (代码, 名称, s_photo_type, s_photo)
  select 'ss99993' as 代码, 'mmmm' as 名称, '.txt' as s_photo_type, * 
             from OPENROWSET(BULK 'E:\buaa\A3_DataAndCode\ss99993.txt', SINGLE_CLOB) as s_photo

SELECT convert(varchar(100), substring(s_photo, 0,40))
FROM  stock WHERE CONTAINS(s_photo, '数据')
go

-- 6、停用词表的开和关
ALTER FULLTEXT INDEX ON stock SET stoplist OFF
SELECT * FROM stock WHERE contains(s_profile, 'He')
ALTER FULLTEXT INDEX ON stock SET stoplist System
SELECT * FROM stock WHERE contains(s_profile, 'He')

--第二讲，2.1和2.2  课件中的脚本

use My_DB
go

--查看数据库文件信息
select * from My_DB.sys.database_files
go

--查看虚拟日志文件信息
dbcc TRACEON(3604) 
go
DBCC loginfo
go


--在指定文件组上创建数据库对象

--创建表，并指定表和大对象的存储位置
Create table stock 		
   ( s_id int not null primary key ,
     s_name char(20) not null,
     s_desc ntext null
   ) ON [PRIMARY] 
     TextImage_on My_FG2

Create  table stock_Exchange 	 
      ( s_id int not null primary key ,
        high decimal(18,6),
        low  decimal(18,6),
        day_close decimal(18,6),
         E_qty int,
         E_date datetime
 ) ON [PRIMARY] 
 go

--指定索引的存储位置
Create nonclustered index idx_name on stock(s_name) on My_FG2
go


--数据迁移、文件收缩、文件删除
--step 1：创建关系
Create table stock2 		
   ( s_id int not null primary key ,
     s_name char(20) not null,
     s_desc ntext null
   ) ON My_FG2
go


--step 2: 插入数据（略）
--step 3：删除文件
--step 4：收缩文件
--step 5：删除文件
-- 观察上述操作的结果
# 分类

- DDL: 数据定义语言，用来定义数据库对象（数据库、表、字段）
- DML: 数据操作语言，用来对数据库表中的数据进行增删改
- DQL: 数据查询语言，用来查询数据库中表的记录
- DCL: 数据控制语言，用来创建数据库用户、控制数据库的控制权限
***

# 类型

## 数值

| 类型          | 大小    | 有符号范围 (类型后加unsigned为无符号型)               | 描述               |
| ------------- | ------- | ----------------------------------------------------- | ------------------ |
| tinyint       | 1 byte  | (-128, 127)                                           | 微整数             |
| smallint      | 2 bytes | (-32768, 32767)                                       | 小整数             |
| mediumint     | 3 bytes | (-8388608, 8388607)                                   | 中整数             |
| int / integer | 4 bytes | (-2147483648, 2147483647)                             | 大整数             |
| bigint        | 8 bytes | (-2^63^, 2^63^-1)                                     | 极大整数           |
| float         | 4 bytes | (-3.402823466e+38, 3.402823466351e+38)                | 单精度浮点数       |
| double        | 8 bytes | (-1.7976931348623157e+308, +1.7976931348623157e+308,) | 双精度浮点数       |
| decimal       |         | 依赖 M(精度: 总位数)和 D(标度: 小数位数)的值          | 小数值(精确定点数) |

## 字符串

| 类型       | 大小 | 描述 |
| ---------- | ---- | ---- |
| char       | 0~255 bytes | 定长字符串 |
| varchar    | 0~65535 bytes | 变长字符串 |
| tinyblob   | 0~255 bytes | 不超过255字符的二进制数据 |
| tinytext   | 0~255 bytes | 短文本字符串 |
| blob       | 0~65 535 bytes | 二进制形式的长文本数据 |
| text       | 0~65 535 bytes | 长文本数据 |
| mediumblob | 0~16 777 215 bytes | 二进制形式的中等长度的文本数据 |
| mediumtext | 0~16 777 215 bytes | 中等长度文本数据 |
| longblob   | 0~4 294 967 295 bytes | 二进制形式的极大文本数据 |
| longtext | 0~4 294 967 295 bytes | 极大文本数据 |

## 日期

| 类型      | 大小 | 范围                                       | 格式                |
| --------- | ---- | ------------------------------------------ | ------------------- |
| date      | 3    | 1000-01-01 至 9999-12-31                   | YYYY-MM-DD          |
| time      | 3    | -838:59:59 至 838:59:59                    | HH:MM:SS            | 
| year      | 1    | 1901 至 2155                               | YYYY                |
| datetime  | 8    | 1000-01-01 00:00:00 至 9999-12-31 23:59:59 | YYYY-MM-DD          | 
| timestamp | 4    | 1970-01-01 00:00:01 至 2038-01-19 03:14:07 | YYYY-MM-DD HH:MM:SS | 

***

# DDL

```mysql
show databases; 	# 查询所有数据库
select database();	# 查询当前数据库

# 创建 (字符集默认 UTF8mb4)
create database [if not exists] 数据库名 [default charset 字符集] [collate 排序规则];
drop database [if exists] 数据库名	# 删除
use 数据库名;	# 进入数据库
show tables;	# 查询当前数据库所有表
desc 表名;	# 查询表结构
show create table 表名;	# 查询指定表的建表语句

# 创建表
create table 表名(
	字段1 类型 [comment '注释'],
	字段2 类型 [comment '注释'],
    ...
    字段n 类型 [comment '注释']
)[comment 表注释]
alter table 表名 add 字段名 类型(长度) [comment 注释] [约束]	# 添加字段

alter table 表名 modify 字段名 新数据类型(长度)	# 修改数据类型

# 修改字段名和字段类型
alter table 表名 change 旧字段名 新字段名 类型(长度) [comment 注释] [约束];	
alter table 表名 drop 字段名;	# 删除字段
alter table 表名 rename to 新表名;	# 修改表名
drop table [if exists] 表名;	# 删除表
truncate table 表名;	# 重置表数据
```

# DML

```mysql
# 给指定字段添加数据
INSERT INTO 表名 (字段名1, 字段名2, ...) VALUES (值1, 值2, ...);	

INSERT INTO 表名 VALUES (值1, 值2, ...);	# 依次给字段添加数据
INSERT INTO 表名 (字段名1, 字段名2, ...) VALUES (值1, 值2, ...), (值1, 值2, ...), (值1, 值2, ...);	# 批量添加数据

# 批量添加数据
INSERT INTO 表名 VALUES (值1, 值2, ...), (值1, 值2, ...), (值1, 值2, ...);	
UPDATE 表名 SET 字段名1 = 值1, 字段名2 = 值2, ... [ where 条件 ];	# 修改数据

DELETE FROM 表名 [ where 条件 ];	# 删除数据
```



# DQL

```mysql
SELECT
	字段列表
FROM
	表名字段
WHERE
	条件列表
GROUP BY
	分组字段列表
HAVING
	分组后的条件列表
ORDER BY
	排序字段列表
LIMIT
	分页参数
```

```mysql
SELECT 字段1, 字段2, 字段3, ... FROM 表名;	# 查询字段
SELECT 字段1 [ AS 别名1 ], 字段2 [ AS 别名2 ], 字段3 [ AS 别名3 ], ... FROM 表名;	# 设置别名
SELECT DISTINCT 字段列表 FROM 表名;	# 去除重复记录

# 转义，/ 之后的\_不作为通配符
SELECT * FROM 表名 WHERE name LIKE '/_张三' ESCAPE '/'	
SELECT 字段列表 FROM 表名 WHERE 条件 # 条件查询
SELECT 聚合函数(字段列表) FROM 表名;	# 使用聚合函数

# 分组查询
SELECT 字段列表 FROM 表名 [ WHERE 条件 ] GROUP BY 分组字段名 [ HAVING 分组后的过滤条件 ]; 

# 排序查询 默认 ASC升序， DESC降序
SELECT 字段列表 FROM 表名 ORDER BY 字段1 排序方式1, 字段2 排序方式2;

# 切片（索引从0开始）
SELECT 字段列表 FROM 表名 LIMIT 索引, 展示数量;
```

## 条件：

| 比较运算符          | 功能                                        |
| ------------------- | ------------------------------------------- |
| >                   | 大于                                        |
| >=                  | 大于等于                                    |
| <                   | 小于                                        |
| <=                  | 小于等于                                    |
| =                   | 等于                                        |
| <> 或 !=            | 不等于                                      |
| BETWEEN ... AND ... | 在某个范围内（含最小、最大值）              |
| IN(...)             | 在in之后的列表中的值，多选一                |
| LIKE 占位符         | 模糊匹配（\_匹配单个字符，%匹配任意个字符） |
| IS NULL             | 是NULL                                      |

| 逻辑运算符         | 功能                         |
| ------------------ | ---------------------------- |
| AND 或 &&          | 并且（多个条件同时成立）     |
| OR 或 &#124;&#124; | 或者（多个条件任意一个成立） |
| NOT 或 !           | 非，不是                     |

## 常见聚合函数：

| 函数  | 功能     |
| ----- | -------- |
| count | 统计数量 |
| max   | 最大值   |
| min   | 最小值   |
| avg   | 平均值   |
| sum   | 求和     |

# DCL

```mysql
# 查询用户
use mysql;
select * from user;
CREATE USER '用户名'@'主机名' IDENTIFIED BY '密码'; # 创建用户

# 修改用户密码
ALTER USER '用户名'@'主机名' IDENTIFIED WITH mysql_native_password BY '新密码';
DROP USER '用户名'@'主机名'; # 删除用户
SHOW GRANTS FOR '用户名'@'主机名'; # 查询权限
GRANT 权限列表 ON 数据库名.表名 TO '用户名'@'主机名'; # 撤销权限
REVOKE 权限列表 ON 数据库名.表名 FROM '用户名'@'主机名'; # 撤销权限
```

## 常用权限：

| 权限                | 说明               |
| ------------------- | ------------------ |
| ALL, ALL PRIVILEGES | 所有权限           |
| SELECT              | 查询数据           |
| INSERT              | 插入数据           |
| UPDATE              | 修改数据           |
| DELETE              | 删除数据           |
| ALTER               | 修改表             |
| DROP                | 删除数据库/表/视图 |
| CREATE              | 创建数据库/表      |

# 函数

## 字符串函数

| 函数                             | 功能                                                      |
| -------------------------------- | --------------------------------------------------------- |
| CONCAT(s1, s2, ..., sn)          | 字符串拼接，将s1, s2, ..., sn拼接成一个字符串             |
| LOWER(str)                       | 将字符串全部转为小写                                      |
| UPPER(str)                       | 将字符串全部转为大写                                      |
| LPAD(str, n, pad)                | 左填充，用字符串pad对str的左边进行填充，达到n个字符串长度 |
| RPAD(str, n, pad)                | 右填充，用字符串pad对str的右边进行填充，达到n个字符串长度 |
| TRIM(str)                        | 去掉字符串头部和尾部的空格                                |
| SUBSTRING(str, start, len)       | 返回从字符串str从start位置起的len个长度的字符串           |
| REPLACE(column, source, replace) | 替换字符串                                                |

## 数值函数

| 函数        | 功能                             |
| ----------- | -------------------------------- |
| CEIL(x)     | 向上取整                         |
| FLOOR(x)    | 向下取整                         |
| MOD(x, y)   | 返回x/y的模                      |
| RAND()      | 返回0~1内的随机数                |
| ROUND(x, y) | 求参数x的四舍五入值，保留y位小数 |

## 日期函数

| 函数                               | 功能                                              |
| ---------------------------------- | ------------------------------------------------- |
| CURDATE()                          | 返回当前日期                                      |
| CURTIME()                          | 返回当前时间                                      |
| NOW()                              | 返回当前日期和时间                                |
| YEAR(date)                         | 获取指定date的年份                                |
| MONTH(date)                        | 获取指定date的月份                                |
| DAY(date)                          | 获取指定date的日期                                |
| DATE_ADD(date, INTERVAL expr type) | 返回一个日期/时间值加上一个时间间隔expr后的时间值 |
| DATEDIFF(date1, date2)             | 返回起始时间date1和结束时间date2之间的天数        |

## 流程函数

| 函数                                                         | 功能                                                      |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| IF(value, t, f)                                              | 如果value为true，则返回t，否则返回f                       |
| IFNULL(value1, value2)                                       | 如果value1不为空，返回value1，否则返回value2              |
| CASE WHEN [ val1 ] THEN [ res1 ] ... ELSE [ default ] END    | 如果val1为true，返回res1，... 否则返回default默认值       |
| CASE [ expr ] WHEN [ val1 ] THEN [ res1 ] ... ELSE [ default ] END | 如果expr的值等于val1，返回res1，... 否则返回default默认值 |

# 约束

## 常用约束

| 约束条件 | 关键字         |
| -------- | -------------- |
| 主键     | PRIMARY KEY    |
| 自动增长 | AUTO_INCREMENT |
| 不为空   | NOT NULL       |
| 唯一     | UNIQUE         |
| 逻辑条件 | CHECK          |
| 默认值   | DEFAULT        |

## 外键约束

```mysql
CREATE TABLE 表名(
	字段名 字段类型,
	...
	[CONSTRAINT] [外键名称] FOREIGN KEY(外键字段名) REFERENCES 主表(主表列名)
);

# 添加外键
ALTER TABLE 表名 ADD CONSTRAINT 外键名称 FOREIGN KEY(外键字段名) REFERENCES 主表(主表列名);
ALTER TABLE 表名 DROP FOREIGN KEY 外键名;	# 删除外键

# 更改删除/更新行为
ALTER TABLE 表名 ADD CONSTRAINT 外键名称 FOREIGN KEY (外键字段) REFERENCES 主表名(主表字段名) ON UPDATE 行为 ON DELETE 行为;
```

### 删除/更新行为

| 行为        | 说明                                                   |
| ----------- | ------------------------------------------------------ |
| NO ACTION   | 父表有对应外键时，不允许删除/更新（与RESTRICT一致）    |
| RESTRICT    | 父表有对应外键时，不允许删除/更新（与NO ACTION一致）   |
| CASCADE     | 父表记录删改同步到子表                                 |
| SET NULL    | 父表中删除/更新对应记录时，子表修改为null              |
| SET DEFAULT | 父表有变更时，子表将外键设为一个默认值（Innodb不支持） |

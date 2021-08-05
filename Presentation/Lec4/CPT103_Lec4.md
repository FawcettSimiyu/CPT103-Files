# CPT103 lect 4

你好，这节课开始，我们将开始学习如何将数据插入到表中，更新数据，以及如何从表里面提取我想要的数据。

## Introduction to the MySQL `INSERT` statement

`INSERT` 命令是MySQL用来向表中插入数据的指令，这个命令可以允许你往一张表里面插入一行或者多行，下面两行解释了`INSERT`的基本语法

```mysql
INSERT INTO your_table_name(c1,c2,...)
	VALUES (v1,v2,...);
```

这上面这个语法里面

+ 首先，第一行开始，你需要说明你要插入的表的名字，后面跟着的括号里面，是用逗号隔开的属性名字
+ 之后，使用`VALUES` 表示后面那个括号里面的东西，是对应着上面那个括号的属性的值，同时也使用逗号隔开，也就是说，c1对应着v1, c2对应着v2，以此类推。

你插入的括号里的属性的数量，必须要跟values的那个括号里面的值的数量要相等，不然对不上啊，除此之外，这俩括号里的属性和值在位置上面，也是一一对应的，顺序不能乱。

如果你想插入多行，那么可以使用以下语法：

```mysql
INSERT INTO your_table_name(c1,c2,...)
VALUES 
   (v11,v12,...),
   (v21,v22,...),
    ...
   (vnn,vn2,...);
```

在这个语法里面，不同的行用逗号隔开就可以了。

### MySQL `INSERT` examples

空说无凭，我们现在通过一个例子来说明`INSERT`怎么用。

首先，来创建一个新的表，叫做`tasks`, 用下面这个语句：

```mysql
CREATE TABLE IF NOT EXISTS tasks (
    task_id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    start_date DATE,
    due_date DATE,
    priority TINYINT NOT NULL DEFAULT 3,
    description TEXT,
    PRIMARY KEY (task_id)
);
```

我们来简单看一下这个表，记录了不同的任务的开始日期，结束日期，标题等等，使用task_id作为主键，同时task_id还是自增的，不用管它，他也会一行一行加一。

#### MySQL `INSERT` – simple `INSERT` example

接下来，我们用`INSERT`命令来插入一行：

```mysql
INSERT INTO tasks(title,priority) VALUES('Learn MySQL INSERT Statement',1);
```

MySQL会返回给我一个值：

```shell
1 row(s) affected
```

这啥意思呢，这一行告诉我们有一行数据被成功插入进去了！

我们来使用select语句看一下效果怎么样：

```mysql
SELECT * FROM tasks;
```

我们的结果是这个样子的：

![image-20210806003757848](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806003757848.png)

在这个例子里面，我们插入的属性是title和priority这两个，对应的值分别是'Learn MySQL INSERT Statement'和1, 而其他的我们没有给到值的属性呢？他们都会被设置为默认值。

比如说task_id, 他在创建的时候就被设置为自动增长，所以它会从整数的默认值0增长1,变成1， 下一条数据哪怕不告诉mysql task_id的值，他也会在现在的基础上增加1,也就是2，我们可以拿刚刚的命令稍稍修改一下，看一下task_id会是什么：

```mysql
INSERT INTO tasks(title,priority) VALUES('Learn MySQL INSERT Statement test',2);
```

结果就会是这个样子的

![image-20210806003834075](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806003834075.png)

而start_date, due_date和description则使用NULL作为默认值，因此现在显示他们就是NULL

#### MySQL `INSERT` – Inserting dates into the table example

刚刚创建表的时候应该注意到了，里面的start_date和due_date都是Date类型的，那么这种数据类型应该怎么插入呢？

如果你要插入一个日期值，那么可以使用以下格式：

```
'YYYY-MM-DD'
```

在这个格式中：

+ `YYYY` 代表年，比如2018
+ `MM` 代表月，比如01
+ `DD`代表日，比如21

下面这条命令就利用了上面这个格式插入日期数据：

```mysql
INSERT INTO tasks(title, start_date, due_date) VALUES('Insert date into table','2018-01-09','2018-09-15');
```



#### MySQL `INSERT` – Inserting multiple rows example

接下来我们来看一下怎么插入多行数据，我们可以用这一条命令来演示：

```mysql
INSERT INTO tasks(title, priority)
VALUES
	('My first task', 1),
	('It is the second task',2),
	('This is the third task of the week',3);
```

之后mysql会返回给我们执行结果：

```shell
3 row(s) affected Records: 3  Duplicates: 0  Warnings: 0
```

这说明三行成功被插入到表格中去，并且没有重复的或者是警告信息。

## Introduction to MySQL `UPDATE` statement

在维护或者编写数据库相关应用的时候，更新任务几乎是最重要的任务之一，现在开始我们就来看看如何使用`UPDATE`来更新数据库里面的数据

`UPDATE`命令允许你改变某一行或者是多行的一个或者多个列的值，简单来说，他能修改一张表里面的所有数据，只要你告诉他要修改的数据在哪里，以及改成啥样。

下面就是update的语法：

```mysql
UPDATE table_name 
SET 
    column_name1 = expr1,
    column_name2 = expr2,
    ...
[WHERE
    condition];
```

在上面这段语法里面：

1. 首先，声明你想更新哪张表里的数据，写在`UPDATE`命令后面
2. 之后，在`SET`后面，跟上具体修改的方式，比如哪一个属性对应的值是什么，你可以使用逗号隔开多个修改
3. 最后，告诉MySQL那些行要应用这些修改，使用`WHERE`语句，但是`WHERE`语句是可选的，如果你不写这个语句的话，就会默认更新所有的行

`WHERE`在这里是非常重要的，因为很少有情况是你要更新所有的行，更多的是某一些满足特定条件的行需要更新而已。

### MySQL `UPDATE` examples

OK，在讲完了语法，现在让我们练习一下如何更新

首先我们看一下刚刚讲到的tasks表：

![image-20210806004041967](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806004041967.png)

我们现在想要修改一些数据，比如说，修改task_id为4的task的开始日期和结束日期

```mysql
UPDATE tasks 
SET 
    start_date = '2021-08-02',
    due_date = '2021-08-05'
WHERE
    task_id = 4;
```

修改之后我们可以看到，task_id为4的任务真的有了开始日期和结束日期

![image-20210806004331937](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806004331937.png)

## Introduction to MySQL `DELETE` statement

最后，我们来介绍怎么从表里面删除我不想要的行，这个操作跟前几个操作极其类似，我们先来看一下语法部分：

```mysql
DELETE FROM your_table_name
WHERE condition;
```

还是老样子，首先你要告诉mysql表的名字，然后最重要的，是`WHERE`，你要删除哪些行，是需要用`WHERE`从句来定义的，你也可以不加`WHERE`语句，后果会很严重，也就是把整张表所有的行都删除了，只留下一个空壳。

### Example

我们还是使用tasks这个表来当做例子，我们想要删除那些start_date是空的任务，那么语句应该像这样写：

```mysql
DELETE FROM tasks 
WHERE start_date is NULL;
```

我这里使用了`WHERE`从句，删除那些start_date为空的行，效果如下：

![image-20210806010228176](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806010228176.png)

## Introduction to MySQL SELECT statement

### Basic SELECT

SELECT语句是MySQL的查询语句，允许用户通过SELECT从一张表或者是多张表中获取数据，SELECT的用法多种多样，而他的最基本的语法很简单：

```mysql
SELECT select_list
FROM table_name;
```

在这个语法中：

+ 首先，需要select_list是1个或者多个列，可以说是定义了查询的范围，同时也是返回的结果的范围，如果是多个列的话，可以使用逗号隔开
+ 其次，你需要指明这些列是从哪个表来的

在执行顺序上，MySQL会首先执行FROM的从句，然后再执行SELECT的从句，也就是说，数据从哪里来至关重要。

#### Basic MySQL SELECT statement examples

首先我们使用`employees`这个表来作为例子，这张表的结构如下：

![image-20210806015649050](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806015649050.png)

这张表包含着8个属性，以下是这张表的一个部分行的截图：

![image-20210806015925903](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806015925903.png)

首先我们可以用select从中间选出所有的雇员的名字, 并规定只展示20行：

```mysql
SELECT lastName, firstName
FROM employees LIMIT 20;
```

得到了如下的结果：

![image-20210806020149501](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806020149501.png)

如果你想要得到整张表的话，应该怎么做呢？使用通配符`*`就可以了，比如：

```mysql
SELECT * FROM employees LIMIT 20;
```

我们就能拿到所有列了：

![image-20210806020343899](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806020343899.png)

### SELECT DISTINCT

顾名思义，SELECT DISTINCT的意思就是，我不仅要选出我想要的行，而且还想对他们进行去重操作，他的基本语法是在SELECT语法基础上进行了改动：

```mysql
SELECT DISTINCT
    select_list
FROM
    table_name
WHERE 
    search_condition
ORDER BY 
    sort_expression;
```

+ 首先声明select和distinct这两个关键字，并告诉mysql我们要哪几个属性/列在最终的结果里。
+ 之后告诉mysql目标的表是哪个
+ WHERE语句限定了选择的范围
+ ORDER BY则将最终的结果排序

因此，这四个从句的执行顺序将会是：

1. FROM
2. WHERE
3. SELECT
4. DISTINCT
5. ORDER BY

#### SELECT DISTINCT examples

我们还是拿employees当作例子：

![image-20210806021122559](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806021122559.png)

首先我们来测试一些如果不加DISTINCT的话，从表中挑选last_name, 并将结果排序：

```mysql
SELECT 
    lastname
FROM
    employees
ORDER BY 
    lastname;
```

我们可以得到很多last_name, 其中很多都重复了：

![image-20210806022620416](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806022620416.png)

那当我们加上了去重DISTINCT:

```mysql
SELECT 
    DISTINCT lastname
FROM
    employees
ORDER BY 
    lastname;
```

结果就删去了重复：

![image-20210806022758045](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806022758045.png)

### SELECT and WHERE

之前我们在其他部分的时候零零散散地提到了`WHERE`语句，相对于其他部分，SELECT与WHERE语句的结合更为紧密，因为我们需要WHERE作为筛选器，精确的拿到我们想要的数据。

从基本语法上，大家都很熟悉了：

```mysql
SELECT 
    select_list
FROM
    table_name
WHERE
    search_condition;
```

语法的最后，添上了WHERE从句，需要注意的是，这三条从句，也就是SELECT, FROM, WHERE的执行顺序是：

1. FROM
2. WHERE
3. SELECT

而WHERE里的那个search_condition，则是一个布尔表达式，只会返回TRUE, FALSE或者是UNKNOWN, 你需要使用类似于以下表达式的方式来写search_condition:

```mysql
(a > 1) AND (B <= 5);
(a = 4) OR (c = 3);
NOT((a = 4) OR (c = 3));
```

也就是说，你需要使用AND, OR, NOT去组合不同的逻辑表达式，来完成筛选工作。

####  WHERE clause with equality operator example

我们依然是用employees作为例子，现在我们想要找到jobtitle是'Sales Rep'的员工的lastname, firstname以及jobtitle:

```mysql
SELECT 
    lastname, 
    firstname, 
    jobtitle
FROM
    employees
WHERE
    jobtitle = 'Sales Rep';
```

这样我们得到了想要的结果：

![image-20210806023818914](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806023818914.png)

#### WHERE clause with the AND operator

我想知道一种员工的firstname, lastname, jobtitle, officecode，

+ 这种员工首先jobtitle是Sailes rep

+ 其次officecode是1

  

  那么我们可以使用AND:

```mysql
SELECT 
    lastname, 
    firstname, 
    jobtitle,
    officeCode
FROM
    employees
WHERE
    jobtitle = 'Sales Rep' AND officeCode = 1;
```

成功拿到想要的信息：

![image-20210806024117414](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806024117414.png)

#### WHERE clause with OR operator

我想知道一种员工的firstname, lastname, jobtitle, officecode，这个员工只要满足以下条件其中一个即可：

+ jobtitle是Sailes rep
+ officecode是1

这里就可以使用OR:

```mysql
SELECT 
    lastName, 
    firstName, 
    jobTitle, 
    officeCode
FROM
    employees
WHERE
    jobtitle = 'Sales Rep' OR 
    officeCode = 1
ORDER BY 
    officeCode , 
    jobTitle;
```

满足这个条件的员工还是挺多的：

![image-20210806024555165](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806024555165.png)

#### WHERE clause with the BETWEEN operator example

我想知道一种员工的firstname, lastname, jobtitle, officecode，这种员工只有一个条件：

+ officecode在1和3之间

这里就可以使用`BETWEEN`：

```shell
expression BETWEEN low AND high
```

完整的MySQL表达式是：

```mysql
SELECT 
    firstName, 
    lastName, 
    officeCode
FROM
    employees
WHERE
    officeCode BETWEEN 1 AND 3
ORDER BY officeCode;
```

最终结果如我们所愿：

![image-20210806024838566](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806024838566.png)

#### WHERE clause with the LIKE operator example

`LIKE`是一种模式匹配操作，就如同字面意思，如果能满足一定的模式，就返回True

使用`LIKE`你可以使用`%`和`_`， 百分号代表着任意长度的字符，比如说以下三个例子：

1. Jackson
2. Thompson
3. Patterson

都满足这个表达式：`%son`, 也就是以`son`结尾，我们可以用一个实际的例子来说明。

我现在想知道那些lastname结尾是son的姓名：

```mysql
SELECT 
    firstName, 
    lastName
FROM
    employees
WHERE
    lastName LIKE '%son'
ORDER BY firstName;
```

然后真的得到了这些名字：

![image-20210806025348128](/home/xunjie/snap/typora/39/.config/Typora/typora-user-images/image-20210806025348128.png)



4. Select and cartesian product
5. SELECT from Multiple Tables
6. Aliases
7. Self-Joins
8. Subqueries
9. IN, NOT IN, EXISTS, ANY, ALL

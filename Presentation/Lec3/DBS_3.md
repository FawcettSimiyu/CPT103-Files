# DBS 3

```sql
CREATE DATABASE dream_home;
USE dream_home;

CREATE TABLE Staff (
    id INT NOT NULL,
    staffNo VARCHAR(5), 
    Name VARCHAR(15), 
    salary DECIMAL(7,2),
	PRIMARY KEY (ID)
);
    
INSERT INTO Staff VALUES('SG16', 'Brown', 8300);

CREATE TABLE Persons (
    Personid INT NOT NULL AUTO_INCREMENT,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255),
    Age INT,
    PRIMARY KEY (Personid)
); 

CREATE TABLE Orders (
    OrderID INT NOT NULL,
    OrderNumber INT NOT NULL,
    PersonID INT,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) 
    	REFERENCES Persons(PersonID)
    	ON DELETE SET NULL
        ON UPDATE CASCADE
); 
```

|   DATA TYPE   |            FROM            |            TO             | Comment                |
| :-----------: | :------------------------: | :-----------------------: | ---------------------- |
|    BIGINT     | -9,223,372,036,854,775,808 | 9,223,372,036,854,775,807 | 超大的整数             |
|      INT      |       -2,147,483,648       |       2,147,483,647       | 整数                   |
|    TINYINT    |             0              |            255            | 非常小的整数           |
|  FLOAT(M, D)  |        M: 可显示M位        |     D: 小数点后面D位      | 浮点数                 |
| DOUBLE(M, D)  |                            |                           | 比FLOAT精度更高        |
| DECIMAL(M, D) |                            |                           | 每一个数字代表一个字节 |

```mysql
ALTER TABLE contacts ADD last_name varchar(40) NOT NULL, ADD first_name varchar(35) NULL;

ALTER TABLE contacts DROP COLUMN contact_type;

ALTER TABLE table_name
  CHANGE COLUMN old_name new_name 
    column_definition;
    
ALTER TABLE contacts
  CHANGE COLUMN contact_type ctype
    varchar(20) NOT NULL;

ALTER TABLE table_name
  MODIFY column_name column_definition;
  
ALTER TABLE contacts
  MODIFY last_name varchar(50) NULL;
  
ALTER TABLE table_name
	ADD CONSTRAINT constraint_name UNIQUE (column1, column2, ... column_n);
    
ALTER TABLE contacts 
    ADD CONSTRAINT contacts_unique UNIQUE (last_name, first_name);
    
ALTER TABLE your_table_name 
    DROP INDEX constraint_name | DROP FOREIGN KEY name | DROP PRIMARY KEY
    
ALTER TABLE contacts
	DROP INDEX contacts_unique;
```




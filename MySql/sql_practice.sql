use nit;
describe customers;
insert into customers(ID,Name,Age,salary) values(1,'Ramesh',23,2000);
select * from customers;
alter table customers add Address varchar(100);
describe customers;
update customers set Address='Ahmedabad' where id=1;
select*from customers;
insert into customers values(3,'Kaushik',23,2000,'kota'),(4,'Chaitali',25,6500,'Mumbai'),(5,'Hardik',27,8500,'Bhopal')
,(6,'Komal',22,4500,'MP'),(7,'Muffy',24,10000,'Indore');
select*from customers;

-- SQL Comparision Operators 

select * from customers where salary>5000;
select*from customers where salary=2000;
select*from customers where salary!=2000;
select*from customers where salary<>2000; -- <> means not equal to in sql

select*from customers where salary>=6500;

select*from customers;



--  SQL Logical Operations

select*from customers where age>=25 and salary>=6500; -- and operator 
select*from customers where age>=25 or salary>=6500;-- or operator
select*from customers where age is not null;-- not operator
select*from customers where name like 'Ko%';-- like operator and 'str%'->find the mention char at start
select*from customers where age in(25,27);-- in operator -> find the value b/w given condition

-- exists operator -> search for rows which meets certain criteria
select age from customers where exists(select age from customers where salary>6500);

-- all operator->all record from condition 
select *from customers where age<all(select age from customers where salary>6500); 

-- any operator
select*from customers where age>any(select age from customers where salary>6500);



use nit;
-- SQL EXPRESSIONS

select * from customers where salary=10000;-- boolean expression
select (age+age) as addition from customers where age=23; -- numerical expression
-- some built in methods are sum(),avg(),count()...

select count(*) as 'records' from customers;



-- SQL - DATE EXPRESSIONS
select current_timestamp(); -- timestamp
select current_date();
select current_time();
select getdate();-- this is not working




-- SQL create DATABASES
-- syntax create database DatabaseName;

create database testdb;
show databases;-- display all existing databases in system


-- Drop or DELETE Databases
drop database testdb;
show databases;-- testdb is deleted


-- SQL Select Database
-- syntax use databasname  
-- always the database name is unque in rdbms

show databases;



-- SQL create table
/*CREATE TABLE table_name( 
column1 datatype, 
column2 datatype, 
column3 datatype, 
..... 
columnN datatype, 
PRIMARY KEY( one or more columns ) 
);*/


-- create table using another table
/*CREATE TABLE NEW_TABLE_NAME AS 
   SELECT [ column1, column2...columnN ] 
   FROM EXISTING_TABLE_NAME 
   [ WHERE ] */
   
   create table salary as select id,salary from customers;
   select*from salary;
   
   describe salary; -- describe gives the information about tables attribute
   desc customers; -- short form of describe
   
   
   
   -- SQL Drop or Delete table
   -- DROP TABLE table_name; 
   
   drop table salary;
   desc salary;
   show tables;-- salary is deleted from database
   
   
 -- SQL INSERT  Query
 /*INSERT INTO TABLE_NAME (column1, column2, column3,...columnN)]   
VALUES (value1, value2, value3,...valueN);  secure way

NSERT INTO TABLE_NAME VALUES (value1,value2,value3,...valueN); common way
   
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (1, 'Ramesh', 32, 'Ahmedabad', 2000.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (2, 'Khilan', 25, 'Delhi', 1500.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (3, 'kaushik', 23, 'Kota', 2000.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (4, 'Chaitali', 25, 'Mumbai', 6500.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (5, 'Hardik', 27, 'Bhopal', 8500.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (6, 'Komal', 22, 'MP', 4500.00 ); */



-- SQL Select Query
-- syntax
/*SELECT column1, column2, columnN FROM table_name; for specific columns
SELECT * FROM table_name; for all records*/

select id,name,salary from customers;
select*from customers;



-- SQL Where Clause
-- it use with select ,delete,update etc
/* synatax->
SELECT column1, column2, columnN  
FROM table_name 
WHERE [condition] */;

select id,name,salary from customers where salary>20;
select*from customers where name='hardik';



-- SQL AND/OR Operator
/*syntax->
SELECT column1, column2, columnN  
FROM table_name 
WHERE [condition1] AND/OR [condition2]...AND/OR [conditionN]; */

select* from customers where salary>2000 and age<25;
select*from customers where salary>2000 or age<25;



-- SQL update Query
/* syntax->
UPDATE table_name 
SET column1 = value1, column2 = value2...., columnN = valueN 
WHERE [condition]; */

update customers set address='Pune' where id=6;-- on specific location
update customers set address='Pune' ,salary=1000;-- update the all record of table



-- SQL Delete Query
/* syntax->
DELETE FROM table_name 
WHERE [condition]; */

delete from customers where id=6;-- delete the specific record
delete from customers ;-- delete all table records



-- SQL JOINS
/* combine two or more table records*/
use nit;
select*from customers;
create table orders(oid int not null primary key,
DATE datetime ,customer_id int,Amount int);
desc orders;
insert into  orders values(102,'2009-10-08 00:00:00',3,3000);
insert into orders values(100,'2009-10-08 00:00:00',3,1500),(101,'2009-11-28 00:00:00',3,1500),(103,'2008-05-08 00:00:00',3,1500);
select*from orders;

update orders set customer_id=2 where oid=101;
update orders set customer_id=4 where oid=103;


-- join
select id,name,age ,amount from customers,orders where customers.id=orders.customer_id;


-- INNER JOIN
/*INNER JOIN: returns rows when there is a match in both tables.
like intersection */

show tables;
select id,name,amount,date from customers inner join orders on customers.id=orders.customer_id;


-- Left join
/*The SQL LEFT JOIN returns all rows from the left table, even if there are no matches in the right table.*/

select*from customers left join orders on customers.id=orders.customer_id;
select*from orders left join customers on orders.customer_id=customers.id;



-- Right Join
/*The SQL RIGHT JOIN returns all rows from the right table, even if there are no matches in the left table.*/
select*from customers right join orders on customers.id=orders.customer_id;
select*from orders right join customers on orders.customer_id=customers.id;


-- Full Join
/*The SQL FULL JOIN combines the results of both left and right outer joins.
MySQL (because MySQL does not support FULL JOIN)
*/;
select*from customers full join orders on customers.id=orders.customer_id;

SELECT  ID, NAME, AMOUNT, DATE 
     FROM CUSTOMERS 
     LEFT JOIN ORDERS 
     ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID 
UNION ALL 
     SELECT  ID, NAME, AMOUNT, DATE 
     FROM CUSTOMERS 
     RIGHT JOIN ORDERS 
     ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID
     
     
     
     
     
-- SELF JOIN
/*The SQL SELF JOIN is used to join a table to itself as if the table were two tables, temporarily renaming at least 
one table in the SQL statement*/;

select a.id,b.name,a.salary from customers a,customers b where a.salary<b.salary;


-- CARTESIAN JOIN
/*The CARTESIAN JOIN or CROSS JOIN returns the cartesian product of the sets of records from the two or more 
joined tables.*/
USE NIT;
select ID,NAME,AMOUNT,DATE FROM CUSTOMERS,ORDERS;-- THE SAME COLUMNS  PRESENTS IN BOTH TABLE



-- SQL UNION CLAUSE
/*The SQL UNION clause/operator is used to combine the results of two or more SELECT statements 
without returning any duplicate rows. */

select ID,NAME,AMOUNT,DATE FROM CUSTOMERS LEFT JOIN ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID
union 
select ID,NAME,AMOUNT,DATE FROM CUSTOMERS RIGHT JOIN ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID;


-- UNION ALL CLAUSE
/*The UNION ALL operator is used to combine the results of two SELECT statements including duplicate rows. */

select ID,NAME,AMOUNT,DATE FROM CUSTOMERS left join ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID
UNION ALL 
select ID,NAME,AMOUNT,DATE FROM CUSTOMERS RIGHT JOIN ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID;

-- INTERSECT CLAUSE
/*The SQL INTERSECT clause/operator is used to combine two SELECT statements, but returns rows only from the 
first SELECT statement that are identical to a row in the second SELECT statement. This means INTERSECT 
returns only common rows returned by the two SELECT statements.

--  MYSQL DOES NOT SUPPORT INTERSECT IT HAS INNER JOIN*/;

use nit;
select ID,NAME,AMOUNT,DATE FROM CUSTOMERS LEFT JOIN ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID

INTERSECT 
SELECT ID,NAME,AMOUNT,DATE FROM CUSTOMERS RIGHT JOIN ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID;



-- EXCEPT CLAUSE
/*The SQL EXCEPT clause/operator is used to combine two SELECT statements and returns rows from the first 
SELECT statement that are not returned by the second SELECT statement. This means EXCEPT returns only 
rows, which are not available in second SELECT statement. 

-- MYSQL NOT SUPPORT EXCEPT*/
use nit;
select ID,NAME,AMOUNT,DATE FROM CUSTOMERS LEFT JOIN ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID
EXCEPT
SELECT ID,NAME,AMOUNT,DATE FROM CUSTOMERS RIGHT JOIN ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID;

SELECT ID,NAME,AMOUNT,DATE FROM CUSTOMERS RIGHT JOIN ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID
except
select ID,NAME,AMOUNT,DATE FROM CUSTOMERS LEFT JOIN ORDERS ON CUSTOMERS.ID=ORDERS.CUSTOMER_ID
-- SQL NULL VALUES
/*The SQL NULL is the term used to represent a missing value. A NULL value in a table is a value in a field 
that appears to be blank.
A field with a NULL value is a field with no value. It is very important to understand that a NULL value is different 
than a zero value or a field that contains spaces. */

-- IS NOT NULL OPERATOR
select ID,NAME,AGE,ADDRESS,SALARY FROM CUSTOMERS WHERE SALARY IS NOT NULL;
insert INTO ORDERS(OID,CUSTOMER_ID) valueS(105,3),(106,4);

-- IS NULL 
select * FROM ORDERS WHERE AMOUNT IS NULL;



-- SQL ALIAS SYNTAX
/*You can rename a table or a column temporarily by giving another name known as alias.*/

-- TABLE ALIAS
SELECT C.ID,C.NAME,C.AGE,O.AMOUNT FROM CUSTOMERS AS C, ORDERS AS O WHERE C.ID=O.CUSTOMER_ID;

-- COLUMN ALIAS
select ID AS CUSTOMER_ID,NAME AS CUSTOMER_NAME FROM CUSTOMERS WHERE SALARY IS NOT NULL;

use nit;



-- SQL INDEXES
/*I ndexes are special lookup tables that the database search engine can use to speed up data retrieval.*/

select*from CUSTOMERS;

DROP index INDEX_1;
create index INDEX_1 ON CUSTOMERS (ID);

create index INDEX_2 ON CUSTOMERS(ID,NAME);



-- SQL ALTER table COMMANDS
/*The SQL ALTER TABLE command is used to add, delete or modify columns in an existing table.*/
select*FROM ORDERS;



-- alter table
-- ADD FIELDS
alter table ORDERS ADD PRODUCTS varchar(50);

-- DROP FIELDS
alter table ORDERS DROP PRODUCTS ;

-- change DATA TYPE
alter table ORDERS modify CUSTOMER_ID INT;
desc ORDERS;



-- NOT NULL
alter table ORDERS MODIFY OID INT not NULL; 

-- ADD UNIQUE CONSTRANT
alter table ORDERS add constraint MYUNIQUECONSTRAINT unique(OID);

-- ADD CHECK CONSTRAINT
alter TABLE ORDERS ADD constraint MYUNIQUECONSTRAINT1 CHECK(AMOUNT>500) ;-- ITS SHOWS ERROR 3819 IF CONDITION IS NOT SATIFY

-- ADD PRIMARY KEY
alter table ORDERS ADD constraint MYPRIMARYKEY primary key (CUSTOMER_ID);-- ERROR 1068 FOR MULTIPLE PRIAMRY KEY

alter table CUSTOMERS ADD SEX CHAR(1);
SELECT*FROM CUSTOMERS;

update CUSTOMERS SET  SEX='M' WHERE ID=1;
alter TABLE CUSTOMERS DROP SEX;



-- SQL truncate table
/*The SQL TRUNCATE TABLE command is used to delete complete data from an existing table.
SYNTAX:
truncate table table_NAME*/


-- SQL USING VIEW
/* A 
view is actually a composition of a table in the form of a predefined SQL query.
SYNTAX:
CREATE VIEW view_name AS 
SELECT column1, column2..... 
FROM table_name 
WHERE [condition];

- VIEW JUST A EXTRACTING HUGE DATA INTO SMALLER PART TO SEE AND WE CAN APPLY SOME FUNCTION LIKE update,INSERT,DELETE */

create VIEW CUST AS SELECT NAME,AGE FROM CUSTOMERS;
SELECT*FROM CUST;


-- UPDATE VIEW
SET SQL_SAFE_UPDATES = 0;-- I AM USING SQL SAFE UPDATE VERSION THATS WHY I NEED TO CHANGE
update CUST VIEW set AGE=35 WHERE NAME='RAMESH';
SET SQL_SAFE_UPDATES = 1;
 
 -- DELETE THE RECORDS
delete from CUST VIEW WHERE AGE=22;

-- DELETE THE VIEW
drop VIEW CUST;
SELECT * FROM CUST;-- SQL SHOWS 1146 ERROR IF DATA IS NOT EXISTS



-- SQL WILDCARD OPERATIONS
/*We already have discussed SQL LIKE operator, which is used to compare a value to similar values 
using wildcard operators.
TWO WILDCARD EXISTS
1.(%)-> Matches one or more characters. 
2.(_)->Matches one character. 
Syntax: 
The basic syntax of ‘%’ and ‘_’ is as follows: 
SELECT FROM table_name 
WHERE column LIKE 'XXXX%' 
 
or  
 
SELECT FROM table_name 
WHERE column LIKE '%XXXX%' 
 
or 
 
SELECT FROM table_name 
WHERE column LIKE 'XXXX_' 
 
or 
 
SELECT FROM table_name 
WHERE column LIKE '_XXXX' 
 */

select*FROM CUSTOMERS WHERE SALARY LIKE '200%';-- CHECKS THE STARTING THREE VALUES IF MATCH THEN RETURN THE values
select*FROM CUSTOMERS WHERE NAME LIKE '_a%';
select*from customers where name like'%i_';
select*from customers where salary like '_0%';



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



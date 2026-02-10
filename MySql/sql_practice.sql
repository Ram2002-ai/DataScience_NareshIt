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
show databases;
create database nit;
use nit;
create table student(name varchar(30),id int not null primary key,address varchar(50),mark int);
describe student;
insert into student (mark,id,name,address) values(78,12,'Ram','Balaghat'); -- secure way to insert
insert into student values('Ram',40,'hydrabad',23);-- common way to insert recod
select*from student;
insert into student values('alex',23,'usa',53),('john',21,'India',13),('arun',24,'bangluru',43),('sonu',26,'Mp',33);
select name from student;
select name,id from student;
select * from student where id=12;
insert into student values('sam',12,'hdy',45); -- duplicte entry on primary key
update student set address='chennai' where id=23;
-- update the table
alter table student add phoneNo int;
select * from student;
update student set phoneNo=93021 where id=12;
-- delete the column
alter table student drop phoneNo; 
select*from student;
delete from student where name='ram';

-- function
select sum(mark) from student;
select avg(mark) from student;
select max(mark) from student;
select min(mark) from student;
-- order by
select * from student order by mark; -- asc by default
select*from student order by mark desc; -- desc change manually
-- 44,45,46.....69

use nit;

select*from student;

-- wildcard operators 
/* two wild operator
(%)
(_)
must start with like*/

select*from student where name like 'a%'; -- start with
select*from student where name like 'y%';
-- second char is a
select*from student where name like '_a%';
select*from student where name like '%s_';

-- 128 page ,129,

-- Joins
/*joins always work with two tables
- left join (left outer  join)


*/

create table emp(id int not null primary key,salary int,empcode int,name varchar(30));

insert into emp values(12,20000,102,'aman'),(23,60000,104,'arup'),(78,36000,165,'max'),(80,25000,103,'ram'),(34,90000,106,'sam');
select*from emp;
select*from student;

--  inner join
select*from student inner join emp on student.id=emp.id;
-- left join
select*from student left join emp on student.id=emp.id;-- left table all record return

select*from emp left join student on emp.id=student.id;

-- right join
select*from student right join emp on student.id=emp.id;
select*from emp right join student on emp.id=student.id;

-- cross join
select * from student cross join emp;
-- 91-120,128-129



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


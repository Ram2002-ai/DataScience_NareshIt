create table emp(empid not null int primary key,name varchar(30));
SELECT weather,temperature from dataset_1;
select*from dataset_1 limit 10;
select DISTINCT (passanger)from dataset_1 d ;
SELECT *FROM dataset_1 ;

-- where clause
SELECT *from dataset_1 d where d.destination ='Home';

-- order by
select *from dataset_1 d ORDER BY coupon;

-- Aliasing
select destination as 'Destination' from dataset_1 d ;

-- comments
SELECT * -- This is a comment FROM dataset_1;

-- AVG
SELECT AVG(age)from dataset_1 d ;




-- Aggregation
-- GROUP BY
SELECT occupation FROM  dataset_1 d group by d.occupation ;

-- AVG
SELECT weather, AVG(temperature) as 'avg_temp' from dataset_1 d group by weather;


-- Count
select weather,COUNT(temperature) as 'count_temp' FROM  dataset_1 d group by d.weather ;


-- COUNT (DISTINCT)
SELECT WEATHER ,COUNT(DISTINCT TEMPERATURE) AS 'COUNT_DISTINCT_TEMP' FROM DATASET_1 GROUP BY WEATHER;



-- SUM
SELECT WEATHER,SUM(TEMPERATURE) AS 'SUM_TEMP' FROM dataset_1 d GROUP BY d.weather;


-- MIN
SELECT  WEATHER,MIN(TEMPERATURE) AS 'MIN_TEMP' FROM DATASET_1 GROUP BY weather ;


-- MAX
SELECT WEATHER, MAX(TEMPERATURE) AS 'MAX_TEMP' FROM dataset_1 d  GROUP BY d.weather ;

-- HAVING
SELECT  occupation from dataset_1 d  group by d.occupation  HAVING d.occupation ='Student';

-- JOIN(LEFT,INNER,OUTER,RIGHT)
SELECT *FROM table_to_join ttj ;
SELECT a.destination,a.time,b.part_of_day from dataset_1 a join table_to_join b on a.time=b.time ;

-- left join
SELECT a.destination ,a.time,b.part_of_day from dataset_1 a left join table_to_join b on a.time=b.time ;



-- ADVANCED QUERYING
-- SUBQUERYING

SELECT DESTINATION,PASSANGER FROM (SELECT*FROM dataset_1 d  WHERE d.passanger ='Alone');


-- ADVANCED FILTERING
-- LIKE
SELECT *FROM dataset_1 d WHERE D.weather LIKE 'S%';


-- BETWEEN
SELECT DISTINCT TEMPERATURE FROM dataset_1 d WHERE d.temperature BETWEEN 29 AND 75;


-- IN
SELECT OCCUPATION FROM dataset_1 d WHERE d.occupation IN('Sales & Related','Management');

SELECT *from table_to_join ttj ;
SELECT *from 
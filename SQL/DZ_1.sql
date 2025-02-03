--1) Вывести самый дешевый велосипед в каждой категории каждого бренда
select *
from production.products pp
where list_price < 500
order by list_price desc


--2) Вывести среднюю цену каждого велосипеда с названием бренда Например:  Trek 2999, Cross 1459 и т.п. 
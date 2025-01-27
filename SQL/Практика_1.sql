use BikeStoresOld

--1) вывести все велосипеды 2017 года
select *
from production.products pp
where model_year = 2017

--2) вывести названия и год выпуска велосипедов под брендом 5
select product_name, model_year
from production.products pp
where brand_id = 5

--3) вывести все велосипеды дешевле 500
select *
from production.products pp
where list_price < 500
order by list_price desc

--4) вывести названия и цены велосипедов дороже тысячи и дешевле полутора тысяч
select product_name, list_price
from production.products pp
where list_price between 1000 and 1500
order by list_price desc

--5) вывести название id и цену самого дорогого велосипеда дешевле 3 тысяч
select top 1 product_id, list_price
from production.products pp
where list_price < 3000
order by list_price desc


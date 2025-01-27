select pp.brand_id as 'Номер бренда'
from production.products pp

select top 10 *
from production.products
where category_id = 7
order by list_price desc, model_year desc
--desc - descending - порядок на убывание

--1) вывести все велосипеды 2017 года

select *
from production.products as pp
where pp.model_year = 2017

--2) вывести названия и год выпуска велосипедов под брендом 5

select pp.product_name, pp.model_year
from production.products as pp
where pp.brand_id = 5

--3) вывести все велосипеды дешевле 500

select *
from production.products
where list_price < 500

--4) вывести названия и цены велосипедов дороже тысячи и дешевле полутора тысяч

select product_name, list_price
from production.products
where list_price > 1000 and list_price < 1500

select product_name, list_price
from production.products
where list_price between 1000 and 1500

--5) вывести название id и цену самого дорогого велосипеда дешевле 3 тысяч

select top 1 product_id, product_name, list_price
from production.products
where list_price < 3000
order by list_price desc

--6) разобраться с between,
--7) вывести все велосипеды с категориями 2, 6 и 7


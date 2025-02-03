-- Находим самый дорогой велосипед из первой категории
select top 1 *
from production.products
where category_id = 1
order by list_price desc

-- добавляем столбец, в котором вычисляем цену велосипеда в руб (1 = 100)
select *, list_price * 100 as list_priceRub
from production.products

-- добавляем столбец, где вычисляем, сколько реально заплатили за каждую позицию в чеке
select *, realprice = list_price * (1 - discount) * quantity
from sales.order_items
where order_id = 500

-- Находим среднюю цену среди всех велосипедов
select avg(list_price) as avgPrice
from production.products

-- находим самую высокую цену на велосипед в каждой категории
select category_id, max(list_price)
from production.products
group by category_id

-- находим самую высокую цену на велосипед у каждого бренда
select brand_id, max(list_price)
from production.products
group by brand_id

-- ищем самую высокую цену на велосипед в каждой категории у каждого бренда
select brand_id, category_id, max(list_price)
from production.products
group by brand_id, category_id
order by brand_id

-- найти самую высокую цену велосипеда дешевле 3 тысяч по каждой категории
select category_id, max(list_price) as maxPrice
from production.products
where list_price < 3000
group by category_id
order by maxPrice desc

-- найти среднюю цену велосипедов в каждой категории
select category_id, avg(list_price) as avgPrice
from production.products
group by category_id

-- найти среднюю цену велосипедов дешевле 3к в каждой категории
select category_id, avg(list_price) as avgPrice
from production.products
where list_price < 3000
group by category_id

-- найти среднюю цену велосипедов в каждой категории, которая меньше 3к
select category_id, avg(list_price) as avgPrice
from production.products
group by category_id
having avg(list_price) < 3000

-- найти среднюю цену вообще
select avg(list_price * (1-discount) * quantity) as avgSumm
from sales.order_items

-- найти среднюю цену каждого заказа
select order_id, avg(list_price * (1-discount) * quantity) as maxRealPrice
from sales.order_items
group by order_id

-- найти среднюю цену каждого заказа, показать те, где она меньше 200
select order_id, avg(list_price * (1-discount) * quantity) as maxRealPrice
from sales.order_items
group by order_id
having avg(list_price * (1-discount) * quantity) < 200

select order_id--, avg(list_price * (1-discount) * quantity) as maxRealPrice
from sales.order_items
group by order_id
having max(list_price * (1-discount) * quantity) < 1000
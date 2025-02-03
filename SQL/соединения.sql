-- соединение таблиц обычное, с помощью join
select p.product_name, b.brand_name, c.category_name, p.model_year, p.list_price
from production.products as p
join production.brands as b on p.brand_id = b.brand_id
join production.categories as c on p.category_id = c.category_id

-- соединение таблиц при помощи декартова произведения и фильтра
select *
from production.products as p
, production.categories as c
where p.category_id = c.category_id

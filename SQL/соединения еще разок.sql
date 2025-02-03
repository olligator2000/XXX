-- декартово произведение. каждая строка из одной таблицы соединяется с каждой строкой из другой
select *
from production.brands, production.categories

-- обычное соединение. соединяем таблицы на каких-то основаниях (условиях, чаще всего - по внешнему ключу)
select *
from production.products as p
join production.brands as b on p.brand_id = b.brand_id

-- обычное соединение, но берет все строки из левой (или правой при right) таблицы, даже если их не с чем соединить
select *-- s.staff_id, s.first_name, s.last_name, s.phone, m.first_name + ' ' + m.last_name as manager
from sales.staffs s left join sales.staffs m on s.manager_id = m.staff_id

-- объединение - берем результаты одного запроса и присоединяем к ним вертикально результаты другого, 
-- главное чтобы совпадали порядок и типы данных столбцов
select *
from production.categories
union
select *
from production.brands

select *
from production.products pp
join sales.order_items oi on pp.product_id = oi.product_id

select *
from production.products p
left join production.stocks s  on s.product_id = p.product_id
right join production.brands b on p.brand_id = b.brand_id
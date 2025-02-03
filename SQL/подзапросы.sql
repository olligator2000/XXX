-- получаем номера и суммы заказов
select order_id, sum(list_price * (1 - discount) * quantity) as summ
from sales.order_items
group by order_id

-- информация о заказах, покупателях, магазинах и суммы заказов
-- получаем с помощью подзапроса. Сначала выполняется он, потом с его результатами соединяем остальные данные
select o.order_id, o.order_date, c.first_name + ' ' + c.last_name as customer, s.store_name, s.phone, orderSumms.summ
from sales.orders o
join sales.customers c on o.customer_id = c.customer_id
join sales.stores s on o.store_id = s.store_id
join (
	select order_id, sum(list_price * (1 - discount) * quantity) as summ
	from sales.order_items
	group by order_id
) as orderSumms on o.order_id = orderSumms.order_id
order by customer desc

-- инфа о покупателях, кто покупал 3 самых дорогих велосипеда
-- подзапрос в фильтре. сперва находим 3 номера трех велосипедов, потом по ним фильтруем остальные данные
select distinct c.*
from sales.customers c
join sales.orders o on c.customer_id = o.customer_id
join sales.order_items oi on o.order_id = oi.order_id
where oi.product_id in (
	select top 3 product_id
	from production.products
	order by list_price desc
)
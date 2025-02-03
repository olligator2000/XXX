-- ������� ����� ������� ��������� �� ������ ���������
select top 1 *
from production.products
where category_id = 1
order by list_price desc

-- ��������� �������, � ������� ��������� ���� ���������� � ��� (1 = 100)
select *, list_price * 100 as list_priceRub
from production.products

-- ��������� �������, ��� ���������, ������� ������� ��������� �� ������ ������� � ����
select *, realprice = list_price * (1 - discount) * quantity
from sales.order_items
where order_id = 500

-- ������� ������� ���� ����� ���� �����������
select avg(list_price) as avgPrice
from production.products

-- ������� ����� ������� ���� �� ��������� � ������ ���������
select category_id, max(list_price)
from production.products
group by category_id

-- ������� ����� ������� ���� �� ��������� � ������� ������
select brand_id, max(list_price)
from production.products
group by brand_id

-- ���� ����� ������� ���� �� ��������� � ������ ��������� � ������� ������
select brand_id, category_id, max(list_price)
from production.products
group by brand_id, category_id
order by brand_id

-- ����� ����� ������� ���� ���������� ������� 3 ����� �� ������ ���������
select category_id, max(list_price) as maxPrice
from production.products
where list_price < 3000
group by category_id
order by maxPrice desc

-- ����� ������� ���� ����������� � ������ ���������
select category_id, avg(list_price) as avgPrice
from production.products
group by category_id

-- ����� ������� ���� ����������� ������� 3� � ������ ���������
select category_id, avg(list_price) as avgPrice
from production.products
where list_price < 3000
group by category_id

-- ����� ������� ���� ����������� � ������ ���������, ������� ������ 3�
select category_id, avg(list_price) as avgPrice
from production.products
group by category_id
having avg(list_price) < 3000

-- ����� ������� ���� ������
select avg(list_price * (1-discount) * quantity) as avgSumm
from sales.order_items

-- ����� ������� ���� ������� ������
select order_id, avg(list_price * (1-discount) * quantity) as maxRealPrice
from sales.order_items
group by order_id

-- ����� ������� ���� ������� ������, �������� ��, ��� ��� ������ 200
select order_id, avg(list_price * (1-discount) * quantity) as maxRealPrice
from sales.order_items
group by order_id
having avg(list_price * (1-discount) * quantity) < 200

select order_id--, avg(list_price * (1-discount) * quantity) as maxRealPrice
from sales.order_items
group by order_id
having max(list_price * (1-discount) * quantity) < 1000
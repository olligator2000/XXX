select pp.brand_id as '����� ������'
from production.products pp

select top 10 *
from production.products
where category_id = 7
order by list_price desc, model_year desc
--desc - descending - ������� �� ��������

--1) ������� ��� ���������� 2017 ����

select *
from production.products as pp
where pp.model_year = 2017

--2) ������� �������� � ��� ������� ����������� ��� ������� 5

select pp.product_name, pp.model_year
from production.products as pp
where pp.brand_id = 5

--3) ������� ��� ���������� ������� 500

select *
from production.products
where list_price < 500

--4) ������� �������� � ���� ����������� ������ ������ � ������� �������� �����

select product_name, list_price
from production.products
where list_price > 1000 and list_price < 1500

select product_name, list_price
from production.products
where list_price between 1000 and 1500

--5) ������� �������� id � ���� ������ �������� ���������� ������� 3 �����

select top 1 product_id, product_name, list_price
from production.products
where list_price < 3000
order by list_price desc

--6) ����������� � between,
--7) ������� ��� ���������� � ����������� 2, 6 � 7


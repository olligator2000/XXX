use BikeStoresOld

--1) ������� ��� ���������� 2017 ����
select *
from production.products pp
where model_year = 2017

--2) ������� �������� � ��� ������� ����������� ��� ������� 5
select product_name, model_year
from production.products pp
where brand_id = 5

--3) ������� ��� ���������� ������� 500
select *
from production.products pp
where list_price < 500
order by list_price desc

--4) ������� �������� � ���� ����������� ������ ������ � ������� �������� �����
select product_name, list_price
from production.products pp
where list_price between 1000 and 1500
order by list_price desc

--5) ������� �������� id � ���� ������ �������� ���������� ������� 3 �����
select top 1 product_id, list_price
from production.products pp
where list_price < 3000
order by list_price desc


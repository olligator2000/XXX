insert into faculties (Name)
values	('���'),
		('��'),
		('���')

select *
from faculties

select *
from groups

insert into groups (name, faculty_id)
values ('�112', 1),
('�113', 1),
('�20', 2),
('�21', 2),
('�99', 3)

select *
from students

insert into students (name, birthYear, group_id)
values 
('���� ������', '05/05/1997', 4), 
('���� ������', '05/05/1998', 3)
, ('������� �������', '05/05/1990', 4)
, ('���� ������', '05/05/2000', 3)
, ('������� ��������', '05/05/1997', 1)
, ('��������� ������', '05/05/1995', 1)
, ('������ ������', '05/05/2001', 1)
, ('���� �������', '05/05/1999', 5)
, ('����� ��������', '05/05/1999', null)

update students
set name = '���� ������'
, birthYear = '01/01/1990'
where id = 13

delete
from students
where id = 13

select name, birthYear
from students
where id = 7

select birthYear
from students
where group_id = 1
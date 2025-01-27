insert into faculties (Name)
values	('ФВТ'),
		('ФЭ'),
		('ИЭФ')

select *
from faculties

select *
from groups

insert into groups (name, faculty_id)
values ('А112', 1),
('А113', 1),
('Р20', 2),
('Р21', 2),
('Ф99', 3)

select *
from students

insert into students (name, birthYear, group_id)
values 
('Иван Иванов', '05/05/1997', 4), 
('Петр Иванов', '05/05/1998', 3)
, ('Николай Семенов', '05/05/1990', 4)
, ('Один Одинов', '05/05/2000', 3)
, ('Дмитрий Дмитриев', '05/05/1997', 1)
, ('Александр Пушкин', '05/05/1995', 1)
, ('Сергей Есенин', '05/05/2001', 1)
, ('Илья Муромец', '05/05/1999', 5)
, ('Мария Цветаева', '05/05/1999', null)

update students
set name = 'Петр Петров'
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
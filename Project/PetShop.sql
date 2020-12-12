BEGIN TRANSACTION;
delete from Pet;
delete from Center;
delete from Client;
delete from Apply;

insert into Center values (1, 'Song-do', 10, 4.5, 'Y');
insert into Center values (2, 'Gang-nam', 30, 4.3, 'Y');
insert into Center values (3, 'Seon-hak', 10, 4.8, 'N');

insert into Client values ('01094016841', 'Y', 2, 24, 'Song-do');


insert into Pet VALUES (1, 'Dog', 2, 'Boy', 1);


insert into Apply values (1, '01094016841');

COMMIT;
drop table if exists apply;
drop table if exists Pet;
drop table if exists Center;
drop table if exists Client;

create table Pet(Pet_Number text, Species text, Age text, Sex text, Center_Number text,
primary key (Pet_Number)
FOREIGN key (Center_Number) REFERENCES Center(Center_Number) on DELETE CASCADE on update CASCADE);

create table Center(Center_Number text, Location text, Many_Pet text, Grade text, Pet_Hospital text,
primary key (Center_Number));

create table Client(Phone_Number text, Experience text, Have_many text, C_age text, C_location text, Apply_Center text,
primary key (Phone_Number));

CREATE TABLE apply (Center_Number text, Phone_Number text,
PRIMARY key (Center_Number, Phone_Number),
FOREIGN key (Center_Number) REFERENCES Center(Center_Number) on DELETE CASCADE on update CASCADE
FOREIGN key (Phone_Number) REFERENCES Client(Phone_Number) on DELETE CASCADE on update CASCADE);


-----------------------------------------------------------------

BEGIN TRANSACTION;
delete from Pet;
delete from Center;
delete from Client;
delete from Apply;

insert into Center values ('1', '인천', '10', '4.5', 'Y');
insert into Center values ('2', '서울', '30', '4.3', 'Y');
insert into Center values ('3', '대전', '10', '4.8', 'N');

insert into Client values ('01094016841', 'Y', '2', '24', '인천','1');
insert into Client values ('01012345678', 'N', '0', '24', '서울','2');
insert into Client values ('01088887444', 'Y', '1', '19', '서울','1');
insert into Client values ('01062225541', 'Y', '1', '22', '서울','2');


insert into Pet VALUES ('1', '진돗개', '2', '♂', '1');
insert into Pet VALUES ('2', '말티즈', '1', '♀', '1');
insert into Pet VALUES ('3', '시츄', '1', '♀', '2');
insert into Pet VALUES ('4', '비숑프리제', '2', '♀', '3');
insert into Pet VALUES ('5', '푸들', '1', '♂', '3');
insert into Pet VALUES ('6', '말티즈', '2', '♂', '3');


insert into Apply values (1, '01094016841');
insert into Apply values (1, '01012345678');



COMMIT;
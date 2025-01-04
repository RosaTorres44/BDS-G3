-- Active: 1735349738436@@rtgmysql.mysql.database.azure.com@3306@datag3
drop table alumno; 

CREATE TABLE alumno(
  `id_alumno` int NOT NULL AUTO_INCREMENT,
  `nro_doc` varchar(10) NOT NULL,
  `nombre` varchar(250) NOT NULL,
  `mail` varchar(250) DEFAULT NULL ,
  PRIMARY KEY (`id_alumno`)
) COMMENT='Tabla de alumnos'

insert into  alumno ( nro_doc, nombre) 
values 
( '100', 'hanna') ,
( '200', 'zoe' ) ,
( '300', 'henry'  ) , 
( '400', 'rosa' ), 
( '500', 'luis' ) ; 


create table curso ( 
  id_curso int not null auto_increment, 
  nombre varchar(100), 
  primary key (id_curso)
);

insert into curso (nombre) values ('matematica'), ('fisica'), ('quimica');


drop table notas_curso; 


CREATE TABLE `notas_curso` (
  `id_curso_notas` int NOT NULL AUTO_INCREMENT,
  `id_alumno` int NOT NULL,
   `curso_id`  int not null,
  `nota` double,
  PRIMARY KEY (`id_curso_notas`),
  FOREIGN KEY (`id_alumno`) REFERENCES alumno(`id_alumno`),
  FOREIGN KEY (`curso_id`) REFERENCES curso(`id_curso`)
) ; 

insert into notas_curso ( id_alumno, curso_id, nota) VALUES
(1, 1, 20),
(2, 1, 19),
(3, 1, 18),
(4, 1, 18),
(5, 1, 10),
(1, 2, 20),
(2, 2, 19),
(3, 2, 18),
(4, 2, 18),
(5, 2, 10),
(1, 3, 20),
(2, 3, 19),
(3, 3, 18),
(4, 3, 18),
(5, 3, 10);




drop table empresa; 

CREATE TABLE empresa(
  `id_empresa` int NOT NULL AUTO_INCREMENT,
  `nro_ruc` varchar(11) NOT NULL,
  `nombre` varchar(250) NOT NULL,
  `mail` varchar(250) DEFAULT NULL ,
  PRIMARY KEY (`id_empresa`)
) COMMENT='Tabla de empresas';

insert into  empresa ( nro_ruc, nombre, mail) 
values 
('20100123456', 'Empresa 1', 'emp1@gmail.com'),
('20100123457', 'Empresa 2', 'emp2@gmail.com'),
('20100123458', 'Empresa 3', 'emp3@gmail.com'),
('20100123459', 'Empresa 4', 'emp4@gmail.com'),
('20100123460', 'Empresa 5', 'emp5@gmail.com'),
('20100123461', 'Empresa 6', 'emp6@gmail.com'),
('20100123462', 'Empresa 7', 'emp7@gmail.com'),
('20100123463', 'Empresa 8', 'emp8@gmail.com'),
('20100123464', 'Empresa 9', 'emp9@gmail.com');


create table ciudad ( 
  id_ciudad int not null auto_increment, 
  nombre_ciudad varchar(100), 
  primary key (id_ciudad)
)COMMENT='Tabla de ciudades';

insert into ciudad (nombre_ciudad) values 
('Lima'),
('Arequipa'),
('Cusco'),
('Trujillo'),
('Piura'),
('Iquitos'),
('Tacna'),
('Puno'),
('Chiclayo'),
('Huancayo');


CREATE TABLE `direcciones` (
  `id_direccion` int NOT NULL AUTO_INCREMENT,
  `id_ciudad` int NOT NULL ,
  `id_empresa` int NOT NULL,
  `direccion`  varchar(250) NOT NULL, 
  PRIMARY KEY (`id_direccion`),
  FOREIGN KEY (`id_ciudad`) REFERENCES ciudad(`id_ciudad`),
  FOREIGN KEY (`id_empresa`) REFERENCES empresa(`id_empresa`)
) ; 

insert into direcciones (id_ciudad, id_empresa, direccion) values 
(1, 1, 'Av. Javier Prado 1234'),
(2, 2, 'Av. Arequipa 1234'),
(3, 3, 'Av. Cusco 1234'),
(4, 4, 'Av. Trujillo 1234'),
(5, 5, 'Av. Piura 1234'),
(6, 6, 'Av. Iquitos 1234'),
(7, 7, 'Av. Tacna 1234'),
(8, 8, 'Av. Puno 1234'),
(9, 9, 'Av. Chiclayo 1234'),
(1, 1, 'Av. Javier Prado 1234'),
(2, 2, 'Av. Arequipa 1234'),
(3, 3, 'Av. Cusco 1234'),
(4, 4, 'Av. Trujillo 1234'),
(5, 5, 'Av. Piura 1234'),
(6, 6, 'Av. Iquitos 1234'),
(7, 7, 'Av. Tacna 1234'),
(8, 8, 'Av. Puno 1234'),
(9, 9, 'Av. Chiclayo 1234');

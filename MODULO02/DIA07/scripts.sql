--select
select * from empleado ;
select  * from empleado LIMIT 10; 

select * from empleado ORDER BY salario DESC limit 10; 

select count(1) from empleado WHERE salario > 5000;

select COUNT(1) from empleado WHERE salario > 5000 AND salario < 10000;

select max(salario) max, min(salario) min, 
avg(salario) prom 
from empleado;

select distinct pais from empleado;

select pais, count(1)  from empleado group by pais 
order by 2 Desc;


select pais, area, max(salario) max, min(salario) min, avg(salario) prom 
from empleado 
where pais = 'Argentina'
group by pais, area 
order by 1 desc ; 

select pais, avg(salario)
from empleado
group by pais
having avg(salario) > 5000; 

select * from empleado 
where salario > (select avg(salario) from empleado);




-- A ALUMNO
-- B NOTAS
-- C CURSO

-- LEFT JOIN
select alumno.nombre,nota.nota 
from alumno left join notas_curso nota
 on nota.id_alumno = alumno.id_alumno;
 

-- RIGHT JOIN
 
select curso.nombre,avg(nota.nota)
from notas_curso nota RIGHT JOIN curso on nota.curso_id = curso.id_curso
GROUP BY curso.nombre;

-- INNER JOIN
select alumno.nombre,curso.nombre,notas_curso.nota
from notas_curso  
inner join alumno on notas_curso.id_alumno = alumno.id_alumno 
inner join curso on notas_curso.curso_id = curso.id_curso
order by alumno.nombre;

/*
# Devuelve el listado de las asignaturas que se imparten en el primer cuatrimestre, en el tercer curso del grado que tiene el identificador 7.
SELECT * FROM asignatura
WHERE cuatrimestre = 1 AND curso =3 AND id_grado=7
*/
/*
# 4. Devuelve el listado de profesores que no han dado de alta su número de teléfono en la base de datos y además su nif termina en K.
SELECT * FROM persona
WHERE tipo = 'profesor' AND telefono IS NULL
	AND nif LIKE COLLATE utf8mb4_bin '%K'
*/
/*
#Filtro de fechas
#3. Devuelve el listado de los alumnos que nacieron en 1999.
SELECT * FROM persona
#Forma 1 mas sencilla
#WHERE YEAR (fecha_nacimiento) = 1999;
#Forma 2 
#WHERE fecha_nacimiento BETWEEN '1999-01-01' AND '1999-12-31'
#Forma 3 
#WHERE fecha_nacimiento >= '1999-01-01' AND fecha_nacimiento >= '1999-12-31'
#Forma 4
WHERE fecha_nacimiento LIKE '1999%'
*/
/*
#Filtrando y concatenando datos
# 2. Averigua el nombre y los dos apellidos de los alumnos que no han dado de alta su número de teléfono en la base de datos.
SELECT nombre, concat(apellido1,' ',apellido2) AS apellidos FROM persona
WHERE tipo = 'alumno' AND telefono IS NULL
#Calcula cuántos alumnos nacieron en 1999.
SELECT count(*) AS "nacidos en 1999" FROM persona 
WHERE tipo = 'alumno' AND YEAR(fecha_nacimiento) = 1999
*/
/*
#Devuelve un listado con el primer apellido, segundo apellido y el nombre de todos los alumnos. El listado deberá estar ordenado alfabéticamente de menor a mayor por el primer apellido, segundo apellido y nombre.
SELECT apellido1 AS "Primer Apellido",apellido2 AS "Segundo Apellido",nombre FROM persona
WHERE tipo = 'alumno' 
ORDER BY apellido1 ASC
*/
/*
#Calcula cuántos profesores hay en cada departamento. El resultado sólo debe mostrar dos columnas, una con el nombre del departamento y otra con el número de profesores que hay en ese departamento. El resultado sólo debe incluir los departamentos que tienen profesores asociados y deberá estar ordenado de mayor a menor por el número de profesores.
#Con la actualizacion ya no es necesario el AS para el alias
SELECT d.nombre, COUNT(p.id_profesor) AS Num_Prof FROM departamento d
JOIN profesor p ON d.id = p.id_departamento
GROUP BY d.nombre
ORDER BY Num_Prof ASC
*/

#Devuelve un listado con el nombre de todos los grados existentes en la base de datos y el número de asignaturas que tiene cada uno, de los grados que tengan más de 40 asignaturas asociadas.
SELECT g.nombre, COUNT(a.id) Num_asig FROM grado g
LEFT JOIN asignatura a ON g.id = a.id_grado
GROUP BY g.nombre
#HAVING Num_asig > 40

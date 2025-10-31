#Consultando nombre de la tabla fabricante, left selecciona dos valores a la izquierda
#UPPER y LOWER para pasar mayusculas o minusculas
#AS alias para encabezados
#FROM nombre de la entidad 
SELECT nombre, LEFT(UPPER(nombre),2) AS Valor FROM fabricante
ORDER BY nombre DESC;
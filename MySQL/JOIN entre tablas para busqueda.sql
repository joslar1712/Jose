SELECT f.nombre as fabricante, p.nombre as producto FROM fabricante as f
LEFT JOIN producto as p ON f.id = p.id_fabricante
WHERE p.id IS NULL

/*
#Relacion entre llaves foraneas y primarias para consultas
entre dos tablas
SELECT producto.nombre,producto.precio, fabricante.nombre FROM producto
JOIN fabricante ON producto.id_fabricante = fabricante.id
#Usando alias
#No hay diferencia entre JOIN e INNER JOIN	
SELECT p.nombre,p.precio,p.nombre as fabricante FROM producto as p
INNER JOIN fabricante as f ON p.id_fabricante=f.id

#Para orden alfabético
SELECT p.nombre,p.precio,p.nombre as fabricante FROM producto as p
INNER JOIN fabricante as f ON p.id_fabricante=f.id
ORDER BY fabricante

#Para orden alfabético
SELECT p.nombre,p.precio,p.nombre as fabricante FROM producto as p
INNER JOIN fabricante as f ON p.id_fabricante=f.id
#WHERE producto = "Lenovo"
#WHERE f.id = 2
#WHERE p.id_fabricante = 2

#LEFT JOIN
#Relacionando producto de cada fabricante
SELECT f.nombre as fabricante, p.nombre as producto FROM fabricante as f
Left JOIN producto as p ON f.id = p.id_fabricante

	#Condicionales en el LEFT JOIN
	SELECT f.nombre as fabricante, p.nombre as producto FROM fabricante as f
	Left JOIN producto as p ON f.id = p.id_fabricante
    #Cuando producto id es null al juntar ambas tablas
	WHERE p.id IS NULL

*/
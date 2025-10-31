# Seleccionamos id y con distinc eliminamos los duplicados
SELECT DISTINCT id_fabricante FROM producto
/*
Para ordenar fabricante en orden alfabetico
SELECT nombre FROM fabricante
ORDER BY nombre DESC;
Al seleccionar dos campos solo uno de ellos se pude ordenar
SELECT nombre, precio FROM producto
ORDER BY precio DESC;
Limitando las filas de las consultas * selecciona todo.
SELECT * FROM fabricante
LIMIT 5;
Limitando la consulta en un rango, posicionamiento, limite
SELECT * FROM fabricante
Limit 3, 2; 
Escogiendo el producto mas barato
SELECT nombre, precio FROM producto
ORDER BY  precio ASC (DES) el mas caro.
LIMIT 1
	O de esta forma mas eficioente
	SELECT nombre, MIN(precio) FROM producto
	SELECT nombre, MAX(precio) FROM producto
Buscando producto por Id
SELECT nombre, id_fabricante FROM producto
WHERE id_fabricante = 2
WHERE se usa cuando hay una condicion para la consulta
SELECT nombre, precio FROM producto
WHERE precio <= 120
Where not Los que no son mayor o igual a 400
SELECT nombre, precio FROM producto
WHERE not (precio >= 400)
Para consultar entre un rango de valores
SELECT nombre, precio FROM producto
WHERE precio >=80 AND precio<=300
	Usando funcion explicita BETWEEN
    SELECT nombre, precio FROM producto
	WHERE precio BETWEEN 80 AND 300
Filtrando por precio y ID
#SELECT nombre, precio, id_fabricante FROM producto
SELECT * FROM producto
WHERE precio>200 AND id_fabricante=6 
Condicional OR y WHERE
SELECT * FROM producto
WHERE id_fabricante=1 OR id_fabricante=3 OR id_fabricante=5
	Opcion mas sencilla usando IN
	SELECT * FROM producto
	WHERE id_fabricante IN (1,3,5)
Consulta nommbres que inicien, terminen o contengan un caracter.
o una cadena especifica ej. Portátil
SELECT nombre FROM fabricante
# %=cualquier cosa
Inicie con S
WHERE nombre LIKE 'S%'
Termine con S
WHERE nombre LIKE '%S'
Contenga S
WHERE nombre LIKE '%S%'
Forzando a un caracter especial
WHERE nombre COLLATE utf8mb4_bin LIKE '%S%'
	Sinn el collate somos mas flecibles para minusculas, mayusculas caracteres especiales
	WHERE nombre LIKE '%S%'
Longitud de caracteres
SELECT nombre FROM fabricante
WHERE LENGTH(nombre)=4 
Filtrando producto y precio especifico
SELECT nombre FROM producto
WHERE nombre COLLATE utf8mb4_bin LIKE '%Monitor%' AND precio<215

*/

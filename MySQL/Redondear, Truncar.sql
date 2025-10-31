#
SELECT nombre, precio, 
ROUND(precio,0) AS Redondea, 
TRUNCATE(precio,0) AS Truncar FROM producto

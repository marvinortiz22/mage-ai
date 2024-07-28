CREATE TABLE agrosantanadb.clean.dim_products1 as
SELECT 
    NUMERO_DE_ARTICULO as id_producto,
    DESCRIPCION_DEL_ARTICULO as nombre_producto,
	EN_STOCK,
	NOMBRE_DE_LA_LISTA_DE_PRECIOS as tipo_de_precio,
	PRECIO_DE_LISTA as precio_publico,
	ITERMEDIO as precio_intermedio,
	DISTRIBUIDOR as precio_distribuidor,
	COSTO_DEL_ARTICULO as costo_sin_IVA,
	COSTO_MAS_IVA as costo_mas_IVA
FROM agrosantanadb.raw.products

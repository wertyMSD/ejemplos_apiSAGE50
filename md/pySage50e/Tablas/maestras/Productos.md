---
Alias: productos api sage50
Creado fecha: 2023-04-10 08:33
Modificado date: domingo 30º abril 2023 19:09:13
Tags: apisage50,productos
obs.html.data:
  inclusion_references:
  - pysage50e/tablas/tablas relacionadas articulos.md
  - pysage50e/notas varias/creacion automatica.md
---
   
Modificado : `$= dv.current().file.mtime`   
   
# Generador campos disponibles   
   
```
api50.product()
```
   
   
## Tablas Relacionadas   
   

#### Disponibles   
   
| **Recursos** 	|   **Uso**   	|   
|:--------------:	|:--------------------------:	|   
|[Ofertas](../../../pySage50e/Tablas/relacionadas/Ofertas.md) |ManteTrel Ofertas||   
|[Precios](../../../pySage50e/Tablas/relacionadas/Precios.md) |ManteTrel Precios||   
|[Referencias](../../../pySage50e/Tablas/relacionadas/Referencias.md) |ManteTrel Relacion con [Proveedores](../../../pySage50e/Tablas/maestras/Proveedores.md)||   
|[StockMaxMinAlmacen](../../../pySage50e/Tablas/relacionadas/StockMaxMinAlmacen.md) |ManteTrel Stock Max / Min por [Almacen](/not_created.md)||   
|[Imagenes](../../../pySage50e/Tablas/relacionadas/Imagenes.md) |ManteTrel Imagenes/Documentos||   
|[CamposAdicionales](../../../pySage50e/Tablas/relacionadas/CamposAdicionales.md) |ManteTrel Campos Libres||   
|[Idiomas](../../../pySage50e/Tablas/relacionadas/Idiomas.md) |ManteTrel Traduciones||   
   
   
   
   
   
------------------------   
# Metodo Creador / Modificador   
   
```python
campos={'Codigo': 'articulo ejemplo'
		,'nombre': 'articulo Ejemplo'
		,'familia':"01",'tipo_iva':"03"}

api50.product(campos)
```
   
   
>[!warning] Campos minimos Creación   
>  - Codigo   
>  - Nombre    
>  - Familia    
>  - Tipo_Iva   
   
>[!tip] Campo minimo Modificación   
>  - Codigo   
>     
   
   
### Tablas vinculadas   
   
|Recursos 	|   **[Creacion automatica](../../../pySage50e/notas%20varias/Creacion%20automatica.md)**   	|    
|:--------------	|:--------------------------:	|   
|[Familias](../../../pySage50e/Tablas/vinculadas/Familias.md)|🆗|   
|[SubFamilias](../../../pySage50e/Tablas/vinculadas/SubFamilias.md)|🆗|   
|[Marcas](../../../pySage50e/Tablas/vinculadas/Marcas.md)|🆗|   
|[Caracteristicas](../../../pySage50e/Tablas/vinculadas/Caracteristicas.md)|🆗|   
   

#### Configuración creación automatica   
   
>[!tip] Configuracion Opcional Creacion Automatica   
>Por defecto se crear si no existen los registros.   
>Usa como *NOMBRE* el mismo que el codigo.   
> _Modifique dicho parametro si no es requerido.__   
>[Fichero configsql.ini](/not_created.md)
   
   
   
   
------------------------   
# Metodo Extraer Registro   
```
api50.product(cextraer='Codigo_Producto')

```
   
   
>[!tip] Campo necesario    
>  - Codigo   
>     
   
Regresa tabla en formato JSON con cada registro de Tabla principal y  tablas relacionadas.   
   
   
------------------------   
# Metodo lista   
Devuelve  una variable con un tabla con los registros que cumple la condicion en la tabla.   
   
```
lista=api50.product(wlista="Familia='01'")

import json
if len(lista)>0:  
	for reg in lista[0]:  
		ajson=api50.product(cextraer=reg["Codigo"])  
		  
		print(json.loads(ajson[0]))

```
   
   
# Codigo Ejemplo   
   
[GitHub](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/maestros-articulos.py)   
   
[Lista Campos disponibles ](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/Articulo.txt)
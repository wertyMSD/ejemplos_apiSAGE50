---
Alias: familias api sage50
Creado fecha: 2023-04-04 08:52
Tags: apisage50 py
obs.html.data:
  inclusion_references:
  - pysage50e/tablas/tablas relacionadas familias.md
  - pysage50e/notas varias/creacion automatica.md
---
   
Modificado : `$= dv.current().file.mtime`   
   
# Generador campos disponibles   
   
```
api50.family()
```
   
   
## Tablas Relacionadas   
   

   
Modificado : `$= dv.current().file.ctime`   
   
### Documentacion tecnica   
[Sage50: Referencia de la Clase sage.ew.articulo.Familia](http://descargas.sage.es/Sage50/Documentacion_html/html/de/d01/classsage_1_1ew_1_1articulo_1_1_familia.html)   
   
### Disponibles   
|Recursos 	|   **[Creacion automatica](../../../pySage50e/notas%20varias/Creacion%20automatica.md)**   	|    
|:--------------	|:--------------------------:	|   
|[Descuentos Familia-Subfamilia](../../../pySage50e/Tablas/relacionadas/Descuentos%20Familia-Subfamilia.md)|🆗|
   
   
   
------------------------   
# Metodo Creador / Modificador   
   
```python
campos={
	    'Codigo': 'Codigo Ejemplo'
		'nombre': 'Familia Ejemplo'
		}

api50.family(campos)
```
   
   
>[!warning] Campos minimos Creación   
   
>  - Codigo    
>  - Nombre    
   
   
>[!tip] Campo minimo Modificación   
>  - Codigo   
   
   
   
### Tablas vinculadas   
   
Ninguna   
   
   
   

#### Configuración creación automatica   
   
>[!tip] Configuracion Opcional Creacion Automatica   
>Por defecto se crear si no existen los registros.   
>Usa como *NOMBRE* el mismo que el codigo.   
> _Modifique dicho parametro si no es requerido.__   
>[Fichero configsql.ini](/not_created.md)
   
   
   
   
------------------------   
# Metodo Extraer Registro   
```
api50.family(cextraer=Codigo Familia)

```
   
   
>[!tip] Campo necesario    
>  - Codigo   
>     
   
Regresa tabla en formato JSON con cada registro de Tabla principal y  tablas relacionadas.   
   
   
------------------------   
# Metodo lista   
Devuelve  una variable con un tabla con los registros que cumple la condicion en la tabla.   
   
```
lista=api50.family(wlista="")

import json
if len(lista)>0:  
	for reg in lista[0]:  
		ajson=api50.family(cextraer=reg["Codigo"])  
		  
		print(json.loads(ajson[0]))

```
   
   
# Codigo Ejemplo   
   
[GitHub](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/vinculados-familias.py)   
   
[Lista Campos disponibles ](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/Familia.txt)
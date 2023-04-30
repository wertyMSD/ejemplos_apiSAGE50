---
Alias: proveedores api sage50
Creado fecha: 2023-04-12 17:07
Tags: apisage50 py
obs.html.data:
  inclusion_references:
  - pysage50e/notas varias/creacion automatica.md
---
   
Modificado : `$= dv.current().file.mtime`   
# Generador campos disponibles   
   
```
api50.supplier()
```
   
   
## Tablas Relacionadas   
   
> **obsidian-html error:** Could not find page Tablas Relacionadas Proveedores 1#Disponibles.   
   
   
------------------------   
# Metodo Creador / Modificador   
   
```python
campos={
		'nombre': 'Proveedor Ejemplo'
		}

api50.supplier(campos)
```
   
   
>[!warning] Campos minimos Creación   
   
>  - Nombre    
   
   
>[!tip] Campo minimo Modificación   
>  - Codigo   
   
   
   
### Tablas vinculadas   
   
|Recursos 	|   **[Creacion automatica](../../../pySage50e/notas%20varias/Creacion%20automatica.md)**   	|    
|:--------------	|:--------------------------:	|   
|[FormaPago](../../../pySage50e/Tablas/vinculadas/FormaPago.md)|🆗|   
   
   

#### Configuración creación automatica   
   
>[!tip] Configuracion Opcional Creacion Automatica   
>Por defecto se crear si no existen los registros.   
>Usa como *NOMBRE* el mismo que el codigo.   
> _Modifique dicho parametro si no es requerido.__   
>[Fichero configsql.ini](/not_created.md)
   
   
   
   
------------------------   
# Metodo Extraer Registro   
```
api50.supplier(cextraer='Codigo_Proveedor')

```
   
   
>[!tip] Campo necesario    
>  - Codigo   
>     
   
Regresa tabla en formato JSON con cada registro de Tabla principal y  tablas relacionadas.   
   
   
------------------------   
# Metodo lista   
Devuelve  una variable con un tabla con los registros que cumple la condicion en la tabla.   
   
```
lista=api50.supplier(wlista="cpostal='11500'")

import json
if len(lista)>0:  
	for reg in lista[0]:  
		ajson=api50.supplier(cextraer=reg["Codigo"])  
		  
		print(json.loads(ajson[0]))

```
   
   
# Codigo Ejemplo   
   
[GitHub](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/maestros-Proveedores.py)   
   
[Lista Campos disponibles ](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/Proveedor.txt)
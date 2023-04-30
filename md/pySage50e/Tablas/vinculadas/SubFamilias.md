---
Alias: familias api sage50
Creado fecha: 2023-04-04 08:52
Tags: apisage50 py
obs.html.data:
  inclusion_references:
  - pysage50e/tablas/tablas relacionadas subfamilias.md
  - pysage50e/notas varias/creacion automatica.md
---
   
Modificado : `$= dv.current().file.mtime`   
   
# Generador campos disponibles   
   
```
api50.subfamily()
```
   
   
## Tablas Relacionadas   
   

Obsidianhtml: Error: Unable to find section #disponible in Tablas Relacionadas subFamilias
   
   
   
------------------------   
# Metodo Creador / Modificador   
   
```python
campos={
	    'Codigo': 'Codigo Ejemplo'
		'nombre': 'Subfamilia Ejemplo'
		}

api50.subfamily(campos)
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
api50.subfamily(cextraer=Codigo Subfamilia)

```
   
   
>[!tip] Campo necesario    
>  - Codigo   
>     
   
Regresa tabla en formato JSON con cada registro de Tabla principal y  tablas relacionadas.   
   
   
------------------------   
# Metodo lista   
Devuelve  una variable con un tabla con los registros que cumple la condicion en la tabla.   
   
```
lista=api50.subfamily(wlista="")

import json
if len(lista)>0:  
	for reg in lista[0]:  
		ajson=api50.subfamily(cextraer=reg["Codigo"])  
		  
		print(json.loads(ajson[0]))

```
   
   
# Codigo Ejemplo   
   
[GitHub](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/vinculados-Subfamilia.py)   
   
[Lista Campos disponibles ](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/Subfamilia.txt)
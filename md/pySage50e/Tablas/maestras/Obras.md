---
Alias: obras api sage50
Creado fecha: 2023-04-12 17:10
Tags: apisage50 py
obs.html.data:
  inclusion_references:
  - pysage50e/tablas/tablas relacionadas obras.md
---
   
Modificado : `$= dv.current().file.mtime`   
# Generador campos disponibles   
   
```
api50.work()
```
   
   
## Tablas Relacionadas   
   
   

### Disponibles   
|Recursos 	|   **[Creacion automatica](../../../pySage50e/notas%20varias/Creacion%20automatica.md)**   	|    
|:--------------	|:--------------------------:	|   
|[Imagenes](../../../pySage50e/Tablas/relacionadas/Imagenes.md)|🆗|
   
   
   
------------------------   
# Metodo Creador / Modificador   
   
```python
campos={'Codigo': '12345'
		,'nombre': 'Obra Ejemplo'
		}

api50.work(campos)
```
   
   
>[!warning] Campos minimos Creación   
>  - Codigo   
>  - Nombre    
   
   
>[!tip] Campo minimo Modificación   
>  - Codigo   
>     
   
   
   
   
   
------------------------   
# Metodo Extraer Registro   
```
api50.work(cextraer='12345')

```
   
   
>[!tip] Campo necesario    
>  - Codigo   
>     
   
Regresa tabla en formato JSON con cada registro de Tabla principal y  tablas relacionadas.   
   
   
------------------------   
# Metodo lista   
Devuelve  una variable con un tabla con los registros que cumple la condicion en la tabla.   
   
```
lista=api50.work(wlista="Terminada=False")

import json
if len(lista)>0:  
	for reg in lista[0]:  
		ajson=api50.work(cextraer=reg["Codigo"])  
		  
		print(json.loads(ajson[0]))

```
   
   
# Codigo Ejemplo   
   
[GitHub](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/maestros-Obras.py)   
   
[Lista Campos disponibles ](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/Obra.txt)
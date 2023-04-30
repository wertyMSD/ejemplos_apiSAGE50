---
Alias: vendedor api sage50
Creado fecha: 2023-04-04 08:52
Tags: apisage50 py
obs.html.data:
  inclusion_references:
  - pysage50e/tablas/tablas relacionadas vendedores.md
  - pysage50e/notas varias/creacion automatica.md
---
   
Modificado : `$= dv.current().file.mtime`   
   
# Generador campos disponibles   
   
```
api50.salesman()
```
   
   
## Tablas Relacionadas   
   

   
Modificado : `$= dv.current().file.ctime`   
### Documentacion tecnica   
[Sage50: Referencia de la Clase sage.ew.cliente.Vendedor](http://descargas.sage.es/Sage50/Documentacion_html/html/d4/d92/classsage_1_1ew_1_1cliente_1_1_vendedor.html)   
   
#### Disponibles   
   
| **Recursos** 	|   **Uso**   	|   
|:--------------:	|:--------------------------:	|   
|[Comisiones](../../../pySage50e/Tablas/relacionadas/Comisiones.md) |ManteTrel de comision de vendedores||
   
   
   
------------------------   
# Metodo Creador / Modificador   
   
```python
campos={
	    'Codigo': 'Codigo Ejemplo'
		'nombre': 'vendedor Ejemplo'
		}

api50.salesman(campos)
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
api50.salesman(cextraer=Codigo Vendedor)

```
   
   
>[!tip] Campo necesario    
>  - Codigo   
>     
   
Regresa tabla en formato JSON con cada registro de Tabla principal y  tablas relacionadas.   
   
   
------------------------   
# Metodo lista   
Devuelve  una variable con un tabla con los registros que cumple la condicion en la tabla.   
   
```
lista=api50.salesman(wlista="cpostal='11500'")

import json
if len(lista)>0:  
	for reg in lista[0]:  
		ajson=api50.salesman(cextraer=reg["Codigo"])  
		  
		print(json.loads(ajson[0]))

```
   
   
# Codigo Ejemplo   
   
[GitHub](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/vinculados-vendedores.py)   
   
[Lista Campos disponibles ](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/vendedor.txt)
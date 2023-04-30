---
Alias: clientes api sage50
Creado fecha: 2023-04-12 17:09
Tags: apisage50 py
obs.html.data:
  inclusion_references:
  - pysage50e/tablas/tablas relacionadas clientes.md
  - pysage50e/notas varias/creacion automatica.md
---
   
Modificado : `$= dv.current().file.mtime`   
   
# Generador campos disponibles   
   
```
api50.customer()
```
   
   
## Tablas Relacionadas   
   

#### Disponibles   
   
| **Recursos** 	|   **Uso**   	|   
|:--------------:	|:--------------------------:	|   
|[Contactos](../../../pySage50e/Tablas/relacionadas/Contactos.md) |ManteTrel de contactos||   
|[Bancos](../../../pySage50e/Tablas/relacionadas/Bancos.md) |ManteTrel de Datos Bancarios||   
|[Descuentos](../../../pySage50e/Tablas/relacionadas/Descuentos.md) |ManteTrel de descuentos||   
|[Direcciones](../../../pySage50e/Tablas/relacionadas/Direcciones.md) |ManteTrel de direcciones||   
|[Imagenes](../../../pySage50e/Tablas/relacionadas/Imagenes.md) |ManteTrel de ficheros asociados||   
|[CamposAdicionales](../../../pySage50e/Tablas/relacionadas/CamposAdicionales.md) |Campos adicionales|   
   
   
   
   
   
------------------------   
# Metodo Creador / Modificador   
   
```python
campos={
		'nombre': 'Cliente Ejemplo'
		}

api50.customer(campos)
```
   
   
>[!warning] Campos minimos Creación   
   
>  - Nombre    
   
   
>[!tip] Campo minimo Modificación   
>  - Codigo   
   
   
   
### Tablas vinculadas   
   
|Recursos 	|   **[Creacion automatica](../../../pySage50e/notas%20varias/Creacion%20automatica.md)**   	|    
|:--------------	|:--------------------------:	|   
|[Vendedores](../../../pySage50e/Tablas/vinculadas/Vendedores.md)|🆗|   
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
api50.customer(cextraer='Codigo_cliente')

```
   
   
>[!tip] Campo necesario    
>  - Codigo   
>     
   
Regresa tabla en formato JSON con cada registro de Tabla principal y  tablas relacionadas.   
   
   
------------------------   
# Metodo lista   
Devuelve  una variable con un tabla con los registros que cumple la condicion en la tabla.   
   
```
lista=api50.customer(wlista="cpostal='11500'")

import json
if len(lista)>0:  
	for reg in lista[0]:  
		ajson=api50.customer(cextraer=reg["Codigo"])  
		  
		print(json.loads(ajson[0]))

```
   
   
# Codigo Ejemplo   
   
[GitHub](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/maestros-Clientes.py)   
   
[Lista Campos disponibles ](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/Cliente.txt)
---
Alias: clientes api sage50
Creado fecha: 2023-04-12 17:09
Modificado date: miércoles 12º abril 2023 17:09:46
Tags: apisage50 py
obs.html.data:
  inclusion_references:
  - 100_proyectos/sage50/pysage50e/tablas/tablas relacionadas recursos maestros.md
---
   
# Uso Rapido   
```python
import apiSage50
api50=apiSage50.apiSage50()
print("Genero Lista campos-------------------------------------")  
campos=api50.product()
print(campos)
print("Creacion Campos Minimos---------------------------------")  
campos={'Codigo': 'CodigoEjemplo',
		'Nombre': 'Articulo Ejemplo',
		'Familia':"001",
		'Tipo_iva':"03"}
resultado=api50.product(campo))  
print(resultado[1])
print("Extrae Creacion anterior--------------------------------")  
print(api50.product(cextraer=resultado[0]))
```
   
   
   
------------------------   
# Generador campos disponibles   
   
```
api50.product()
```
   
   
## Tablas Relacionados   
   

# Clientes   
   
[Sage50: Referencia de la Clase sage.ew.cliente.Cliente](http://descargas.sage.es/Sage50/Documentacion_html/html/d4/d8b/classsage_1_1ew_1_1cliente_1_1_cliente.html)   
   
| **Recursos** 	|   **Uso**   	| Estado 	|   
|:--------------:	|:--------------------------:	|:--:	|   
|[Contactos](/not_created.md) |ManteTrel de contactos||   
|[Bancos](/not_created.md) |ManteTrel de Datos Bancarios||   
|[Descuentos](/not_created.md) |ManteTrel de descuentos||   
|[Direcciones](/not_created.md) |ManteTrel de direcciones||   
|[Entregas](/not_created.md) |ManteTrel de entregas||   
|[Giros](/not_created.md) |ManteTrel de giros||   
|[Imagenes](/not_created.md) |ManteTrel de ficheros asociados||   
|[Vacaciones](/not_created.md) |ManteTrel de vacaciones||   
|[Actividades](/not_created.md) |ManteTrel de actividades||   
|[Cuotas](/not_created.md) |ManteTrel de cuotas||   
|[CamposAdicionales](/not_created.md) |Campos adicionales|
   
   
   
   
   
Campos adicionales   
   
------------------------   
# Metodo Creador / Modificador   
   
```python
campos={'Codigo': 'articuloejemolo','nombre': 'articulo Ejemplo','familia':"001",'tipo_iva':"03"}

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
   
   
|Recursos 	|   **Uso**   	| Estado 	|   
|:--------------	|:--------------------------:	|:--:	|   
|[Familias](../../../../../100_Proyectos/Sage50/pySage50e/tablas/vinculadas/Familias.md)||   
|[SubFamilias](../../../../../100_Proyectos/Sage50/pySage50e/tablas/vinculadas/SubFamilias.md)||   
|[Marcas](../../../../../100_Proyectos/Sage50/pySage50e/tablas/vinculadas/Marcas.md)||   
|[Caracteristicas](../../../../../100_Proyectos/Sage50/pySage50e/tablas/vinculadas/Caracteristicas.md)||   
   
   
   
>[!tip] Configuracion Opcional   
>Por defecto se crear si no existen los registros.   
>Usa como *NOMBRE* el mismo que el codigo.   
> _Modifique dicho parametro si no es requerido.__   
>[Fichero configsql.ini](/not_created.md)   
   
   
------------------------   
# Metodo Extraer Registro   
```
api50.product(cextraer='Codigo_Producto')

```
   
   
>[!tip] Campo necesario Modificación   
>  - Codigo   
>     
   
Regresa tabla en formato JSON con cada registro de Tabla principal y  tablas relacionadas. 
# Articulos   
   
   
   

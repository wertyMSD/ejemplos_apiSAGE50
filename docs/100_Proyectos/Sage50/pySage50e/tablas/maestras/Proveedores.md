---
Alias: proveedores api sage50
Creado fecha: 2023-04-12 17:07
Modificado date: miércoles 12º abril 2023 17:09:02
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
   

# Articulos   
   
   
   
   
   
   
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
   
   
   

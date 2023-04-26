---
Alias: caracteristica api sage50
Creado fecha: 2023-04-04 08:52
Modificado date: martes 4º abril 2023 08:52:42
Tags: apisage50 py
obs.html.data:
  inclusion_references:
  - 100_proyectos/sage50/pysage50e/api_pysage50e.md
---
   
CREA FAMILIA SI NO EXISTE   
   
   
# Ejemplo   
```ejemplo completo
import apiSage50
api50=apiSage50.apiSage50()
print(api50.feature())  
print("---------------------------------")  
print(api50.feature(campo))  
print("---------------------------------")  
print(api50.feature(cextraer='001'))
```
   
   
   
   
   

   
# Visión general   
   
*BIENVENIDO A LA DOCUMENTACIÓN DE API PySage50e*   
   
Esta nueva versión de nuestra Interfaz de Programación de Aplicaciones (API) representa un gran paso adelante. Es más potente y fácil de usar. Aquí encontrarás toda la orientación que necesitas para crear integraciones entre Sage50 españa y [Python version 3.10 ](https://www.python.org/downloads/release/python-3100/)     
   
# Documentacion   
   

# URL   
   
[api dll sage Sage50: Página principal](http://descargas.sage.es/Sage50/Documentacion_html/html/)   
[Estructura\_db\_Sage50.xlsx](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fsage50c.sage.es%2Fhelp50c%2FEstructura_db_Sage50.xlsx&wdOrigin=BROWSELINK)
   
   

# URL   
[Source Files and Compilation — Cython 0.29.34 documentation](https://cython.readthedocs.io/en/stable/src/userguide/source_files_and_compilation.html#compilation)   
   
   
   
   
   
# Requisitos Previos   
   

#### Python  version 3.10   
[Python 3.10.11 - April 5, 2023](https://www.python.org/downloads/release/python-31011/)   
   
>[!error] Nota importante   
>    **Python 3.10.11  no es compatible con Windows 7 o inferior   
   
   
   

#### Instalacion de la Libreria    
   
``` terminal_windows
pip install apiSage50e
```

   
   
   
   
   
   
   
   
*Debe conocer y tener acceso desde su terminal a:*   
   
#### Datos SAGE50   
   
 - Ubicacion Teminal Sage50 para el [grupo de empresa](/not_created.md)  a procesar   
 - usuario_sage50   
 - clave_sage50   
 - empresa_sage50   
   
#### Datos SQL Base datos Sage50    
   
 - Direccion servidor MSSQL[^1]   
 - Nombre Usuario  MSSQL[^1]   
 - Password MSSQL[^1]   
[^1]: (Datos generados con la configuracion habitual)   
   
# Comentarios   
Tu opinión es *importante*, dinos qué quieres ==conseguir con esta API== y te ayudamos con ello desde [Alcatic](/not_created.md).   
   
   
# Endpoints     
La API PySage50e está diseñada en torno al concepto de recursos.     
Un "recurso" está relacionado con una entidad dentro de Sage50.   
Es posible que ya conozcas estos recursos como Clientes, Articulos, Proveedores, Obras, etc.     
Los endpoints están disponibles a través de la API.    
Pueden ser acciones como recuperar una registro, actualizar un Contacto. Cada recurso tiene su propio punto final que se utiliza para recibir datos para un recurso en particular.    
Los endpoints realizan una función específica, tomando un cierto número de parámetros y devolviendo datos.     
   
# Recursos Api   
   
## Recursos Maestros   

   
   
- [Productos](./100_Proyectos/Sage50/pySage50e/tablas/maestras/Productos.md) 👍   
- [Clientes](./100_Proyectos/Sage50/pySage50e/tablas/maestras/Clientes.md) 👍   
- [Proveedores](./100_Proyectos/Sage50/pySage50e/tablas/maestras/Proveedores.md) 👍   
- [Obras](./100_Proyectos/Sage50/pySage50e/tablas/maestras/Obras.md) 👍
   
   
   
## Documentos    

   
### Ventas   
   
-  [Presupuesto Venta](/not_created.md)   
-  [Pedido Venta](./100_Proyectos/Sage50/pySage50e/documentos/Pedido%20Venta.md)   
-  [Albaran venta](./100_Proyectos/Sage50/pySage50e/documentos/Albaran%20venta.md)   
-  [Factura Venta](/not_created.md)   
   
### Compras   
   
-  [Presupuesto Compra](/not_created.md)   
-  [Pedido Compra](/not_created.md)   
-  [Albaran Compra](/not_created.md)
   
# Comienzo uso rapido   
   

# Codigo Python ejemplo    
   
``` py
import apiSage50
api50 = apiSage50.apiSage50()
```


   
   
   
# Configuracion configsql.ini   
> **obsidian-html error:** Could not find page Fichero configsql.ini.   
   
   
   
# Contrato de Uso  API   
> **obsidian-html error:** Could not find page Contrato TRIAL.
   
   
# Metodo Generador    
```
api50.feature()
'Codigo': 'xxxxxx' 
lo actualiza sino lo crear si no existe.
```
   
   
```
{'Codigo': '', 'Nombre': ''}
```
   
   
# Metodo Extraer   
```
api50.feature(cextraer='xxxxxxx')
```
   
   
# Metodo Creador / Modificador   
   
```
api50.feature(campo)
```

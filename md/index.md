---
Alias: Inicio
obs.html.data:
  inclusion_references:
  - pysage50e/1nopublicar/documentacion sage tecnica.md
  - pysage50e/comienzo rapido.md
  - pysage50e/documentos venta.md
  - pysage50e/documentos compra.md
tags:
- apisage50
- Python
---
   
# Visión general   
   
*BIENVENIDO A LA DOCUMENTACIÓN DE API PySage50e*   
   
Esta nueva versión de nuestra Interfaz de Programación de Aplicaciones (API) representa un gran paso adelante. Es más potente y fácil de usar. Aquí encontrarás toda la orientación que necesitas para crear integraciones entre Sage50 españa y [Python Release Python 3.11.3 | Python.org](https://www.python.org/downloads/release/python-3113/)     
   
# Documentacion SAGE   
   

#### URL documentacion api .net SAGE   
   
[api dll sage Sage50: Página principal](http://descargas.sage.es/Sage50/Documentacion_html/html/)
   
   
   
# Requisitos Previos   
   

#### Python  version 3.11   
[Python Release Python 3.11.3 | Python.org](https://www.python.org/downloads/release/python-3113/)   
   
   
>[!error] Nota importante   
>    **Python 3.11  no es compatible con Windows 7 o inferior   
   
   
   

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
## Tablas Maestras   
   
- [Productos](./pySage50e/Tablas/maestras/Productos.md) 👍   
- [Clientes](./pySage50e/Tablas/maestras/Clientes.md) 👍   
- [Proveedores](./pySage50e/Tablas/maestras/Proveedores.md) 👍   
- [Obras](./pySage50e/Tablas/maestras/Obras.md) 👍   
   
## Documentos    
   

   
* [Venta Presupuesto](./pySage50e/Documentos/Venta%20Presupuesto.md)   
 * [Venta Pedido](./pySage50e/Documentos/Venta%20Pedido.md)   
 * [Venta Albaran](./pySage50e/Documentos/Venta%20Albaran.md)   
 * [Venta Factura](./pySage50e/Documentos/Venta%20Factura.md)
   

   
* [Compras Presupuesto](./pySage50e/Documentos/Compras%20Presupuesto.md)   
 * [Compras Pedido](./pySage50e/Documentos/Compras%20Pedido.md)   
 * [Compras Albaran](./pySage50e/Documentos/Compras%20Albaran.md)   
 * ~Factura No diponible~
   
   
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
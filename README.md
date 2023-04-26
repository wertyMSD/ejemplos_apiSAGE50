---
tags: apisage50 PY
Alias: 
---
# Visión general

*BIENVENIDO A LA DOCUMENTACIÓN DE API PySage50e*

Esta nueva versión de nuestra Interfaz de Programación de Aplicaciones (API) representa un gran paso adelante. Es más potente y fácil de usar. Aquí encontrarás toda la orientación que necesitas para crear integraciones entre Sage50 españa y [Python version 3.11 ](https://www.python.org/downloads/release/python-3110/)  

# Documentacion

![[Documentacion SAGE tecnica#URL]]

![[Cython py#URL]]


# Requisitos Previos

![[Comienzo Rapido#Python version 3.10]]

![[Comienzo Rapido#Instalacion de la Libreria]]



*Debe conocer y tener acceso desde su terminal a:*

#### Datos SAGE50
 - Ubicacion Teminal Sage50 para el [[grupo de empresa]]  a procesar
 - usuario_sage50
 - clave_sage50
 - empresa_sage50

#### Datos SQL Base datos Sage50 
 - Direccion servidor MSSQL[^1]
 - Nombre Usuario  MSSQL[^1]
 - Password MSSQL[^1]
[^1]: (Datos generados con la configuracion habitual)

# Comentarios
Tu opinión es *importante*, dinos qué quieres ==conseguir con esta API== y te ayudamos con ello desde [[Alcatic]].


# Endpoints  
La API PySage50e está diseñada en torno al concepto de recursos.  
Un "recurso" está relacionado con una entidad dentro de Sage50.
Es posible que ya conozcas estos recursos como Clientes, Articulos, Proveedores, Obras, etc.  
Los endpoints están disponibles a través de la API. 
Pueden ser acciones como recuperar una registro, actualizar un Contacto. Cada recurso tiene su propio punto final que se utiliza para recibir datos para un recurso en particular. 
Los endpoints realizan una función específica, tomando un cierto número de parámetros y devolviendo datos.  

# Recursos Api

## Recursos Maestros
![[Recursos Maestros]]


## Documentos 
![[Recursos Documentos]]
# Comienzo uso rapido

![[Comienzo Rapido#Codigo Python ejemplo]]


# Configuracion configsql.ini
![[Fichero configsql.ini]]



# Contrato de Uso  API
![[Contrato TRIAL]]


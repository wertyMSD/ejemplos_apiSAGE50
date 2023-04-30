---
Alias: pedido ventas api sage50
Creado fecha: 2023-04-12 17:09
Tags: apisage50 py
obs.html.data:
  inclusion_references:
  - pysage50e/documentos/modelo registro documentos compra.md
---
   
Modificado : `$= dv.current().file.mtime`   
   
# Generador Modelo   
   
```
api50.pre_compra()
```
   
   
   

#### Modelo Documento   
   
```py
 documento_compra=
		 { "Cabecera":{
                  'Empresa': '','Numero': 0 , 'Serie': ''  
                  ,'Fecha': '|31-12-2023|' #opcional
                  
                  , 'Proveedor': '' #obligatorio
                  , 'Env_Cli': 0 , 'Ruta': '', 'Entrega': '|31-12-2023|'
                  , 'Vendedor': '', 'Obra': ''
                  , 'Observacio': '', 'Nota': ''
                  , 'Pronto_Pago': 0.0
                  , 'Fpag': '','Tarifa': '',"Almacen":''
                  ,'Libre_1': '' , 'Libre_2': '', 'Libre_3': ''
                            }
                ,"Lineas":[
                  {'Articulo': '1', 'Definicion': '', 'CodigoTipoIVA': ''
                 ,'PorcentajeIVA': '','Cajas': 0.0, 'Unidades': 0.0
                 ,'Talla': '','Color': '', 'Peso': 0.0, 'PuntoVerde': ''
                 ,"lote":'',"FechaCaducidad":'|31-12-2023|'
                 ,'PrecioIva': 0, 'Precio': 0, 'Dto1': 0, 'Dto2': 0
                  } #linea 1
                 ,{'Articulo': '1', 'Definicion': 'hola mundo'
                 , 'CodigoTipoIVA': '00', 'Cajas': 0.0, 'Unidades': 0.0
                 ,'Talla': '', 'Color': '', 'Peso': 0.0, 'PuntoVerde': ''
                 , "lote": '', "FechaCaducidad" : '|31-12-2023|'
                 ,'PrecioIva': 0, 'Precio': 0, 'Dto1': 0, 'Dto2': 0
                  }  # linea 2
                         ]
                ,"Porte":{
                    "Importe": 0, "Agencia": ""
                   ,"Tipo_Iva": "" ,"Tipo_Portes": 1 # 1 Debidos 2 Pagados
                   ,"Iva_Incluido": False, "Incluir_ProntoPago": False
                   ,  "Incluir_EnFactura": False
                          }
         }
```


   
   
# Uso    
```
api50.pre_compra(documento)
```
   
   
   
   
# Codigo Ejemplo   
   
[GitHub](https://github.com/wertyMSD/ejemplos_apiSAGE50/blob/master/documentos-compra.py)
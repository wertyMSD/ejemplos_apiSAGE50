import apiSage50
import json

def reg():
  ## relacion de campos
  documento_venta =		 { "Cabecera":{
                  'Empresa': '','Numero': 0 , 'Serie': ''
                  ,'Fecha': '|31-12-2023|' #opcional

                  , 'Cliente': '' #obligatorio
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
                 ,{'Articulo': '2', 'Definicion': 'hola mundo'
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
  return documento_venta



if __name__ == "__main__":
    api50 = apiSage50.apiSage50()
    modelo=api50.pre_venta()
    modelo["Cabecera"]["Cliente"]="430000000"
    modelo["Lineas"][0]["Unidades"] = 10
    modelo["Lineas"][1]["Precio"] = 100
    modelo["Porte"]["Agencia"] = "Seu"

    print("Creado Presupuesto ",api50.pre_venta(modelo))
    print("Creado Pedido ",api50.ped_venta(modelo))
    print("Creado Albaran ",api50.alb_venta(modelo))
    print("Creado Factura ",api50.fac_venta(modelo))



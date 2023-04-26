import json

import apiSage50

if __name__ == "__main__":
    api50 = apiSage50.apiSage50()
    # api50.ldebugcamposdll = True
    print(api50.supplier())

    pre={'Cabecera': { 'Fecha': '|04-04-2023|', 'Cliente': '430002148', 'Env_Cli': 0,
                   'Entrega': '|05-05-2023|', 'Nota': 'hola nota',  'Pronto_Pago': 0, 'Observacio': 'Hola observacion',
                    'Libre_1': '1', 'Libre_2': '2', 'Libre_3': '3',
                    }, 'lineas': [

          {'Articulo':  '1',  'Definicion': 'ascasas', 'Unidades': 50.0 ,'Precio': 101 }
          # {'Articulo': '2',  'Definicion': 'ascasas545', 'Unidades': 1, 'Precio': 100,'Dto1': 10, 'Dto2': 20,"lote":"2"}
         ]
       ,"Porte":{
                    "Importe": 100, "Agencia": "sex"
                   # ,"Tipo_Iva": "03","Tipo_Portes": 2,"Iva_Incluido": False, "Incluir_ProntoPago": True,  "Incluir_EnFactura": False
                          }}

    compras = {'Cabecera': {"numero":'Ho1289','Fecha': '|04-04-2023|', 'Cliente': '410000036', 'Env_Cli': 0,
                        'Entrega': '|05-05-2023|', 'Nota': 'hola nota', 'Pronto_Pago': 0,
                        'Observacio': 'Hola observacion',
                        'Libre_1': '1', 'Libre_2': '2', 'Libre_3': '3',
                        }, 'lineas': [

        {'Articulo': '1', 'Definicion': 'ascasas', 'Unidades': 50.0, 'Precio': 101},
        {'Articulo': '2',  'Definicion': 'ascasas545', 'Unidades': 1, 'Precio': 100,'Dto1': 10, 'Dto2': 20,"lote":"3"}
    ]
        , "Porte": {
            "Importe": 100, "Agencia": "sex"
            # ,"Tipo_Iva": "03","Tipo_Portes": 2,"Iva_Incluido": False, "Incluir_ProntoPago": True,  "Incluir_EnFactura": False
        }}

    api50.cierre()

    # print(api50.pre_venta(pre))
    # print(api50.ped_venta(pre))
    # /print(api50.alb_venta(pre))



    # print("alb",api50.alb_venta(pre))
    # print("fac",api50.fac_venta(pre))
    # print("pre",api50.pre_venta(pre))
    # print("ped",api50.ped_venta(pre))


    # print("alb",api50.alb_compra(compras))
    # print("fac",api50.fac_compra(compras))
    # print("pre",api50.pre_compra(compras))
    # print("ped",api50.ped_compra(compras))
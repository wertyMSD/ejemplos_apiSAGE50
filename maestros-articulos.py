import apiSage50
import json

def reg():
  ## relacion de campos

  '''
     articulo={'Codigo': 'prueba', 'Nombre': 'prueba nombre', 'Abrev': '', 'Familia': '001', 'Marca': '', 'Minimo': 0.0, 'Maximo': 0.0, 'Aviso': False,
     'Baja': False, 'Tipo_Iva': '03', 'Retencion': '', 'Iva_Inc': False, 'Cost_Ult1': 0.0, 'Fecha_Ult': '|31-12-2023|',
     'Ult_Fecha': '|31-12-2023|', 'Pmcom1': 0.0, 'Imagen': '', 'Carac': '', 'Fechaalta': '|31-12-2023|',
     'Fechabaja': '|31-12-2023|', 'Ubicacion': '', 'Medidas': '', 'Peso': '', 'Litros': '', 'Observacio': '',
     'Unicaja': 0.0, 'Desglose': 0, 'Aranceles': 0.0, 'Definicion2': '', 'Subfamilia': '', 'Internet': False,
     'Pverde': False, 'P_Importe': 0.0, 'P_Tan': 0, 'Lcolor': False, 'Margen': 0.0, 'Tcp': '', 'Venserie': False,
     'Puntos': 0.0, 'Des_Esc': False, 'Tipo_Art': 0, 'Modelo': '', 'Cocina': False, 'Art_Impues': '', 'Nombre2': '',
     'Color_Art': '', 'Tipo_Pvp': 0.0, 'Cost_Escan': 0, 'Tipo_Escan': 0, 'Art_Canon': False, 'Actua_Colo': 0,
     'Fact_Arepe': False, 'Garantia': 0, 'Alquiler': False, 'Orden': 0, 'C_Ent': '', 'Cn8': '', 'Ivalot': False,
     'Artant': '', 'Reportetiq': '', 'Isp': False, 'Grupoiva': 0, 'Suplidos': False, 'Csuplido': '', 'Tipo': 0,
     'Contrapar': '', 'Contrapco': '', 'Segurointr': False, 'Codintradi': '', '_Ofertas#Fecha_In': '|31-12-2023|',
     '_Ofertas#Fecha_Fin': '|31-12-2023|', '_Ofertas#Pvp': 0.0, '_Ofertas#Regalo': 0, '_Ofertas#Descuento': 0.0,
     '_Ofertas#Desde': 0.0, '_Ofertas#Hasta': 0.0, '_Ofertas#Moneda': '', '_Ofertas#Cajas': False,
     '_Ofertas#Tarifa': '', '_Ofertas#Cliente': '', '_Ofertas#Talla': '', '_Ofertas#Color': '', '_Ofertas#Tallare': '',
     '_Ofertas#Colore': '', '_Ofertas#Hora_Ini': '', '_Ofertas#Hora_Fin': '', '_Ofertas#Unidades': False,
     '_Precios#Tarifa': '', '_Precios#Pvp': 0.0, '_Precios#Margen': 0.0, '_Precios#Tcp': '',
     '_Precios#Fechaini': '|31-12-2023|', '_Precios#Fechafin': '|31-12-2023|', '_Referencias#Articulo': '',
     '_Referencias#Proveedor': '', '_Referencias#Referencia': '', '_Referencias#Pcompra': 0.0, '_Referencias#Dto1': 0.0,
     '_Referencias#Dto2': 0.0, '_Referencias#Fecha_Ult': '|31-12-2023|', '_Referencias#Moneda': '',
     '_Referencias#Predet': False, '_Referencias#Color': '', '_Referencias#Talla': '', '_Referencias#Dto5': 0.0,
     '_Referencias#Cambiar': False, '_Referencias#Gasto': 0.0, '_Referencias#Notas': '', '_Referencias#Coste': 0.0,
     '_Referencias#Cambio': 0.0, '_StockMaxMinAlmacen#Almacen': '', '_StockMaxMinAlmacen#Color': '',
     '_StockMaxMinAlmacen#Maximo': 0.0, '_StockMaxMinAlmacen#Minimo': 0.0, '_StockMaxMinAlmacen#Talla': '',
     '_Imagenes#Imagen': '', '_ListCamposAdicionales#Campo': '', '_ListCamposAdicionales#Valor': '',
     '_Escandallos#Articulo': '', '_Escandallos#Componente': '', '_Escandallos#Unidades': 0.0, '_Escandallos#Pvp': 0.0,
     '_Escandallos#Valorado': False, '_Escandallos#Tarifa': '', '_Escandallos#Linia': 0, '_Escandallos#Pmanual': False,
     '_Escandallos#Coste': 0.0, '_Escandallos#Fecha': '|31-12-2023|', '_Escandallos#Anotacion': '',
     '_Escandallos#Libre_1': '', '_Escandallos#Libre_2': '', '_Escandallos#Libre_3': '',
     '_Escandallos#Noactcostp': False, '_Escandallos#Talla': '', '_Escandallos#Color': '', '_Escandallos#Costerec': 0.0,
     '_Idiomas#Idioma': '', '_Idiomas#Definicion': ''}
  '''


if __name__ == "__main__":
    api50 = apiSage50.apiSage50()



    ''''
    ALTA
    si existe lo actualiza con lo nuevo valores.
    =============== 
    Campos  minimo:
             Codigo
           Familias 
    Codigo Tipo IVA     
    '''


    print("Alta con campos minimos")
    articulominimo = {'Codigo': 'prueba', 'Nombre': 'prueba nombre', 'Familia': '01',  'Tipo_Iva': '03'}
    print(api50.product(articulominimo))

    '''
    Tablas relacionadas
    '''
    print("Alta oferta _Ofertas")
    articulo_tablarelacionada= {'Codigo': 'prueba', '_Ofertas#Tarifa': 'TD',}
    print(api50.product(articulo_tablarelacionada))

    print("Alta precios _Precios")
    articulo_tablarelacionada= {'Codigo': 'prueba', '_Precios#Tarifa': 'TD', '_Precios#Pvp': 100 }
    print(api50.product(articulo_tablarelacionada))


    print("Alta tarifa_proveedores _Referencias")
    articulo_tablarelacionada= {'Codigo': 'prueba',  '_Referencias#Proveedor': '400000001', '_Referencias#Referencia': 'codiprovee', '_Referencias#Pcompra': 10}
    print(api50.product(articulo_tablarelacionada))

    print("Alta Stock Minimo_Maximo _StockMaxMinAlmacen")
    articulo_tablarelacionada= {'Codigo': 'prueba',  "_StockMaxMinAlmacen#almacen": "01", "_StockMaxMinAlmacen#Maximo": 100.0, '_StockMaxMinAlmacen#Minimo': 10.0,}
    print(api50.product(articulo_tablarelacionada))

    print("Alta Imagenes/Documentos _Imagenes")
    articulo_tablarelacionada= {'Codigo': 'prueba',  '_Imagenes#Imagen': 'E:\@github\ejemplos_apiSAGE50\Articulo.txt'}
    print(api50.product(articulo_tablarelacionada))

    print("Alta campos libres _ListCamposAdicionales")
    articulo_tablarelacionada= {'Codigo': 'prueba',  '_ListCamposAdicionales#Campo': '001' , '_ListCamposAdicionales#Valor': 'test valor'   }
    print(api50.product(articulo_tablarelacionada))

    print("Alta Escandadallos _Escandallo") # todo por hacer
    articulo_tablarelacionada = {'Codigo': 'prueba', '_Escandallos#Componente': '1' ,'_Escandallos#Unidades': 10 ,'_Escandallos#Campo':"hola"  }
    print(api50.product(articulo_tablarelacionada))

    print("Alta Idioma _Idiomas ")
    articulo_tablarelacionada = {'Codigo': 'prueba','_Idiomas#Idioma': 'ING'  , '_Idiomas#Definicion': 'Test'}
    print(api50.product(articulo_tablarelacionada))

    ''''
    LISTADO 
    Devuelve lista registro que lo cumple condicion. Si esta vacion son todos los registros 
    '''

    lista=api50.product(wlista="Familia='01'")
    print(lista)
    ''''
        Extrae  
        Devuelve JSON con las registro en la tablas relacionas
    '''

    if len(lista)>0:
        for reg  in lista[0]:
            ajson=api50.product(cextraer=reg["Codigo"])

        print(json.loads(ajson[0]))


    ## genera los campos disponibles
    #
    # print(api50.product())

    ## ver documento Articulo.txt
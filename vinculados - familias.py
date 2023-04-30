import apiSage50
import json

def reg():
    '''
      {'Codigo': '', 'Nombre': '', 'Cta_Compra': '', 'Cta_Venta': '', 'Cod_Intra': '', 'Margen': 0.0, 'Tcp': '',
     'Descuen': 0.0, 'Orden': 0, 'Junfra': False, 'Vertpv': False, 'Codintradi': '', '_Descuentos#Familia': '',
     '_Descuentos#Fecha_Fin': '', '_Descuentos#Fecha_Ini': '', '_Descuentos#Tan': 0.0, '_Descuentos#Uni_Fin': 0.0,
     '_Descuentos#Uni_Ini': 0.0}

  
    '''
  


if __name__ == "__main__":
    api50 = apiSage50.apiSage50()


    ''''
    ALTA
    si existe lo actualiza con lo nuevo valores.
    =============== 
    Campos  minimo:
             Codigo
             Nombre
      
    '''
    

    print("Alta con campos minimos")
    familiaminimo = { 'Codigo': 'A1','Nombre': 'prueba nombre'}
    familiaminimo =api50.family(familiaminimo)
    print(familiaminimo)


    '''
    Tablas relacionadas
    '''
    print("Alta Descuento clientes por familia")
    familia_tablarelacionada= {'Codigo': familiaminimo[0], '_Descuentos#tan':  10}
    print(api50.family(familia_tablarelacionada))




    ''''
    LISTADO 
    Devuelve lista registro que lo cumple condición. Si esta vacio son todos los registros 
    '''
    print("Listado para procesar")
    lista=api50.family(wlista="")
    print(lista)
    ''''
        Extrae  
        Devuelve JSON con las registro en la tablas relacionas
    '''
    if lista[0]==None:
        lista=""


    if len(lista)>0:
        for reg  in lista[0]:
            ajson=api50.family(cextraer=reg["Codigo"])

        print(json.loads(ajson[0]))


    ##genera los campos disponibles

    print(api50.family())

    ## ver documento familia.txt


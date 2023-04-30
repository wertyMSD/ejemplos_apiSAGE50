import apiSage50
import json

def reg():
    '''
        {'Codigo': '', 'Nombre': '', 'Familia': '', 'Margen': 0.0, 'Tcp': '', 'Vertpv': False, '_Descuentos#Fecha_Fin': '',
     '_Descuentos#Fecha_Ini': '', '_Descuentos#Tan': 0.0, '_Descuentos#Uni_Fin': 0.0, '_Descuentos#Uni_Ini': 0.0}

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
             Familia
      
    '''
    

    print("Alta con campos minimos")
    subfamiliaminimo = { 'Codigo': 'A100','Familia': '00','Nombre': 'prueba nombre'}
    subfamiliaminimo =api50.subfamily(subfamiliaminimo)
    print(subfamiliaminimo)

    '''
    Tablas relacionadas
    '''
    print("Alta Descuento clientes por subfamilia")
    subfamilia_tablarelacionada= {'Codigo': subfamiliaminimo[0],  '_Descuentos#tan': 10.0 }
    print(api50.subfamily(subfamilia_tablarelacionada))




    ''''
    LISTADO 
    Devuelve lista registro que lo cumple condición. Si esta vacio son todos los registros 
    '''
    print("Listado para procesar")
    lista=api50.subfamily(wlista="")
    print(lista)
    ''''
        Extrae  
        Devuelve JSON con las registro en la tablas relacionas
    '''
    if lista[0]==None:
        lista=""


    if len(lista)>0:
        for reg  in lista[0]:
            ajson=api50.subfamily(cextraer=reg["Codigo"])

        print(json.loads(ajson[0]))


    ##genera los campos disponibles

    print(api50.subfamily())

    ## ver documento subfamilia.txt
    {'Codigo': '', 'Nombre': '', 'Familia': '', 'Margen': 0.0, 'Tcp': '', 'Vertpv': False, '_Descuentos#Fecha_Fin': '',
     '_Descuentos#Fecha_Ini': '', '_Descuentos#Tan': 0.0, '_Descuentos#Uni_Fin': 0.0, '_Descuentos#Uni_Ini': 0.0}



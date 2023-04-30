import apiSage50
import json

def reg():
    '''
    {'Codigo': '', 'Nombre': '', 'Report': '', 'Direccion': '', 'Poblacion': '', 'Codpost': '', 'Provincia': '',
         'Pais': '', 'Telefon': '', 'Email': '', 'Http': ''}

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
    agencia_transporte_minimo = { 'Codigo': 'A1','Nombre': 'prueba nombre'}
    agencia_transporte_minimo =api50.agency(agencia_transporte_minimo)
    print(agencia_transporte_minimo)




    ''''
    LISTADO 
    Devuelve lista registro que lo cumple condición. Si esta vació son todos los registros 
    '''
    print("Listado para procesar")
    lista=api50.agency(wlista="")
    print(lista)
    ''''
        Extrae  
        Devuelve JSON con las registro en la tablas relacionas
    '''
    if lista[0]==None:
        lista=""


    if len(lista)>0:
        for reg  in lista[0]:
            ajson=api50.agency(cextraer=reg["Codigo"])

        print(json.loads(ajson[0]))


    ##genera los campos disponibles

    print(api50.agency())

    ## ver documento agencia_transporte_.txt


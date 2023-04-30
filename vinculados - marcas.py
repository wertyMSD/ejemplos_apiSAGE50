import apiSage50
import json

def reg():
    '''
    {'Codigo': '', 'Nombre': '', 'Margen': 0.0, 'Tcp': '', 'Descuen': 0.0, 'Vertpv': False}
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
    marcaminimo = { 'Codigo': 'A1','Nombre': 'prueba nombre'}
    marcaminimo =api50.mark(marcaminimo)
    print(marcaminimo)




    ''''
    LISTADO 
    Devuelve lista registro que lo cumple condición. Si esta vació son todos los registros 
    '''
    print("Listado para procesar")
    lista=api50.mark(wlista="")
    print(lista)
    ''''
        Extrae  
        Devuelve JSON con las registro en la tablas relacionas
    '''
    if lista[0]==None:
        lista=""


    if len(lista)>0:
        for reg  in lista[0]:
            ajson=api50.mark(cextraer=reg["Codigo"])

        print(json.loads(ajson[0]))


    ##genera los campos disponibles

    print(api50.mark())

    ## ver documento marca.txt


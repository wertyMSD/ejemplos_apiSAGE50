import apiSage50
import json

def reg():
    '''
      {'Codigo': '', 'Nombre': '', 'Rec_Finan': 0.0, 'Grupo': '', 'Efectivo': False, 'Csb34': 0, 'Dias_Riesgo': 0,
     'Contado': False, 'Fraefpag': '', 'Domibanc': False, 'Girmescomp': False}


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
    formapagominimo = { 'Codigo': 'A1','Nombre': 'prueba nombre'}
    formapagominimo =api50.fp(formapagominimo)
    print(formapagominimo)





    ''''
    LISTADO 
    Devuelve lista registro que lo cumple condición. Si esta vacio son todos los registros 
    '''
    print("Listado para procesar")
    lista=api50.fp(wlista="Efectivo!=1")
    print(lista)
    ''''
        Extrae  
        Devuelve JSON con las registro en la tablas relacionas
    '''
    if lista[0]==None:
        lista=""

    if len(lista)>0:
        for reg  in lista[0]:
            ajson=api50.fp(cextraer=reg["Codigo"])

        print(json.loads(ajson[0]))


    ##genera los campos disponibles

    print(api50.fp())

    ## ver documento formapago.txt


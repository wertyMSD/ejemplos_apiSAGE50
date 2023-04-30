import apiSage50
import json

def reg():
    '''
    ## relacion de campos
    {'Codigo': '', 'Nombre': '', 'Comision': 0.0, 'Dni': '', 'Telefon': '', 'Mobil': '', 'Fax': '', 'Direccion': '',
     'Poblacion': '', 'Codpost': '', 'Observacio': '', 'Provincia': '', 'Foto': '', 'Com_Dto': False, 'Ctacobro': '',
     'Pais': '', 'Empresa': '', 'Matricula': '', 'Menoscomi': False, 'Ctacobro2': '', 'Almauto': '', 'Libre_1': '',
     'Libre_2': '', 'Libre_3': '', 'Clavepol': '', 'Poblacerp': '', 'Delegerp': '', 'Provinerp': '', 'Email': '',
     'Eticomu': '', 'Fbloqnocar': '|31-12-2023|', 'Fbloqnoema': '|31-12-2023|', 'Nocomucar': False, 'Nocomuema': False,
     'Nocomuobs': '', '_Comisiones#Articulo': '', '_Comisiones#Familia': '', '_Comisiones#Comision': 0.0,
     '_Comisiones#Prima': 0.0, '_Comisiones#Imp_Uni': 0.0, '_Comisiones#Moneda': '', '_Comisiones#Dto': 0.0,
     '_Comisiones#Libre_1': '', '_Comisiones#Libre_2': '', '_Comisiones#Libre_3': '', '_Comisiones#Cliente': '',
     '_Comisiones#Subfamilia': ''}
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
    vendedorminimo = { 'Codigo': 'A1','Nombre': 'prueba nombre'}
    vendedorminimo =api50.salesman(vendedorminimo)
    print(vendedorminimo)


    '''
    Tablas relacionadas
    '''
    print("Alta Contactos _Comisioness")
    vendedor_tablarelacionada= {'Codigo': vendedorminimo[0],  '_TRelDescuen#Familia': '43' , '_TRelDescuen#Subfamilia': '001',  '_TRelDescuen#Dto1':  10}
    print(api50.salesman(vendedor_tablarelacionada))




    ''''
    LISTADO 
    Devuelve lista registro que lo cumple condición. Si esta vacio son todos los registros 
    '''
    print("Listado para procesar")
    lista=api50.salesman(wlista="Comision>0")
    print(lista)
    ''''
        Extrae  
        Devuelve JSON con las registro en la tablas relacionas
    '''
    if lista[0]==None:
        lista=""


    if len(lista)>0:
        for reg  in lista[0]:
            ajson=api50.salesman(cextraer=reg["Codigo"])

        print(json.loads(ajson[0]))


    ##genera los campos disponibles

    print(api50.salesman())

    ## ver documento vendedor.txt


import apiSage50
import json

def reg():
  ## relacion de campos

  '''
        {'Codigo': '', 'Env_Pro': 0, 'Nombre': '', 'Nombre2': '', 'Direccion': '', 'Codpost': '', 'Poblacion': '',
     'Provincia': '', 'Cif': '', 'Banco': '', 'Fpag': '', 'Pronto': 0.0, 'Tipo_Iva': '', 'Recargo': False,
     'Comunitari': 0, 'Retencion': False, 'Modo_Ret': False, 'Tipo_Ret': '', 'Email': '', 'Http': '', 'Dias_Ent': 0,
     'Observacio': '', 'Descu1': 0.0, 'Descu2': 0.0, 'Idioma': '', 'Pais': '', 'Diapag': 0.0, 'Diapag2': 0.0,
     'Mod349': False, 'Contrapar': '', 'Idioma_Imp': '', 'C_Ent': '', 'Cod_Agrup': '', 'Comision': 0.0, 'Csb': False,
     'Mensaje': '', 'Nocomusms': False, 'Nocomuema': False, 'Nocomucar': False, 'Fbloqnosms': '|31-12-2023|',
     'Fbloqnoema': '|31-12-2023|', 'Fbloqnocar': '|31-12-2023|', 'Nocomuobs': '', 'Regcaja': False, 'Recc': False,
     'Recc2': False, 'Proveederp': '', 'Ctaerp': '', 'Nombre3Erp': '', 'Poblacerp': '', 'Provinerp': '', 'Territerp': 0,
     'Direcc2Erp': '', 'Delegerp': '', 'Canal': '', 'Facebook': '', 'Twitter': '', 'Skype': '', 'Cambio': 0.0,
     'Fec_Cam': '|31-12-2023|', 'Excluir349': False, 'Refer_Cat': '', 'Eticomu': '', '_TRelContacTelefs#Proveedor': '',
     '_TRelContacTelefs#Predet': False, '_TRelContacTelefs#Persona': '', '_TRelContacTelefs#Cargo': '',
     '_TRelContacTelefs#Telefono': '', '_TRelContacTelefs#Observa': '', '_TRelContacTelefs#Email': '',
     '_TRelContacTelefs#Skype': '', '_TRelContacTelefs#Facebook': '', '_TRelContacTelefs#Twitter': '',
     '_TRelContacTelefs#Lincontpro': 0, '_TRelContacTelefs#Lintelfpro': 0, '_TRelContacTelefs#Tipo': 0,
     '_TRelDatosBancarios#Codigo': 0, '_TRelDatosBancarios#Proveedor': '', '_TRelDatosBancarios#Banco': '',
     '_TRelDatosBancarios#Direccion': '', '_TRelDatosBancarios#Codpos': '', '_TRelDatosBancarios#Poblacion': '',
     '_TRelDatosBancarios#Provincia': '', '_TRelDatosBancarios#Ctabanco': '', '_TRelDatosBancarios#Ctasucur': '',
     '_TRelDatosBancarios#Digcon': '', '_TRelDatosBancarios#Ctacuenta': '', '_TRelDatosBancarios#Iban': '',
     '_TRelDatosBancarios#Cuentaiban': '', '_TRelDatosBancarios#Swift': '', '_TRelDescuen#Articulo': '',
     '_TRelDescuen#Familia': '', '_TRelDescuen#Marca': '', '_TRelDescuen#Subfam': '', '_TRelDescuen#Definicion': '',
     '_TRelDescuen#Dto1': 0.0, '_TRelDescuen#Dto2': 0.0, '_TRelDescuen#Dto3': 0.0, '_TRelDescuen#Dto4': 0.0,
     '_TRelDescuen#Dto5': 0.0, '_TRelDescuen#Dto6': 0.0, '_TRelDescuen#Fecha_Ini': '|31-12-2023|',
     '_TRelDescuen#Fecha_Fin': '|31-12-2023|', '_TRelDescuen#Pvp': 0.0, '_TRelDescuen#Moneda': '',
     '_TRelDescuen#Uni_Min': 0.0, '_TRelDescuen#Uni_Max': 0.0, '_TRelDirecciones#Nombre': '',
     '_TRelDirecciones#Direccion': '', '_TRelDirecciones#Codpos': '', '_TRelDirecciones#Poblacion': '',
     '_TRelDirecciones#Provincia': '', '_TRelDirecciones#Tipo': 0, '_TRelDirecciones#Horario': '',
     '_TRelDirecciones#Pais': '', '_TRelDirecciones#Fax': '', '_TRelDirecciones#Telefono': '',
     '_TRelImagenes#Imagen': '', '_ListCamposAdicionales#Campo': '', '_ListCamposAdicionales#Valor': ''}

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
    proveedorminimo = { 'Nombre': 'prueba Proveedor'}
    proveedorminimo=api50.supplier(proveedorminimo)
    print(proveedorminimo)

    '''
    Tablas relacionadas
    '''
    print("Alta Contactos _TRelContacTelefs")
    proveedor_tablarelacionada = {'Codigo': proveedorminimo[0], '_TRelContacTelefs#Persona': 'antonio'}
    print(api50.supplier(proveedor_tablarelacionada))

    print("Alta datos bancarios TRelDatosBancarios")
    proveedor_tablarelacionada = {'Codigo': proveedorminimo[0], '_TRelDatosBancarios#Cuentaiban': '210019198221211'}
    print(api50.supplier(proveedor_tablarelacionada))

    print("Alta politica Descuentos TRelDescuen")
    proveedor_tablarelacionada = {'Codigo': proveedorminimo[0], '_TRelDescuen#Familia': '00', '_TRelDescuen#Dto1': 10}
    print(api50.supplier(proveedor_tablarelacionada))

    print("Alta otras direcciones TRelDirecciones")
    proveedor_tablarelacionada = {'Codigo': proveedorminimo[0], '_TRelDirecciones#Nombre': 'otra direccion',
                                '_TRelDirecciones#Direccion': 'direcccion entrega'}
    print(api50.supplier(proveedor_tablarelacionada))

    print("Alta Imagenes/Documentos _Imagenes")
    proveedor_tablarelacionada = {'Codigo': proveedorminimo[0], '_TRelImagenes#Imagen': 'E:\@github\ejemplos_apiSAGE50\proveedor.txt'}
    print(api50.supplier(proveedor_tablarelacionada))

    print("Alta campos libres _ListCamposAdicionales")
    proveedor_tablarelacionada = {'Codigo': proveedorminimo[0], '_ListCamposAdicionales#Campo': '001',
                                '_ListCamposAdicionales#Valor': 'test valor'}
    print(api50.supplier(proveedor_tablarelacionada))

    # print("Alta actividades_o") # todo por hacer
    # proveedor_tablarelacionada = {'Codigo': 'prueba', '_Escandallos#Componente': '1' ,'_Escandallos#Unidades': 10 ,'_Escandallos#Campo':"hola"  }
    # print(api50.customer(proveedor_tablarelacionada))

    '''
    LISTADO 
    Devuelve lista registro que lo cumple condicion. Si esta vacion son todos los registros 
    '''

    lista=api50.supplier(wlista="codigo>'410000169'")
    print(lista)
    ''''
        Extrae  
        Devuelve JSON con las registro en la tablas relacionas
    '''

    if len(lista)>0:
        for reg  in lista[0]:
            ajson=api50.supplier(cextraer=reg["Codigo"])

        print(json.loads(ajson[0]))


    ##genera los campos disponibles

    print(api50.supplier())

    ## ver documento proveedor.txt


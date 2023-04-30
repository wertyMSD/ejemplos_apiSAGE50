import apiSage50
import json

def reg():
  ## relacion de campos

  '''
  {'Codigo': '', 'Cif': '', 'Nombre': '', 'Nombre2': '', 'Direccion': '', 'Codpost': '', 'Poblacion': '',
     'Provincia': '', 'Pais': '', 'Ruta': '', 'Vendedor': '', 'Tarifa': '', 'Lin_Des': '', 'Valor_Alb': False,
     'Tipofac': '', 'Copia_Fra': 0, 'Idioma': '', 'Credito': 0.0, 'Descu1': 0.0, 'Descu2': 0.0, 'Pronto': 0.0,
     'Diapag': 0, 'Diapag2': 0, 'Fpag': '', 'Tipo_Iva': '', 'Recargo': False, 'Comunitari': 0, 'Retencion': False,
     'Modo_Ret': False, 'Tipo_Ret': '', 'Observacio': '', 'Email': '', 'Http': '', 'Refundir': False, 'Env_Cli': 0,
     'Albafra': False, 'Csb': False, 'Cia_Cred': '', 'Operacio': '', 'Idioma_Imp': '', 'Agencia': '', 'Bloq_Ven': False,
     'Lim_Mon': 0, 'Portes': '', 'Portcomp': 0.0, 'F_Alta': '|31-12-2023|', 'Oferta': False, 'Bloq_Cli': False,
     'Fecha_Baj': '|31-12-2023|', 'Contrapar': '', 'Zona': '', 'Posicion': 0.0, 'Mensaje': '', 'Pregvac': False,
     'Valportes': 0.0, 'Fraped': False, 'Val_Punt': 0.0, 'Contado': False, 'C_Ent': '', 'Dia1': False, 'Dia2': False,
     'Dia3': False, 'Dia4': False, 'Dia5': False, 'Dia6': False, 'Dia7': False, 'Es_Grupo': False, 'Clifinal': '',
     'Pverde': False, 'Tipcredit': '', 'Recarfin': 0.0, 'Retnofisc': False, 'Tpcretnofi': 0.0, 'Libre1': '',
     'Modretnofi': 0, 'Email_F': '', 'Tipo_Cli': 0, 'Fraesi': False, 'Autotipdoc': '', 'Bloqalbvta': False,
     'Bloqpedvta': False, 'Bloqprevta': False, 'Bloqdepvta': False, 'Nocomusms': False, 'Nocomuema': False,
     'Nocomucar': False, 'Fbloqnosms': '|31-12-2023|', 'Fbloqnoema': '|31-12-2023|', 'Fbloqnocar': '|31-12-2023|',
     'Nocomuobs': '', 'Regcaja': False, 'Clienteerp': '', 'Recc': False, 'Ctaerp': '', 'Nombre3Erp': '',
     'Poblacerp': '', 'Provinerp': '', 'Territerp': 0, 'Direcc2Erp': '', 'Delegerp': '', 'Isp': False, 'Canal': '',
     'Facebook': '', 'Twitter': '', 'Skype': '', 'Banco_Prev': '', 'Cambio': 0.0, 'Fec_Cam': '|31-12-2023|',
     'Plefact': '', 'Dire': '', 'Excluir349': False, 'Refer_Cat': '', 'Letdefven': '', 'Letdefrect': '', 'Eticomu': '',
     '_TRelContacTelefs#Predet': False, '_TRelContacTelefs#Persona': '', '_TRelContacTelefs#Cargo': '',
     '_TRelContacTelefs#Telefono': '', '_TRelContacTelefs#Observa': '', '_TRelContacTelefs#Email': '',
     '_TRelContacTelefs#Skype': '', '_TRelContacTelefs#Facebook': '', '_TRelContacTelefs#Twitter': '',
     '_TRelContacTelefs#Lincontcli': 0, '_TRelContacTelefs#Lintelfcli': 0, '_TRelContacTelefs#Tipo': 0,
     '_TRelDatosBancarios#Codigo': 0, '_TRelDatosBancarios#Banco': '', '_TRelDatosBancarios#Direccion': '',
     '_TRelDatosBancarios#Codpos': '', '_TRelDatosBancarios#Poblacion': '', '_TRelDatosBancarios#Provincia': '',
     '_TRelDatosBancarios#Ctabanco': '', '_TRelDatosBancarios#Ctasucur': '', '_TRelDatosBancarios#Digcon': '',
     '_TRelDatosBancarios#Ctacuenta': '', '_TRelDatosBancarios#Iban': '', '_TRelDatosBancarios#Cuentaiban': '',
     '_TRelDatosBancarios#Swift': '', '_TRelDescuen#Articulo': '', '_TRelDescuen#Familia': '', '_TRelDescuen#Dto1': 0.0,
     '_TRelDescuen#Dto2': 0.0, '_TRelDescuen#Dto3': 0.0, '_TRelDescuen#Fecha_In': '|31-12-2023|',
     '_TRelDescuen#Fecha_Fin': '|31-12-2023|', '_TRelDescuen#Linia': 0, '_TRelDescuen#Pvp': 0.0,
     '_TRelDescuen#Moneda': '', '_TRelDescuen#Subfamilia': '', '_TRelDescuen#Obra': '', '_TRelDescuen#Marca': '',
     '_TRelDescuen#Talla': '', '_TRelDescuen#Color': '', '_TRelDescuen#Uni_Min': 0.0, '_TRelDescuen#Uni_Max': 0.0,
     '_TRelDirecciones#Nombre': '', '_TRelDirecciones#Direccion': '', '_TRelDirecciones#Codpos': '',
     '_TRelDirecciones#Poblacion': '', '_TRelDirecciones#Provincia': '', '_TRelDirecciones#Horario': '',
     '_TRelDirecciones#Telefono': '', '_TRelDirecciones#Fax': '', '_TRelDirecciones#Pais': '',
     '_TRelDirecciones#Tipo': 0, '_TRelDirecciones#Libre_1': '', '_TRelDirecciones#Libre_2': '',
     '_TRelDirecciones#Poblacerp': '', '_TRelDirecciones#Provinerp': '', '_TRelDirecciones#Direcc2Erp': '',
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
    clienteminimo = { 'Nombre': 'prueba nombre'}
    clienteminimo =api50.customer(clienteminimo)
    print(clienteminimo)

    '''
    Tablas relacionadas
    '''
    print("Alta Contactos _TRelContacTelefs")
    cliente_tablarelacionada= {'Codigo': clienteminimo[0], '_TRelContacTelefs#Persona': 'Pepe','_TRelContacTelefs#Telefono': '600573', }
    print(api50.customer(cliente_tablarelacionada))

    print("Alta datos bancarios TRelDatosBancarios")
    cliente_tablarelacionada= {'Codigo': clienteminimo[0], '_TRelDatosBancarios#Cuentaiban': '21001919980200007777','_TRelDatosBancarios#iban': 'ES40'   }
    print(api50.customer(cliente_tablarelacionada))


    print("Alta politica Descuentos TRelDescuen")
    cliente_tablarelacionada= {'Codigo': clienteminimo[0],  '_TRelDescuen#Familia': '43' , '_TRelDescuen#Subfamilia': '001',  '_TRelDescuen#Dto1':  10}
    print(api50.customer(cliente_tablarelacionada))


    print("Alta otras direcciones TRelDirecciones")
    cliente_tablarelacionada= {'Codigo': clienteminimo[0],  '_TRelDirecciones#Nombre': 'otra direccion1 emvop 3' , '_TRelDirecciones#Direccion': 'direcccion entrega 3'   }
    print(api50.customer(cliente_tablarelacionada))

    print("Alta Imagenes/Documentos _Imagenes")
    cliente_tablarelacionada= {'Codigo': clienteminimo[0],  '_TRelImagenes#Imagen': 'E:\@github\ejemplos_apiSAGE50\cliente.txt'}
    print(api50.customer(cliente_tablarelacionada))

    print("Alta campos libres _ListCamposAdicionales")
    cliente_tablarelacionada= {'Codigo': clienteminimo[0],  '_ListCamposAdicionales#Campo': '002' , '_ListCamposAdicionales#Valor': 'test valor'   }
    print(api50.customer(cliente_tablarelacionada))

    # print("Alta actividades_o") # todo por hacer
    # cliente_tablarelacionada = {'Codigo': clienteminimo[0], '_Escandallos#Componente': '1' ,'_Escandallos#Unidades': 10 ,'_Escandallos#Campo':"hola"  }
    # print(api50.customer(cliente_tablarelacionada))


    ''''
    LISTADO 
    Devuelve lista registro que lo cumple condicion. Si esta vacion son todos los registros 
    '''
    print("Listado para procesar")
    lista=api50.customer(wlista="codigo>'440000000'")
    print(lista)
    ''''
        Extrae  
        Devuelve JSON con las registro en la tablas relacionas
    '''

    if len(lista)>0:
        for reg  in lista[0]:
            ajson=api50.customer(cextraer=reg["Codigo"])

        print(json.loads(ajson[0]))


    ##genera los campos disponibles

    print(api50.customer())

    ## ver documento cliente.txt


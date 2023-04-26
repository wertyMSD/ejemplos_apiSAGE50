---
{}
---
   
Tener en cuenta:   
   
[linea adicional con la descripcion larga](../../../../100_Proyectos/Sage50/pySage50e/documentos/linea%20adicional%20con%20la%20descripcion%20larga.md)   
   
   
   
   
   
		//Init contador   
		Contador = 0   
		SI HExecuteRequeteSQL(rqCabeceras,cstNomConexioiGes,hRequêteSansCorrection,"SELECT * FROM Cabeceras WHERE Tipo='A'") ALORS   
			POUR TOUT rqCabeceras   
				   
				   
				//Init contador     
		Contador = 0   
		SI HExecuteRequeteSQL(rqCabeceras,cstNomConexioiGes,hRequêteSansCorrection,"SELECT * FROM Cabeceras WHERE Tipo='A'") ALORS     
		POUR TOUT rqCabeceras     
		     
		//Título sección     
		Contador++     
		SI Contador = 1 ALORS     
		RegistroFicheroSeguimiento += RC+RC+"ALBARANES RECIBIDOS"+RC+Repete("=",80)+RC+"FECHA NUMERO CLIENTE "+RC+Repete("=",80)     
		FIN   
   
		//Título sección   
		Contador++   
		SI Contador = 1 ALORS   
			RegistroFicheroSeguimiento += RC+RC+"ALBARANES RECIBIDOS"+RC+Repete("=",80)+RC+"FECHA       NUMERO  CLIENTE   "+RC+Repete("=",80)   
		FIN   
   
		_SageAlbaran.init()   
   
		//Actualizar estado reparto. Se indica el codigo del campo adicional y el valor a reasingar   
		SI "%HABILITARREPARTO%"="SI" ALORS   
			_SageAlbaran.CodigoCampoAdicional=""   
			_SageAlbaran.ValorCampoAdicional=""   
		FIN   
   
		SI rqCabeceras.CodigoCliente < ValorInicialNuevosClientes ALORS   
			_SageAlbaran.CodigoCliente = rqCabeceras.CodigoCliente   
		SINON   
		 	_SageAlbaran.CodigoCliente = tbEquivalencia[rqCabeceras.CodigoCliente]   
		FIN   
   
		//Datos cliente contado   
		_SageAlbaran.DatosClienteContado.NIF = rqCabeceras.NIF   
		_SageAlbaran.DatosClienteContado.Nombre = rqCabeceras.NombreFiscal   
		_SageAlbaran.DatosClienteContado.Domicilio = rqCabeceras.DomicilioFiscal   
		_SageAlbaran.DatosClienteContado.Poblacion = rqCabeceras.PoblacionFiscal   
		_SageAlbaran.DatosClienteContado.Telefono = rqCabeceras.TelefonoFiscal   
		   
		//Dirección entrega   
		_SageAlbaran.NumeroDireccion = rqCabeceras.NumeroDelegacion	   
		   
		//Cabecera albarán   
		//_SageAlbaran.Almacen = ""   
		_SageAlbaran.CodigoSerie = rqCabeceras.CodigoSerie   
		_SageAlbaran.GUID = rqCabeceras.GUID   
		SI Majuscule("%RENUMERAR_ALBARANES%")<>"SI" ALORS _SageAlbaran.Numero = rqCabeceras.Numero   
		_SageAlbaran.Fecha = DateVersChaine(Remplace(rqCabeceras.Fecha,"-",""),"AAAA-MM-JJ")   
		_SageAlbaran.Hora =  HeureVersChaine(Remplace(Gauche(rqCabeceras.Hora,5),":",""),"HH:MM")   
		_SageAlbaran.CodigoFPago = rqCabeceras.CodigoFPago   
		_SageAlbaran.CodigoRepresentante = rqCabeceras.CodigoRepresentante   
		SI ExisteAlbaran=0 ALORS _SageAlbaran.Observaciones = rqCabeceras.Observaciones   
		_SageAlbaran.ProntoPago = Val(rqCabeceras.ProntoPago)   
   
		//Init detalle lineas   
		DetalleLineas = ""   
		ContadorLinea est un entier=0   
   
		//Lineas del albarán   
		SI HExecuteRequeteSQL(rqLineas,cstNomConexioiGes,hRequêteSansCorrection,"SELECT * FROM Lineas WHERE CodigoCabecera="+rqCabeceras.CodigoCabecera+ " ORDER BY linea") ALORS   
		  POUR TOUT rqLineas   
				//Si se tienen que aplicar la promociones automáticamente y la línea actual se ha generado desde una promoción no se tiene que incorporar.   
				SI _Sage50.AplicarPromocionesAutomaticamente AND rqLineas.CodigoRegistroOrigenPromocion <> 0 ALORS   
					CONTINUER   
				FIN   
   
				ContadorLinea+=1   
				_SageLineaAlbaran.init()   
			  	_SageLineaAlbaran.Linea =ContadorLinea   
				_SageLineaAlbaran.CodigoProducto = rqLineas.CodigoProducto   
				_SageLineaAlbaran.Titulo = rqLineas.Titulo   
				_SageLineaAlbaran.Unidades = Val(rqLineas.Unidades)   
				_SageLineaAlbaran.NumEnvases = Val(rqLineas.NumEnvases)   
				_SageLineaAlbaran.PrecioVenta = Val(rqLineas.PrecioVenta)   
				//_SageLineaAlbaran.Peso = Val(0)   
				//_SageLineaAlbaran.PuntoVerde = Val(0)   
   
				//Descuento 1   
				SI rqLineas.AplicarDescuentoEnEuros ALORS   
					_SageLineaAlbaran.Descuento3 = Val(rqLineas.Descuento)   
				SINON   
					_SageLineaAlbaran.Descuento1 = Val(rqLineas.Descuento)   
				FIN   
   
				//Descuento 2   
				SI rqLineas.AplicarDescuento2EnEuros ALORS   
					_SageLineaAlbaran.Descuento3 = Val(rqLineas.Descuento2)   
				SINON   
					_SageLineaAlbaran.Descuento2 = Val(rqLineas.Descuento2)   
				FIN   
   
				Si rqcabeceras.regimeniva=2 ALORS    
					_SageLineaAlbaran.CodigoTipoIVA =0   
				SINON   
					_SageLineaAlbaran.CodigoTipoIVA = rqLineas.CodigoTipoIVA   
				fIN   
				_SageLineaAlbaran.Talla = rqLineas.CodigoValorPropiedad1   
				_SageLineaAlbaran.Color = rqLineas.CodigoValorPropiedad2   
				_SageLineaAlbaran.Lote = rqLineas.Lote   
				   
				//Regalo   
				_SageLineaAlbaran.EsRegalo = rqLineas.TipoLinea = "R" ? Vrai SINON Faux   
				   
				//Promoción   
				SI rqLineas.CodigoRegistroOrigenPromocion <> 0 ALORS   
					_SageLineaAlbaran.EsPromocion = Vrai   
					_SageLineaAlbaran.EsRegalo = Faux   
   
					SI HExecuteRequeteSQL(rqNumeroLineaPromocion, cstNomConexioiGes,hRequêteSansCorrection, "SELECT Linea FROM Lineas WHERE CodigoCabecera="+rqCabeceras.CodigoCabecera+" AND CodigoRegistro="+rqLineas.CodigoRegistroOrigenPromocion) ALORS   
					  SI HNbEnr(rqNumeroLineaPromocion) > 0 ALORS   
					  	HLitPremier(rqNumeroLineaPromocion)   
					  	_SageLineaAlbaran.LineaPromocionPadre = rqNumeroLineaPromocion.Linea   
					  FIN   
					FIN   
				FIN   
				   
				//Añadir linea al albarán   
				_SageAlbaran.addLinea(_SageLineaAlbaran)   
				   
				//Detalle del fichero seguimiento   
				SI _SageLineaAlbaran.EsRegalo ALORS   
					DetalleLineas += "  R  "   
				SINON SI _SageLineaAlbaran.EsPromocion ALORS   
					DetalleLineas += "  P  "   
				SINON   
					DetalleLineas += Repete(" ",5)   
				FIN   
				DetalleLineas += Complete(rqLineas.CodigoProducto,12)+" "+Complete(rqLineas.Titulo,20)+" "+NumeriqueVersChaine(rqLineas.Unidades,"8.2f")+"  "+NumeriqueVersChaine(rqLineas.PrecioVenta,"9.2f")+"  "+NumeriqueVersChaine(rqLineas.Descuento,"8.2f")+"  "+NumeriqueVersChaine(rqLineas.ImporteNeto,"10.2f")+RC			   
				SI rqLineas.Lote <> "" ALORS DetalleLineas += Repete(" ",10)+"LOTE: "+rqLineas.Lote+RC	   
				SI rqLineas.CodigoValorPropiedad1 <> "" ALORS DetalleLineas += Repete(" ",10)+"TALLA: "+rqLineas.CodigoValorPropiedad1+RC   
				SI rqLineas.CodigoValorPropiedad2 <> "" ALORS DetalleLineas += Repete(" ",10)+"COLOR: "+rqLineas.CodigoValorPropiedad2+RC   
   
		  FIN   
		SINON   
			LogIncorporacion("Se ha producido un error al seleccionar las lineas del albaran ["+rqCabeceras.CodigoSerie+"/"+rqCabeceras.Numero+"]")   
		FIN   
   
		//Guardar albarán   
		SI _SageAlbaran.guardar() ALORS   
			RegistroFicheroSeguimiento += RC+Complete(DateVersChaine(ChaineVersDate(rqCabeceras.Fecha,"AAAA-MM-JJ"))+"  "+rqCabeceras.CodigoSerie+" "+rqCabeceras.Numero+"  "+rqCabeceras.CodigoCliente+" - "+rqCabeceras.NombreFiscal,80)   
			RegistroFicheroSeguimiento += RC+DetalleLineas   
		SINON   
		 	LogIncorporacion("Se ha producido un error al guardar el albaran ["+rqCabeceras.CodigoSerie+"/"+rqCabeceras.Numero+"]. Detalles del error: "+_SageAlbaran.getLastError())   
		FIN   
		   
		//Integrar cobros de albaran   
		SI HExecuteRequeteSQL(rqCobros,cstNomConexioiGes,hRequêteSansCorrection,"SELECT * FROM Cobros WHERE codigocabecera='"+rqCabeceras.codigocabecera+"'" + "and cobrado=1") ALORS   
			POUR TOUT rqCobros   
				SI _SageAlbaran.entregaACuenta(rqCobros.ImporteCobrado) ALORS   
					RegistroFicheroSeguimiento += RC+"Entrega a cuenta: "+rqCobros.ImporteCobrado   
				SINON   
					LogIncorporacion("Se ha producido un error al guardar el cobro de albaran ["+rqCabeceras.GUID+"]. Detalles del error: "+_SageAlbaran.getLastError())   
				FIN   
			FIN   
		FIN   
	FIN   
SINON   
	LogIncorporacion("Se ha producido un error al seleccionar los albaranes")   
FIN
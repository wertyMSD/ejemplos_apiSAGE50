---
{}
---
   
Tiene que ver :[Albaran venta](../../../../100_Proyectos/Sage50/pySage50e/documentos/Albaran%20venta.md)   
   
``` IGES   
//Añadimos linea adicional del documento de venta con la descripcion larga del producto   
// en el caso que el cliente quiera poner comentarios de linea usaremos el campo de descripcion larga    
// de las lineas de pedido para poner ese comentario y pasarlo a sage. Los comentarios en sage son    
// lineas sin codigo de producto , tener en cuenta que hay que poner la dll de fecha 31/03/2021 o superior   
tmpCodigoCabecera est un entier   
HExécuteRequêteSQL(rq,cstNomConexioiGes,hRequêteSansCorrection,"SELECT 1 AS Procesar FROM Lineas WHERE Descripcion<>''")   
HLitPremier(rq)   
SI rq.Procesar=1 ALORS   
	Linea est un entier=0   
	HExécuteRequêteSQL(rq,cstNomConexioiGes,hRequêteSansCorrection,"SELECT * FROM Lineas ORDER BY CodigoCabecera,Linea")   
	POUR TOUT rq   
		SI rq.CodigoCabecera<>tmpCodigoCabecera ALORS   
			tmpCodigoCabecera=rq.CodigoCabecera   
			Linea=0   
		FIN   
		Linea++	   
		HExécuteRequêteSQL("ins",cstNomConexioiGes,hRequêteSansCorrection,"UPDATE Lineas SET Linea="+Linea+" WHERE CodigoRegistro="+rq.CodigoRegistro)   
		SI rq.Descripcion<>"" ALORS   
			Linea++   
			InstruccionSQL est une chaîne=[   
				INSERT INTO Lineas (CodigoCabecera,Linea,Titulo,CodigoRegistro)    
				VALUES   
				(%1,%2,'%3',(SELECT MAX(CodigoRegistro)+1 FROM Lineas))   
			]   
			InstruccionSQL=ChaîneConstruit(InstruccionSQL,rq.CodigoCabecera,Linea,rq.Descripcion)   
			HExécuteRequêteSQL("ins",cstNomConexioiGes,hRequêteSansCorrection,InstruccionSQL)   
		FIN   
	FIN   
FIN
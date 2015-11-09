def Guardar_datos(datos):
	#abrimos un archivos que sera usado para guardar los clientes que ingrese
	archivo = open("Sistema_de_Ingreso.txt", "a") 
	archivo.write("CLIENTE".center(45, "-") )
	archivo.write("\n")
#vamos recorriendo los datos de la lista y lo vamos agrgando al archivo
	for x in datos:		
		archivo.write(x)
		archivo.write(",") 
	archivo.write("\n") 	
	archivo.close() 
	print ("Datos Guardaos Exitosamente")

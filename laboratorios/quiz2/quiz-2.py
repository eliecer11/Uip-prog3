# laboratorio clase 4

descuento1= 0.30
descuento2= 0.20
descuento3= 0.10


while clientes < 5:
	clientes = int(input("ingrese cliente: "))
	
	clientes +=1

	compra=
		int(input("ingrese compra: "))

	if compra >=500:
		descuento = compra*descuento1
		total = compra+descuento
		print (total a pagar el cliente es {0} ".format (total ))

	if compra < 500 or >= 200:
		descuento = compra*descuento2
		total = compra+descuento
		print (total a pagar el cliente es {0} ".format (total ))

	if compra < 200 0r >= 100:
		descuento = compra*descuento3
		total = compra+descuento
		print (total a pagar el cliente es {0} ".format (total ))	
	
	else
		print("no existe descuento")

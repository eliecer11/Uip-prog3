# 5.	El Emperador esta celebrando aniversario y ofrecera a sus clientes una serie 
#de ofertas que se traduciran en un incremento de sus ventas Las reglas de las ofertas
#se basan en un porcentaje de descuento sobre el total de compra,  que estarian variando 
#dependiendo del monto adquirido: Por un ponton mayor o igual a $500 descuento del 30 Por
#un monto menor de $500 pero mayor o igual a $200 despuento del 20% Por un monto menor de
#$200 pero mayor o igual a $100 descuento del 10% Elabore este programa considerando 5 
#susuarios por ejecución

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

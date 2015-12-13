import quiz1menu 
op  = 0
opc= 0
elemento= ""

vegetales= []
bebidas= []
personal= []
def agregar(lista, elemento):
	lista.append(elemento)
def eliminar(lista, elemento):
        if elemento in lista:
                print (type(elemento))
                lista.remove(elemento)
        else:
            print("no existe el artiuclo")
def impresion(lista):
	for x in lista:
		print ("* "+x)

try:
	while (opc != 3):
		print ("--SUPERMERCADO--")
		print("1. VEGETALES")
		print("2. BEBIDAS")
		print("3. PERSONALES")
		opc =  int((input ("------> ")))
		if (opc == 1): # VEGETALES
			op =  int (quiz1menu.inicio())
			if op == 1: # agregar
				elemento = input("Ingrese el articulo: ")
				agregar(vegetales,elemento)
			if op == 2: # eliminar
				elemento = input("Ingrese el articulo a eleiminar: ")			
				print (type(elemento))
				eliminar(vegetales,elemento)			
			if op==3: # ver 
				print("--IMPRESION--")
				impresion(vegetales)
		elif opc == 2: # BEBIDAS
			op =  int (quiz1menu.inicio())
			if op == 1: # agregar
				elemento = input("Ingrese el articulo: ")
				agregar(bebidas,elemento)
			if op == 2: # eliminar
				elemento = input("Ingrese el articulo a eleiminar: ")			
				print (type(elemento))
				eliminar(bebidas,elemento)			
			if op==3: # ver 
				print("--IMPRESION--")
				impresion(bebidas)
		elif opc==3: # PERSONALES 
			op =  int (quiz1menu.inicio())
			if op == 1: # agregar
				elemento = input("Ingrese el articulo: ")
				agregar(personal,elemento)
			if op == 2: # eliminar
				elemento = input("Ingrese el articulo a eleiminar: ")			
				print (type(elemento))
				eliminar(personal,elemento)			
			if op==3: # ver 
				print("--IMPRESION--")
				impresion(personal)
except Exception as e:
	print(e) 

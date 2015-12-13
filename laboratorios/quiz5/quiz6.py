nam = input("Ingrese la palabra magica:  "  )

if nam =="hola mundo":
    print("Exitooo")
    archivo = open("holamundo.txt","a")
    archivo.write("Hola mundo")
    archivo.close
else:
	print("No es la Palabra magica")

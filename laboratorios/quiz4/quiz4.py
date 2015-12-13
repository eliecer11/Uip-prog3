
def grabartxt(nombre,notas, promedio):
	archi=open((nombre+'.txt'),'a')
	archi.write("Nombre: ")
	archi.write(nombre)
	archi.write("\n")
	archi.write("Notas: ")
	for x in notas:
		nota = ""+str(x)
		archi.write(nota+" ")
	archi.write("\n")
	archi.write("Promedio: ")
	archi.write(str(promedio))
	archi.close()
	    
for x in range(3):
	calificaciones= []
	promedio=0
	nota = []
	print ("Estudiante #"+str(x+1))
	nombre = input("Ingrese el nombre: ")
	for c in range(4):
		nota = int (input("Ingrese la Calificaciones #"+str(c+1)+" ----> "))
		calificaciones.append(""+str(nota))
		promedio += nota
	print("promedio "+str(promedio/4))
	grabartxt(nombre,calificaciones,(promedio/4))

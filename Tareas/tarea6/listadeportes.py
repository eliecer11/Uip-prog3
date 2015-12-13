def menu():
        print("1.AJEDREZ")
        print("2.ATLETISMO")
        print("3.BALONCESTO")
        print("4.FUTBOL")
        print("5.KARATE")
        print("6.NATACION")
        print("7.VOLLEYBALL")
        print("8.FLAG")
        print("9.PING PONG")
        print("0.0TROS")
        opc = int(input("------>"))
        return opc
aj=0
at=0
bal=0
fut=0
kar=0
nat=0
voll=0
fla=0
pin=0
otros=0
for x in range(10):	
	print("Encuentas #"+str(x+1))
	print("QUE DEPORTES TE GUSTA")
	opc = menu()
	if opc == 1 : aj+=1
	if opc == 2 : at+=1
	if opc == 3 : bal+=1
	if opc == 4 : fut+=1
	if opc == 5 : kar+=1
	if opc == 6 : nat+=1
	if opc == 7 : voll+=1
	if opc == 8 : fla+=1
	if opc == 9 : pin+=1
	if opc == 0 : otros+=1
print("RESUMEN DE DEPORTES")
print ("Deporte #"+str(1),"promedio ",str(aj*0.1*100))
print ("Deporte #"+str(2),"promedio ",str(at*0.1*100))
print ("Deporte #"+str(3),"promedio ",str(bal*0.1*100))
print ("Deporte #"+str(4),"promedio ",str(fut*0.1*100))
print ("Deporte #"+str(5),"promedio ",str(kar*0.1*100))
print ("Deporte #"+str(6),"promedio ",str(nat*0.1*100))
print ("Deporte #"+str(7),"promedio ",str(voll*0.1*100))
print ("Deporte #"+str(8),"promedio ",str(fla*0.1*100))
print ("Deporte #"+str(9),"promedio ",str(pin*0.1*100))
print ("Deporte #"+str(0),"promedio ",str(otros*0.1*100))

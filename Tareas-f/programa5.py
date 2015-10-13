


chance = 0

minutos = 0

while chance < 10:

    tiempo = int(input("Introduzca el tiempo en minutos: "))

    chance +=1

    if tiempo / 60:

        dias = 24 - tiempo % 24
		
		    horas = 8 - tiempo % 8
		
	    	minutos = 60 - tiempo % 60

        print(dias)
		
	     	print(horas)
		
        print(minutos)

        

        


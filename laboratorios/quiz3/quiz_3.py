#dado un intervalo de tiempo en segundos, calcular los segundos restantes 
#corresponden para convertirse exactamente en minutos. Este programa debe 
#funcionar para 5 oportunidades.

chance = 0
segundos_restantes = 0
while chance < 5:
	segundos = int (input("Introduzca sus segundos:"))
	chance +=1
	if segundos / 60:
		segundos_restantes =60-segundos%60
		print (segundos_restantes)


#Escriba un programa en Python donde el usuario introduce un número n 
#y el programa imprime los primeros n números triangulares, junto con 
#su índice. Los números triangulares se originan de la suma de los números
#naturales desde 1 hasta n.Ejemplo: Si se piden los primeros 3 números
#triangulares, la salida es: 1 - 1 2 - 3 3 - 6



try:
    numero = int(input("Introduzca un numero: "))
except ValueError:
    print("debe ser un numero Natural")
    numero = 0

index = 0
result = 0


if numero < 0:
    print("Este numero no es natural")
else:
    while (index <= numero):
        result += index
        index += 1


    print(str(numero) + " - " + str(result))

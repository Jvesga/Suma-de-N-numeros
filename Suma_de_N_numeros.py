"""SUMA DE N NUMEROS"""

# INPUT
N = int(input("Digite el valor de N: "))

# processing

i = 1
suma = 0
while (i <= N):
    suma = suma + i
    i = i + 1

# input 
print("La suma de los " + str(N) + " primeros numeros es " + str(suma))
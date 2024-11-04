#lista "base"
lista = list(range(16))

#intervalo de 1 a 9
intervalo_1a9 = lista[1:10]

#intervalo de 8 a 13
intervalo_8a13 = lista[8:14]

#numeros pares
num_par = [num for num in lista if num %2 == 0]

#numeros impares
num_impar = [num for num in lista if num %2 != 0]

#multiplos de 2, 3 e 4
multiplos = [num for num in lista if num %2 == 0 or num %3 == 0 or num %4 == 0]

#lista reversa
reversa = lista[::-1]

#intervalo de 10 a 15
int_10a15 = lista[10:16]
soma1 = sum(int_10a15)

#intervalo de 3 a 9 
int_3a9 = lista[3:10]
soma2 = sum(int_3a9)

#razão entre a soma do intervalo de 10 a 15 por o intervalo de 3 a 9
razao = soma1 / soma2

#exibindo os resultados
print("intervalo de 1 a 9:", intervalo_1a9)
print("intervalo de 8 a 13:", intervalo_8a13)
print("numeros pares:", num_par)
print("numeros impares:", num_impar)
print("multiplos de 2, 3 e 4:", multiplos)
print("lista reversa:", reversa)
print("razão entre a soma do intervalo de 10 a 15 por o intervalo de 3 a 9:", razao)
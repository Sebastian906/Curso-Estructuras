# Sumatoria de una lista
lista = [2, 4, 6, 1, 2]

# Definir valor inicial de sumatoria como 0
sumatoria = 0

# Recorrido de la lista 
for num in lista:
    # Incrementa la sumatoria mientras se recorre la lista
    sumatoria += num

print(sumatoria)

# Promedio de una lista
promedio = 0
for num in lista:
    promedio += num

# Se divide el promedio por el total de la lista
promedio /= len(lista)
print(promedio)

# Sacar dato más grande de la lista
max = 0
for num in lista:
    if max < num:
        max = num
print(max)

lista_negativa = [-1, -3, -7, -2]
max = lista_negativa[0]
for num in lista_negativa:
    if max < num:
        max = num
print(max)

min = lista_negativa[0]
for num in lista_negativa:
    if min > num:
        min = num
print(min)
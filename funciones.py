lista = [1, 3]

# Método append para añadir un dato a la lista
lista.append(4)
print(lista)

# Método extend para añadir una sublista a la lista existente
lista.extend([5, 6, 7])
print(lista)

# Método insert para añadir un valor en una posición espécifica
lista.insert(1, 2) # indice (posición del arreglo), valor
print(lista)

# Creación de nueva lista de letras
letras = ["x", "y", "z"]
# Método remove para quitar un dato específico de la lista
letras.remove("y")
print(letras)

numeros = [1, 2, 2, 2, 2, 2, 3, 4, 5]
numeros.remove(2) # Solo se remueve la primera ocurrencia del dato (en caso de repetirse)
print(numeros)

nombres = ["Juan", "Elena", "Pedro", "Maria"]
# Método pop que elimina el último dato de la lista
nombres.pop()
print(nombres)

# Se indica indice a borrar de la lista
nombres.pop(1)
print(nombres)

# Método count que devuelve cantidad de datos de un valor en espécifico
print(numeros.count(2))

# Método index para verificar posisión de dato en la lista
mas_letras = ["a", "b", "c", "d", "d"]
print(mas_letras.index("b"))
print(mas_letras.index("d")) # Retorna la primera instancia en caso de dos datos
# Método len para contar total de valores en la lista
print(len(mas_letras))
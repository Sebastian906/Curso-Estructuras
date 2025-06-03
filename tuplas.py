tupla = ("a", "b", "c")

tupla2 = 1, 2, 3, 4

tupla_combinada = ("a", 2, "c", 4.4)

print(tupla_combinada)

print(tupla_combinada[0])

tupla_grande = ("Python", "Java", "C++", "Javascript", "Go", "PHP")
print(tupla_grande)

# Buscar valores entre un rango determinado
print(tupla_grande[2:5])

# Prueba de cambiar valor en tupla (debe fallar)
#tupla_combinada[0] = 3

# Transformar tupla en lista
tupla_original = ("A", "B", "C", "D")
nueva_lista = list(tupla_original)
print(nueva_lista)

# Transformar lista a tupla
lista_original = ["A", "B", "C"]
nueva_tupla = tuple(lista_original)
print(nueva_tupla)

# Recorrido de tuplas
tupla_letras = ("x", "y", "z")
for letra in tupla_letras:
    print(letra)
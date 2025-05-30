# Definir lista inicial
lista = ["a", "b", "c"]

# Definición de otra lista con diferentes tipos de valores 
lista_distinta = ["A", 2, "C", 4.4]

# Lector de lista distinta de acuerdo a las posiciones 
print(lista_distinta)
print(lista_distinta[0])
print(lista_distinta[1])
print(lista_distinta[2])
print(lista_distinta[3])

# Cambio de variable dentro de la primera lista en posición [1] 
lista[1] = "B"
print(lista)

# Definición de lista con gran cantidad de datos
lista_grande = ["Python", "Javascript", "Typescript", "Java", "Go", "C++", "C#"]

print(lista_grande)

# Definición de lista pequeña con datos de lista grande en un rango menor
lista_pequena = lista_grande[0:3]

print(lista_pequena)

lista_grande[3:5] = ["Rust", "PHP"]

print(lista_grande)
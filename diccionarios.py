estudiante = {
    "nombre": "Sebastian",
    "apellido": "Salazar",
    "edad": 24,
    "ciudad": "Manizales"
}

# Imprimir todo el diccionario
print(estudiante)

# Imprimir un valor específico del diccionario
print(estudiante["nombre"])

# Cambiamos un valor del diccionario
estudiante["edad"] = 23
print(estudiante)

# Ingresar nuevo elemento dentro del diccionario
estudiante["cursos"] = ["Python", "Javascript", "Go"]
print(estudiante)

# Recorrido de llaves en el diccionario
for llave in estudiante:
    print(llave)

# Recorrido de los valores dentro de las llaves en el diccionario
for llave in estudiante:
    print(estudiante[llave])

# Recorrido para imprimir llave y valores correspondientes
for llave, valor in estudiante.items():
    print(llave, valor)
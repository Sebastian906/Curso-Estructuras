matriz = [
    [1, 3, 5, 6, 9],
    [3, 2, 4, 5, 8],
    [7, 1, 5 ,0 ,6]
]

print(matriz[2][0])

print(matriz)

print(matriz[1])

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        print(matriz[i][j], end= " ")
    print()
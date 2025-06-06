set1 = (2, 3, 5, 7)
set2 = set([2, 3, 5, 7])

nombres = {"Elena", "Juana", "Pablo", "Elena"}
print(nombres)

for nombre in nombres:
    print(nombre)

print("Elena" in nombres)

nombres.add("Pedro")
print(nombres)

nombres.remove("Elena")
print(nombres)

# Elimina elemento aleatoriamente
nombres.pop()
print(nombres)
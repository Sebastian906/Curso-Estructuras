lenguajes1 = {"Python", "Java", "PHP", "Go"}
lenguajes2 = {"C++", "Javascript", "Java", "C#"}

todos_lenguajes = lenguajes1.union(lenguajes2)
print(todos_lenguajes)

coincidencias = lenguajes1.intersection(lenguajes2)
print(coincidencias)

print(lenguajes1.isdisjoint(lenguajes2))

mas_lenguajes = {"Ruby", "Rust"}
print(lenguajes1.isdisjoint(mas_lenguajes))
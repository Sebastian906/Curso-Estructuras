lista_alumnos = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", "apellido": "Paramo", "id": 345, "cursos": ["Fundamentos de la Web", "Python", "MERN", "Golang"]},
]

lista_alumnos[2]["cursos"].pop(2)

from pprint import pprint
pprint(lista_alumnos)
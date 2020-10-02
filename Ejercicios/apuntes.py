# Longitud listas

# alumnos = ["enrique", "oscar"]

# len(alumnos)

# alumnos.append introduce en una lista

# alumnos.extend introduce un elemento en la lista

# alumnos.clear limpia la lista

# alumnos.pop saca al ultimo de la lista

# se pueden sumar dos listas alumnos + nuevos_alumnos

# realizar saltos alumnos[::3] recoger de la lista desde el primer valor saltando al tercero y viceversa

# recoger de la lista del primer valor al segundo alumnos[:2]

# invertir orden de la lista alumnos[::-1] o relizar saltos al reves salumnos[::-2]

# del letras[4] elimina la posicion 4 empezando desde 0

# del letras borraria la lista completa

# realizar una copia de un elemento a otro sin que se cambien los datos al cambiarlos en uno de los dos lados
# from copy import deepcopy
# nuevas_letras = deepcopy(letras)
# y no tendrian el mismo id

# bucles
# for x in numeros:
    # print(x)

# for i in range(len(numero)):
    # print(numero[i])

# asi te devuelve el indice y el nombre con el enumerate
# for i, alumno in enumerate(nuevos_alumnos):
    # print(i, alumnos)

# saber si un valor esta en la lista
# 4 in numeros y te devuelve true o false
# "oscar" in nuevos_alumnos

# con count contamos las veces que se repite un elemento en la lista
# numeros.count(variable o elemento a buscar)

# tuplas tupla = (1,2,3) es inmutable, y no se puede hacer nada con ella ni añadir ni eliminar, no se puede modificar
# se utiliza para constantes

# en vez de else if es elif
# if ....... :
# elif ..... :
# else ..... :
# aqui los condiciones son or o and
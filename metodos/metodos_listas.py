#Crear una lista con list() (No sirve de mucho)
lista = list(["Joaquin", "Puertas", 25, 1.80])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("de boca")

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"Con Ani")

#agregando varios elementos a la lista
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice) 
#lista.pop(0)
#eliminando un elemento de la lista (por su indice) para eliminar el ultimo -1
lista.pop(3)

#removiendo un elemento de la lista por su valor
lista.remove("Puertas")

#eliminando todos los elementos de la lista
#lista.clear()

#ordena la lista de false a true y siguiendo con numeros de menor a mayor
#si lo ponemos en reverse = true los invierte
#lista.sort()
#lista.sort(reverse=True)

#invirtiendo los elementos de una lista
#lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index("Con Ani")

print(elemento_encontrado)
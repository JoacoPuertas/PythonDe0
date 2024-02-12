#Creando un conjunto con set()
conjunto = set(["dato 1", "dato 2"]) #No son modificables los datos de un conjunto

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1, "Dato 3"}

# print(conjunto2)

#Teoria de conjuntos 

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verficando si conjunto2 es un subconjunto de conjunto 1
resultado = conjunto2.issubset(conjunto1)
#resultado = conjunto2 <= conjunto1 # Otra forma

#Verficando si conjunto es un superconjunto de conjunto 2
resultado2 = conjunto1.issuperset(conjunto2)
#resultado = conjunto1 >= conjunto2 # Otra forma

#Verificar si hay un numero en comun
resultado3 = conjunto2.isdisjoint(conjunto1) # Devuelve true si no hay ningun numero en comun
print(resultado)
print(resultado2)
print(resultado3)
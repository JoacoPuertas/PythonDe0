#creando diccionarios con dict()
diccionario = dict(nombre="lucas",apellido="dalto")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos como key
#diccionario = {("Joaco", "Puertas") : "Crack"} #Uso una tupla como key
diccionario = {frozenset(["Joaco", "Puertas"]): "Crack"} 

#Creando un diccionario con fromkeys()
diccionario = dict.fromkeys(["nombre", "apellido"])

print(diccionario)
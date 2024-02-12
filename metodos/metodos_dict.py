diccionario = {
    "nombre": 'Joaquin',
    "apellido": 'Puertas',
    "edad": 20
}

# claves = diccionario.keys() --> Devuelve las claves (tambien nos sirve para iterar(?))

# claves = diccionario.get("edad") --> Devuelve el valor de una clave

# claves = diccionario.clear() #--> Elimina todos los elementos del diccionario

diccionario.pop("nombre") # --> Elimina un elemento del diccionario

diccionario_iterable = diccionario.items() # --> para iterar el dict

print(diccionario_iterable)


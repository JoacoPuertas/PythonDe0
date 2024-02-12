diccionario = {
    "Nombre": "Joaquin",
    "Apellido": "Puertas",
    "Edad": "20 años",
    "Estado Civil": "Con Ani"
}

#Recorriendo diccionario para obtener las claves
for key in diccionario:
    print(f"la clave es {key}")
#Recorriendo diccionario con items() para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"{key}: {value}")

#Creando una funcion cn paramteros
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido} sos muy {adjetivo}"

#Utilizando keywords arguments
frase_resultante = frase(apellido =  "Puertas",adjetivo= "Crack", nombre="Joaquin" )
print(frase_resultante)

#Creando una funcion con un parametro predeterminado que luego se puede cambiar
def frase_nueva(nombre,apellido,adjetivo = "tonto"):
    return f"Hola {nombre} {apellido} sos muy {adjetivo}"

print(frase_nueva("Joaquin", "Puertas", adjetivo = "Inteligente"))
#creando una funcion simple()
#def saludar():
    #print("Hola")

# Ejecutando la funcion simple
#saludar()

#Crear una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "maestro"
    else:
        adjetivo = "amor" 
    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")

saludar("Joaquin", "hombre")
saludar("Nacho", "helicoptero")

# Crear una funcion que retorne un valor
def crear_contraseña(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

password,primer_num = crear_contraseña(6)


print(f"Tu nueva contraseña es: {password} y el numero utilizado fue {primer_num}")



# Hola Mundo
a = "Joaco"
b = 5
c = "Hola " + a + f" {b}" + " Puto"

# Usar snake_case para definir variables
#nombre_completo = "Joaco Puertas"

#print(nombre_completo)
# Operadores de pertenencia (not in / in)

#print("Hola" in c) #True

#print("hola" not in c) #True

#print("hola" in c) #False porque es sensibles a las mayusculas, h y H son caracteres totalmente distintos

#Creando Datos Compuestos
#Array y tupla (? unica diferencia
lista = ['Joaco', 'Puertas', 20, 1.80] # Se puede Modificar
tupla = ('Joaco', 'Puertas', 20, 1.80) # No se puede modificar

print(lista[0])
print(tupla[1])

#creando un conjunto (set)

# Se muede recontruir pero no modificar un elemente del set. No se puede acceder con un indice. No puede haber un elemento repetido.
conjunto = {'Joaco', 'Puertas', 20, 1.80}

#Creando un diccionario (dict) (la estructura es key : value t¿y separamos con comas)
diccionario = {
    'nombre' : "Joaquin Puertas",
    'Edad' : "20 años"
}

print(diccionario['nombre'])
#Funcion para obtener el asistente y el profesor segun la edad (El mas grande es el profe y el mas chico es el asistente)
def obtener_compañeros(cantidad_de_compañeros):
    
    #Creando la lista con los compañeros 
    compañeros = []
    
    #Ejecutando el for para obtener el nombre y la edad de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input(("Escribí el nombre del compañero: "))
        edad = int(input("Ingresá la edad del compañero: "))
        compañero = (nombre, edad)
        
        #Agregando la informacion a la lista
        compañeros.append(compañero)
    
    #Ordenando la lista de menor a mayor por la key edad (Que seria [1] porque la key [0] es la de nombre)
    compañeros.sort(key = lambda x: x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre 
    #para definir al asistente y al profesor.
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #Retornamos una tupla 
    return asistente,profesor

#Desempaquetamos lo que nos retorna la funcion y le asignamos la cantidad de alumnos que hay en la clase
asistente, profesor = obtener_compañeros(4)

#Imprimimos en la consola 
print(f"El asistente es {asistente} y el profesor es {profesor}")
        
        
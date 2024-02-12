
# Esto funciona exactamente igual con Listas que con tuplas y conjuntos
animales = ["koala", "pinguino", "pez", "cocodrilo"]
Las_Fuerzas_del_cielo = ["Ani", "Joaco", "Cande", "Fercho"]
    
#Recorriendo la lista numeros y multiplicando cada valor por 5
Numeros = [20,40,50,73]

for numero in Numeros:
    resultado = numero * 5
    #print(resultado)

for animal, crack in zip(animales,Las_Fuerzas_del_cielo):
    print(f"{crack} es un {animal}")


#Recorrer una lista a partir del indice 
#Forma no optima de recorrer una lista
for i in range(len(Las_Fuerzas_del_cielo)): # No funciona en conjuntos
    print(Las_Fuerzas_del_cielo[i])
    
    
#Forma correcta de recorrer una lista con su indice
for num in enumerate(Las_Fuerzas_del_cielo):
   i = num[0]
   Valor = num[1]
   print(f"el indice es: {i} y el valor es: {Valor}")
   
#Usando el for/else
for numero in Numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else: # Se ejecuta cuando termina de recorrerse el for
    print("el bucle termino")
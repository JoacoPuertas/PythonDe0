numeros = [1,3,5,7,9,1.666666]

#Encontrando el numero mayor de una lista (Lo mismo con el numero mas bajo pero con min())
numero_mas_alto = max(numeros)
numero_mas_bajo = min(numeros)
print(f"El numero mas alto de la lista es :{numero_mas_alto}")
print(f"El numero mas bajo de la lista es :{numero_mas_bajo}")

#Redondeando de 6 decimales de la manera vieja
numero = round(15.356858 * 100)
print(numero / 100)

#Forma nueva 
numero2 = round(15.356858,2)

print(numero2)

#Retorna false -> 0, vacio, False, none / True -> distinto a 0, True, cadena, datos no vacios
resultado_bool = bool([])

print(resultado_bool)

#Retorna True, si todos los valores son verdaderos
resultado_all = all([234, "True", [544, 687]])
print(resultado_all)

#Suma todos los valores de un iterable #Si o si tienen que ser int o float #Tenes que cerrar el estadio
suma_total = sum(numeros)
print(round(suma_total,2))



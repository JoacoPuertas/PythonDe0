numeros = [1,2,3,4,5,6,7,8,9,10,11,12,15,20]

#Creando una funcion comun que diga si es par o no
#def es_par(num):
 #   if(num%2 == 0):
  #      return True

#Usando filter con una funcion comun
#numeros_pares = filter(es_par,numeros)

#Creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numeros:numeros%2==2,numeros)
print(list(numeros_pares))
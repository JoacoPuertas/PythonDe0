#Creando una funcion que determine cuales son los numeros primos en desde 2 al numero que le asignemos

def es_primo(num):
    for i in range(2,num - 1):
        if num %i == 0: return False # Significa que se puede dividir por algun numero y no es primo. Si esto ocurre termina el bucle
    return True

#numero = int(input("Escribi el numero que queres verificar si es primo: "))
#print(es_primo(numero)) # Primer prueba

#Esta funcion utiliza la funcion anterior para verificar cuales son numeros primos para agregarlos en una lista y luego imprimirlos en la consola
def primos_hasta(num):
    #Esta es la lista (Ahora vacia) que luego vamos a llenar con los numeros primos
    primos = []
    #For que recorre desde el 3 hasta ek numero que queramos verificando cuales son los numeros primos
    for i in range(3,num + 1):
        # Le pone el valor de True o False a resultado dependiendo si el numero recorrido es primo o no
        resultado = es_primo(i)
        # Si es true los agrega a la lista "primos" con la funcion append(usando el numero que se usó en la fucion es_primo(en este caso es i))
        if resultado == True : primos.append(i)
    #Retorna la lista primos con todos los numeros ya cargados
    return primos

#Le pide al usuario que escriba un numero que se almacena en la variable numero
numero = int(input("Escribi el numero hasta el que queres verificar cuales son los primos: "))
# Esa variable la usamos en la funcion primos_hasta porque dicha funcion pide el parametro para funcionar
resultado = primos_hasta(numero)
#Imprimimos el resultado de la funcion (Que seria el return primos que mencionamos anteriormente)
print(f"Estos son todos los numeros primos: {resultado}")
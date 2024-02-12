#Creando una funcion que nos muestre la lista de numeros fibonacci

#def fibonacci(num):
#    a,b = 0,1
#    fibonacci_lista = [0]
#    for i in range(num):
#        if b > num: return fibonacci_lista
#        else:
#            fibonacci_lista.append(b)
#            a,b = b, a+b

#numero = int(input("Ingresá el numero que quieras y te mostraré cuales son los numeros que siguen el patron de fibonacci hasta ese numero: "))
#resultado = fibonacci(numero)
#print(resultado)


#Manera mas optimizada de hacer lo mismo
def fibonacci(num):
    a, b = 0, 1
    fibonacci_lista = []
    while a <= num:
        fibonacci_lista.append(a)
        a, b = b, a + b
    return fibonacci_lista

numero = int(input("Ingresa el número hasta el cual quieres obtener la secuencia de Fibonacci: "))
resultado = fibonacci(numero)
print(resultado)
print("El que lee es puto :) Feliz cierre de año")


#Utilicé un bucle while en lugar de for, ya que no necesitamos una condición adicional para verificar si b supera el número dado.
#Eliminé la condición if b > num: return fibonacci_lista, ya que el bucle while se encarga de salir cuando se supera el número dado.
#Cambié el nombre de la variable en el mensaje de entrada para que sea más claro.
#Inicialicé fibonacci_lista como una lista vacía desde el principio, ya que 0 se añade en la primera iteración del bucle.
#Abriendo el archivo con with open y asignandole el nombre archivo
with open("archivos\\Msj ani.txt", encoding="UTF-8") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
#No es necesario cerrarlo al usar with open
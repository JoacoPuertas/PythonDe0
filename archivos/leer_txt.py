#Usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo_sin_leer = open("archivos\\Msj ani.txt",encoding="UTF-8") #Para abrir el archivo usamos open y adentro ponemos la ruta del archivo. 
#Parra que se puedan usar las tildes y otros caracteres usamos encoding = UTF-8.

#Imprime cosas raras
print(archivo_sin_leer)

#Para leer el archivo completo usamos la funcion read()
#archivo = archivo_sin_leer.read()

#Para leer una sola linea o caracteres especificos usamos readline()
linea_1 = archivo_sin_leer.readline()

archivo_sin_leer.close()
#Para leer varias lineas usamos readlines()
#lineas = archivo_sin_leer.readlines()
print(linea_1)

with open("archivos\\Msj ani.txt","w", encoding="UTF-8") as archivo:
    #Sobreescribiendo el archivo
    #archivo.write("")
    #archivo.writelines("","")
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
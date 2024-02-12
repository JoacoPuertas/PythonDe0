with open("archivos\\Msj ani.txt","a", encoding="UTF-8") as archivo:
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Linea {i} Agregada \n")
    
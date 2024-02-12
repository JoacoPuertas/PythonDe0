frutas = ["Banana", "Manzana", "Naranja", "Mandarina", "Anana", "Ciruela", "Pera", "Duraznos"]
cadena = "Joaco el mas mejor"
numeros = [2,5,8,10]


#Evitando que se coma un Anana con la sentencia continue
for fruta in frutas:
    if fruta == "Anana":
        continue
    print(f"Me voy a comer una {fruta}")

#Evitar que el bucle siga ejecutandose
for frutita in frutas:
    print(f"Me voy a Morfar una {frutita}")
    if frutita == "Naranja":
        break

print("Me duele la panza no quiero comer mas fruta")

#Recorrer cadena de texto (Caracter por caracter)
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo (Duplicamos los numeros de una lista)
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)
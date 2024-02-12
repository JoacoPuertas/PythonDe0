frase = input("Decime una palabra y te calculo cuanto tardarias en decirlo: ")
palabras_separadas = frase.split(" ")
cantidad_palabras = len(palabras_separadas)

print(f"Dijiste {cantidad_palabras} palabras y tardarias {cantidad_palabras/2} segundos en decirlo")
print(f"Dalto tardaria {round(cantidad_palabras / 2 / 1.3,2)} segundos en decirlo")
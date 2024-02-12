cadena1 = "Joaquin"
cadena2 = "Ani, la, mas, crack"

#resultado = dir(cadena1)

#dir es una funcion que te dice que metodos se pueden usar en el tipo de dato que le estamos pasando
#METODO ES = Dato.metodo()

#Convierte a mayusculas
mayus = cadena1.upper() 

#Convierte a minusculas
minus = cadena1.lower() 

#Convierte la primera en mayusculas
mayusPri = cadena1.capitalize() 

#Buscamos una cadena en otra cadena. Cuando no encuentra una coincidencia devuelve -1
busqueda_find = cadena1.find("") 

#Funcionan igual, solo que cuando no encuentra una coincidencia nos tira una exepcion y no funciona el codigo
busqueda_index = cadena1.index("J") 

#Si es numerico devuelve true
es_numerico = cadena1.isnumeric()

#Si es alfa numerico devuelve true
es_alfanumerico = cadena1.isalpha()

#Buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")

#Si es alfa numerico devuelve true
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es cierto nos devuelve true
empieza_con = cadena1.startswith("Joa")

#Verificamos si una cadena termina con otra cadena dada, si es cierto nos devuelve true
termina_con = cadena1.endswith("quin")

#Remplaza un pedazo de la cadena dada por otra dada
cadena_nueva = cadena1.replace("Joaquin", "Joaquin Puertas")

#Separar cadenas con la cadena que le pasemos
cadena_separada = cadena2.split(",")

print(cadena_separada[0])

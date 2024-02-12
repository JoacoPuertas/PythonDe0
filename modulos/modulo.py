#Importando modulos
#Importa las funciones que tengamos en algun modulo
from modulo_saludar import saludar as formal, saludar_raro as raro

#Importa el modulo que luego podemos usar asi: saludos.saludar() para llamar a la funcion
# as lo que hace es llamar al modulo o funcion con el nombre que queramos en este modulo
import modulo_saludar as saludos

Saludo_formal = formal("Joaquin")
Saludo_raro = raro("ani")

print(Saludo_formal)
print(Saludo_raro)

#Imprime en la consola el nombre del modulo que usamos
print(saludos.__name__)
#En caso de tener que importar saludar estando en la misma ruta pero en distinta carpeta seria:

#import funciones_buenas.saludar as m_saludar
#from funciones_buenas.saludar import saludar as formal

#print(formal("Joaquin"))

#Como está en otra ruta es asi:
import sys

sys.path.append("c:\\Users\\Joaco\\My project\\PythonDe0\\funciones_buenas")

import saludar as saludito

print(saludito.saludar("Joaquin"))
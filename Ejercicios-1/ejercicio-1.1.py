#Promedio de duracion
curso_min = 2.5
curso_max = 7
curso_promedio = 4
dalto_curso = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5 
#Diferencias de duracion
diferencia_con_min = 100 - dalto_curso / curso_min * 100
diferencia_con_max = round(100 - dalto_curso / curso_max * 100,2)
diferencia_con_promedio = 100 - dalto_curso / curso_promedio * 100


print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento")
print(f"El curso de Dalto dura un  {diferencia_con_promedio}% menos que el promedio")
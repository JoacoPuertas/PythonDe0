ingreso_mensual = 81000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    print("estas bien en cualquier parte del mundo")
    if ingreso_mensual - gasto_mensual < 0: 
        print("Estas en deficit")
    if ingreso_mensual - gasto_mensual > 3000:
        print("estas hecho un toro")
    else:
        print("Hay que ver si llegas a fin de mes")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("estas bien en Argentina")
    
elif ingreso_mensual > 200:
    print("estas bien en Venezuela")

else:
    print("sos pobre")
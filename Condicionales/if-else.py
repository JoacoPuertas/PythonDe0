nombre_almacenado = "JoacoPuertas"
contraseña_almacenada = "JoacoBoca123"

usuario_escrito = "JoacoPuertas" + "JoacoBoca123"

if usuario_escrito == nombre_almacenado + contraseña_almacenada:
    print("INICIANDO SESIÓN...")
else:
    print("Nombre de Usuario o contraseña incorrecta")
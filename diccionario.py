# Crear un diccionario
puntajes = {'Juan': 95, 'María': 87, 'Pedro': 78, 'Ana': 92}

# Acceder a valores por clave
print(puntajes['María'])

# Modificar valores
puntajes['Pedro'] = 82
print(puntajes)

# Agregar nuevos elementos
puntajes['Carlos'] = 88
print(puntajes)

# Eliminar elementos
del puntajes['Ana']
print(puntajes)
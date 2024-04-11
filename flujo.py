inventario = {'manzanas': 10, 'bananas': 5, 'naranjas': 3, 'peras': 7 }

def gestion_inventario(accion, articulo, cantidad = 0):
    if accion == 'agregar':
        if articulo in inventario:
            inventario[articulo] += cantidad
        else:
            inventario[articulo] = cantidad
    elif accion == 'quitar':
        if articulo in inventario and inventario[articulo] >= cantidad:
            inventario[articulo] -= cantidad
        else:
            print('No se puede realizar la acción')
    elif accion == 'buscar':
        if articulo in inventario:
            return inventario[articulo]
        else:
            return None
    else:
        print('Acción no reconocida')
        
gestion_inventario('agregar', 'manzanas', 5)
print(inventario)

gestion_inventario('quitar', 'naranjas', 2)
print(inventario)

print(gestion_inventario('buscar', 'peras'))
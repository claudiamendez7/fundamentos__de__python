def linear_search(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Ejemplo
numeros = [64, 34, 25, 12, 22, 11, 90]
elemento_buscado = 20
indice = linear_search(numeros, elemento_buscado)
if indice != -1:
    print(f"El elemento {elemento_buscado} se encuentra en el índice {indice}.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")
    
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Ejemplo
numeros = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numeros)
print(numeros)

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1 ] = lista[j]
            j -= 1
        lista[j + 1] = key

# Ejemplo
numeros = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(numeros)
print(numeros)

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

# Ejemplo
numeros = [64, 34, 25, 12, 22, 11, 90]
selection_sort(numeros)
print(numeros)

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
            
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


# Ejemplo O(n log n)
numeros = [64, 34, 25, 12, 22, 11, 90]
ordenados = merge_sort(numeros)
print(ordenados)

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista [len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    
    return quick_sort(izquierda) + medio + quick_sort(derecha)

# Ejemplo O(n**2)
numeros = [64, 34, 25, 12, 22, 11, 90]
ordenados = quick_sort(numeros)
print(ordenados)
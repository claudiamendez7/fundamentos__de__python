def ordenar_por_burbuja(numeros):
    """Ordena una lista de números de menor a mayor usando el algoritmo de ordenación por burbuja."""
    intercambios_hechos = True
    while intercambios_hechos:
        intercambios_hechos = False
        for i in range(len(numeros) - 1):
            if numeros[i] > numeros[i + 1]:
                numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
                intercambios_hechos = True
                
numeros = [5, 2, 4, 6, 1, 3]

ordenar_por_burbuja(numeros)

print(numeros)                
    
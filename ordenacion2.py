import random

numeros = [random.randint(1, 100) for _ in range(20)]
print(f"Lista desordenada: {numeros}")

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
bubble_sort(numeros)
print(f"Lista ordenada: {numeros}")
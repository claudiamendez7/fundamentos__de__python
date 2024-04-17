discos = [
    {"nombre": "Escape the Era", "artista": "Dreamcatcher",
     "canciones": [("Intro", 260), ("You & I", 182), ("Which a star", 167), ("Scars", 152), ("Mayday", 140)],
     "stock": 5},
    {"nombre": "Square up", "artista": "Blackpink",
     "canciones": [("Ddu-Ddu-Ddu", 190), ("Forever Young", 181), ("Really", 231), ("See you later", 122)],
     "stock": 3},
    # Más discos
]

def buscarDisco(discos, nombre=None, artista=None):
    resultados = []
    for disco in discos:
        if nombre and disco["nombre"] == nombre:
            resultados.append(disco)
        if artista and disco["artista"] == artista:
            resultados.append(disco)
    return resultados

def buscarCancion(discos, nombre):
    resultados =[]
    for disco in discos:
        for cancion in disco["canciones"]:
            if cancion[0] == nombre:
                resultados.append((cancion, disco["nombre"], disco["artista"]))
    return resultados

def comprarDiscos(discos, nombre):
    for disco in discos:
        if disco["nombre"] == nombre and disco["stock"] > 0:
            disco["stock"] -= 1
            print(f"Has comprado {nombre}. Quedan {disco['stock']} en stock.")
            return
    print(f"No se pudo completar la compra de {nombre}.")
        
def bubbleSortDiscos(discos):
    n = len(discos)
    for i in range(n):
        for j in range(0, n-i-1):
            if discos[j]["nombre"] > discos[j+1]["nombre"]:
                discos[j], discos[j+1] = discos[j+1], discos[i]

def buscarDiscoParcial(discos, nombreParcial, indice=0):
    if indice == len(discos):
        return None
    if nombreParcial in discos[indice]["nombre"]:
        return discos[indice]
    return buscarDiscoParcial(discos, nombreParcial, indice+1)

print(buscarDisco(discos, nombre="Escape the Era"))
print(buscarCancion(discos, "Mayday"))
comprarDiscos(discos, "Escape the Era")
comprarDiscos(discos, "Square up")
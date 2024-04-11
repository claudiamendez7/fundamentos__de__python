musica = [('Yellow Submarine', 'The Beatles', 9.2),
          ('Let it Be', 'The Beatles', 10.2),
          ('Hey Jude', 'The Beatles', 8.2),
          ('A Day in the Life', 'The Beatles', 9.2),
          ('Stairway to Heaven', 'Led Zeppelin', 7.5),
          ('Enter Sandnman', 'Metallica', 8.5)]

def buscar_cancion(nombre):
    for cancion in musica:
        if cancion [0] == nombre:
            return cancion
    return None

def buscar_por_artista(artista):
    canciones_artista = []
    for cancion in musica:
        if cancion [1] == artista:
            canciones_artista.append(cancion)

    return canciones_artista

print(buscar_cancion('Hey Jude'))
print(buscar_cancion('Let it Be'))
print(buscar_por_artista('The Beatles'))
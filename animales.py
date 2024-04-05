class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def hacer__sonido(self):
        raise NotImplementedError("El método es implementado por las subclases")
        
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        
    def hacer__sonido(self):
        return "¡Guau, guau!"
    
   
perro = Perro("Oliver", 1, "Criollo")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
        
    def hacer__sonido(self):
        return "¡Miau, miau!"
    
gato = Gato("Tom", 2, "Gris y blanco")

def presentar_animal(animal):
    if isinstance(animal, Perro):
        print(f"Raza: {animal.raza}")
    elif isinstance(animal, Gato):
        print(f"Color: {animal.color}")
    print(f"Nombre: {animal.nombre}")
    print(f"Edad: {animal.edad}")
    print(f"Sonido: {animal.hacer__sonido()}")
    
presentar_animal(perro)
print("---")
presentar_animal(gato)


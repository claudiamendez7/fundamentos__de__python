def main():
    shopping_listas = []
    
    while True:
        print("\n---Lista de Compras---")
        print("1. Agregar artículo")
        print("2. Eliminar artículo")
        print("3. Ver lista")
        print("4. Salir")
        
        option = input("Por favor introduzca una opción: ")
        
        if option == "1":
            item = input("Introduce el nombre del artículo que quieres agregar: ")
            shopping_listas.append(item)
        elif option == "2":
            item = input("Introduce el nombre del artículo que quieres eliminar: ")
            if item in shopping_listas:
                shopping_listas.remove(item)
        elif option == "3":
            print("\nTu lista de compras es: ")
            for item in shopping_listas:
                print(" - " + item)
        elif option == "4":
            break
        else:
            print("Opción Inválida. Por favor intenta de nuevo")
            
if __name__ == "__main__":
    main()
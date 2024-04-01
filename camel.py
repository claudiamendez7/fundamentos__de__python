camel_case = input("Ingrese una variable en camel case: ")

snake_case = ""

for i in range (len(camel_case)):
    
    if camel_case[i].isupper():
        
        snake_case += "_" + camel_case[i].lower()
    else:
        
        snake_case += camel_case[i]
        
print("El nombre de la variable en snake case es: ", snake_case)
        
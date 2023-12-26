### Loops ###

cont = 1
while cont < 11:
    print(cont)
    cont += 1
else:
    print("Ya no cumplo la condición del bucle")

my_condition = 100
while my_condition>=0:
    if my_condition % 2 == 0:
        print(f"{my_condition} es par")
        if my_condition == 50:
            break #Salir del bucle
    else:
        print(f"{my_condition} es impar")
    my_condition -= 1



# For
    
my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print(i)


my_tuple = ("Caballo","Oveja","Tigre")
for animal in my_tuple:
    print(animal)

my_other_dict = {
    "Nombre":"Sergio", 
    "Apellido": "Marín", 
    "Edad":36,
    "Lenguajes": {"Python", "Swift", "Kotlin"}
    }

print("#####################")
for data in my_other_dict:
    print(f"{data}:{my_other_dict.get(data)}")
    if my_other_dict.get(data)==36:
        print("La clave es Edad y paro el bucle")
        break
else:
    print("Bucle for para el diccionario ha finalizado")
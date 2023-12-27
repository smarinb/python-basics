### Functions ###
def mi_function():
    print("Hola mundo desde una función!")


def mi_suma(num1,num2):
    return num1 + num2

def mi_suma_dos(num1,num2):
    print(num1 + num2)


mi_function()

print(mi_suma(3,5))
print(mi_suma(3.9,5))



mi_suma_dos(40,50)

def print_name(name,surname):
    print(f"{name} {surname}")

print_name("Sergio","Marin")
print_name(surname="Sergio",name="Marin") #Puedo cambiar el orden



def print_name_default_value(name,surname,alias = "Sin alias"): #Parametro por defecto si no le paso ese parametro
    print(f"{name} {surname} alias = {alias}")

print_name_default_value("Sergio", "Marín", "Sergi")
print_name_default_value("Sergio", "Marín")


def print_texts(*texts): #mas de un parametro
    for text in texts:
        print(text.upper())

print_texts("Hola")
print_texts("Hola","Sergio")
### Conditionals ###

my_condition = False

if my_condition:
    print("Se ejecuta la condicion del IF")


my_condition = 51 * 2

if my_condition > 8 and my_condition <= 10:
    print("Mi condición es mayor que 8 y menor o igual que 10")
elif my_condition<=100:
    print("Mi condicion es menor que 8 o mayor que 10 y menor o igual que 100")
else:
    print("My condición es menor que 8 o mayor que 100")



my_string = "Sergio"
if not my_string:
    print("Mi cadena de texto no es vacia")
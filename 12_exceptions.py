### Exceptions ###

number_one = 5
number_two = 1

number_two = "2"

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
    print(number_one + int(number_two))
except TypeError:
    print("Se ha producido un TypeError")
else:
    #Se ejecuta si no se produce excepción
    pass
finally:
    #Se ejecuta siempre
    print("La ejecución continua")

print("######################################")
try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
    print(number_one + int(number_two))
except TypeError as error:
    print(error)
except Exception as error:
    print(error)
else:
    #Se ejecuta si no se produce excepción
    pass
finally:
    #Se ejecuta siempre
    print("La ejecución continua")



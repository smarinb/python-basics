### Classes ###

from typing import Any


class MyEmptyPerson: #Camel case 
    pass

class Person:
    def __init__(self, name, surname, alias ="Sin Alias"): #Constructor
        self.__name = name #atributo privado
        self.surname = surname #atributo publico
        self.alias = alias #atributo publico
        self.full_name = f"{name} {surname} ({alias})"
    

    def walk(self):
        print(f"{self.full_name} esta caminando")

    def get_name(self): #Getter
        return self.__name
    
    def set_name(self,name):
        self.__name = name

my_person = Person("Sergio","Marín","Ciervo") #Crear un objeto de tipo Person
my_person.walk()

my_person.alias = 777 #cambio el alias

my_person.set_name("Cristina")

print(f"Mi nombre es {my_person.get_name()} y mi apellido es {my_person.surname} y mi nombre completo es: {my_person.full_name} y mi alias es: {my_person.alias}")

print(type(Person))
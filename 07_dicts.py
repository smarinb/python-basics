### Dicts ###

my_dict = {}
print(type(my_dict))

my_other_dict = dict()


my_dict = {"Nombre":"Sergio", "Apellido": "Marín", "Edad":36}
print(my_dict)


my_other_dict = {
    "Nombre":"Sergio", 
    "Apellido": "Marín", 
    "Edad":36,
    "Lenguajes": {"Python", "Swift", "Kotlin"}
    }

print(my_other_dict)


print(type(my_other_dict.get("Lenguajes")))

print(my_other_dict.get("Lenguajes"))

print(f"M apellido es {my_other_dict["Apellido"]}")

my_other_dict["Experiencia"] = "Junior" #Add element key:value
print(my_other_dict)

#Methods of Dicts
my_other_dict.pop("Experiencia")
print(my_other_dict)

print("Nombre" in my_other_dict)

print(my_other_dict.items())

print(my_other_dict.keys())
print(my_other_dict.values())
my_new_dict = dict.fromkeys("Nombre","Apellido")
print(my_new_dict)
print(type(my_other_dict.values()))



my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)


### Sets ###
#No es una estructura ordenada
#No tiene datos repetidos

my_set = set()

print(type(my_set))

my_other_set = {"Sergio","Marín",36}
print(type(my_other_set))

print(len(my_other_set))


#Methods of Sets
my_other_set.add("Barberá")
print(my_other_set)
my_other_set.add("Barberá")
print(my_other_set)

print("Barberá" in my_other_set) #True
print("Gonzalez" in my_other_set) #False

my_other_set.remove("Barberá")
print(my_other_set)

my_other_set.pop()
print(my_other_set)

my_other_set.clear()


my_set = {"Cristina", "Reyes", 37}

#my_list = list(my_set) #NO RECOMENDADO: en cada ejecución la lista tendrá un orden distinto

#print(my_list)

my_other_set = {"Kotlin", "Swift" , "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union({"Pascal","C#"}))

print(my_new_set)

my_set_uno = {1,2,3}
my_set_dos = {1,2,3,4,5,6}

my_dif_set = my_set_uno.difference(my_set_dos)

print(my_dif_set)

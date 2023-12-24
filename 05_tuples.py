### Tuples ###
#En las tuplas no se pueden modificar elementos ya asignado
#my_tuple[2]="Cambiar" No te deja cambiar es inmutable


my_tuple = tuple()

my_other_tuple = ()

my_tuple = (36, 1.93, "Sergio", "Marín")
print(type(my_tuple))

print(my_tuple[-1])

print(my_tuple.count("Sergio"))

my_tuple = (36, 1.93, "Sergio", "Marín","Barberá","Sergio")
print(my_tuple)

print(my_tuple.index("Sergio"))#2


my_other_tuple = (27, 36 , 37, 20)
print(my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[1:4])

my_list_tuple = list(my_sum_tuple) #tuple to list
print(type(my_list_tuple))
print(my_list_tuple)
my_list_tuple[1] = 1.92
print(my_list_tuple)
my_list_tuple = tuple(my_list_tuple)
print(type(my_list_tuple))
print(my_tuple)
del my_tuple #delete the variable
#print(my_tuple) error



### Lists ###

my_list = list()
my_other_list = []

my_list = [24,54,3,80,91]

my_other_list = [36, 1.92, "Sergio", "Marín"]


print(len(my_list))

print(my_other_list)


print(type(my_other_list),type(my_other_list))


print(my_other_list[3])
print(my_other_list[-2])

print(my_other_list.count(3)) #Count then number of times appears number: 3 --> 2

age, height, name, surname = my_other_list

print(my_other_list)
print(age)#3


print(my_list + my_other_list)
print(my_other_list + my_list)


print(type(my_list))
my_list = "Sergio"
print(type(my_list))

my_list = list(my_list) #String to List
print(my_list)


#Methods in lists

my_other_list.append("Ibermatica") #add element ends
print(my_other_list)

my_other_list.insert(4,"Barbera") #add element in index
print(my_other_list)


my_other_list.remove("Ibermatica") #remove the element passed
print(my_other_list)


my_list.append('o')
print(my_list)

my_list.remove('o') #remove the first coincidence
print(my_list)


my_list.pop() #remove the last element by default
print(my_list)

my_list.pop(2)
print(my_list)#Segi


del my_list[2]#Sei
print(my_list)


my_list[1]='o'#Soi
print(my_list)




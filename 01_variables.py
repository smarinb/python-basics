#Variables


my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)


print(my_string_variable,my_int_variable,my_bool_variable)

my_int_to_string_variable = str(my_int_variable) #str convert int in String

print(type(my_int_to_string_variable)) 

print(type(print())) #type of print is NoneType

#len function
print(len(my_string_variable)) #length of string 


print("Este es el varlo de 'my_bool_variable': ", my_bool_variable)


#How declare variables in the same line
name, last_name, age = "Sergio","Marín",36
print("Me llamo:",name,last_name,"y mi edad es:",age)
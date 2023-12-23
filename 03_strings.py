### Strings ###

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

#\t tabulación
my_tab_string = "\tEmpiezo tabulando el string"
print(my_tab_string)

my_scape_string = "\\tEste es un String \nescapado"
print(my_scape_string)

# \ -> to scape

### Formate Strings ###


name, surname, age = "Sergio","Marín",36
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age)) 
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") 



#Desempaquetado de caracteres
languaje = "python"
a, b, c, d , e , f = languaje
print(a)
print(b)

languaje_slice = languaje[1:3]
print(languaje_slice)

languaje_slice = languaje[1:]
print(languaje_slice)

languaje_slice = languaje[-2]
print(languaje_slice)

#Reverse

reversed_languaje = languaje[::-1]
print(reversed_languaje)

pto = languaje[0:6:2] 
print(pto) # Pto


#Methods with strings


print(languaje.capitalize())
print(languaje.upper())
print(languaje.count("t"))
print(languaje.find("p"))
print("6".isnumeric())
print(languaje.upper())
print(languaje.startswith("p"))
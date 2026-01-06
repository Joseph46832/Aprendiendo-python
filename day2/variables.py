# Dia 2: 30 Days of Python Programming
# Autor: Joseph Marin
# Description: Variables, data types, operators and basic input

#Agregamos varias variables

nombre, apellido, nombre_completo, pais, ciudad, edad, año, casado, is_true, is_light_on = "Joseph", "Marin", "Joseph Marin", "Colombia", "Cali", 18, 2026, False, False, True

#Vemos el tipo de texto ya sea string, entero y asi

print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(casado))
print(type(is_light_on))
print(type(is_true))

print("Tu nombre tiene una longitud de:",len(nombre))
print("Tu apellido tiene una longitud de:", len(apellido))

num_one = 5
num_two = 4

valor_total = num_one + num_two
valor_diff = num_one - num_two
valor_divid = num_one/num_two
valor_mult = num_two * num_one
valor_remainder= num_two%num_one
valor_exp= num_one ** num_two
valor_divfloor= num_one//num_two



#Radio de un circulo

radius = 30
pi = 3.1416

area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Area:", area_of_circle)
print("Circunferencia:", circum_of_circle)

radius = float(input("Dime el radio del círculo: "))
pi = 3.1416

area_of_circle = pi * radius ** 2

print("El área del círculo es:", area_of_circle)



#Pedimos nombres y apellidos

nombre_inp = input ("Hola :D Regalame tu nombre: ")
apellido_inp = input ("Ahora tu apellido, es para una tarea: ")
edad_inp = int(input ("No te molesto mas, cual es tue edad: "))

print(f"Holaaaaa eres {nombre_inp} {apellido_inp} y tienes la maravillosa edad de {edad_inp},años de edad, muchisimas gracias!!!")
print("ahora veremos cual es mas largo, si tu apellido o tu nombre")

#Comparacion de lengitud nombre y apellido

if len(nombre_inp)>len(apellido_inp):
    print("Oyeee tu nombre es mas largo que tu apellido")
elif len(apellido_inp)>len(nombre_inp):
    print("Tu apellido es mas largo que tu nombre")
else:
    print("Ambos, tu nombre y apellido son de la misma longitud")


#Vemos los valores de los resultados numericos

print(valor_total)
print(valor_remainder)
print(valor_mult)
print(valor_exp)
print(valor_divid)
print(valor_divfloor)
print(valor_diff)

help('keywords')

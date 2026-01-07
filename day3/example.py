# VARIABLES BÁSICAS Y TIPOS DE DATOS

my_age = 18
my_age = int(my_age)

my_height = 1.68
my_height = float(my_height)

complex_number = 3 + 4j
complex_number = complex(complex_number)


# ÁREA Y PERÍMETRO DE UN TRIÁNGULO


print("Vamos a calcular el area de un triangulo")
base_triangulo = float(input("Cual es la base del triangulo?: "))
altura_triangulo = float(input("Cual es la altura del triangulo?: "))
print("El area del triangulo es: ", 0.5 * base_triangulo * altura_triangulo)

print("Ahora vamos a calcular el perimetro de un triangulo")
lado_a = float(input("Cual es el lado a del triangulo?: "))
lado_b = float(input("Cual es el lado b del triangulo?: "))
lado_c = float(input("Cual es el lado c del triangulo?: "))
print("El permietro de nuestro triangulo es:", lado_a + lado_b + lado_c)


# ÁREA Y PERÍMETRO DE UN RECTÁNGULO

print("Ahora vamos a calcular el area y perimetro de un rectangulo")
lado_largo_retalngulo = float(input("Cuan largo es el rectangulo?: "))
lado_ancho_retalngulo = float(input("Cual es el ancho del rectangulo?: "))
print("El area del rectangulo es:", lado_largo_retalngulo * lado_ancho_retalngulo)
print("El perimetro del rectangulo es:", 2 * (lado_largo_retalngulo + lado_ancho_retalngulo))


# PENDIENTE E INTERSECCIONES DE y = 2x - 2

pendiente_1 = 2

x = 0
y_intercept = 2 * x - 2

y = 0
x_intercept = 2 / 2

print("Pendiente:", pendiente_1)
print("y-intercept:", (0, y_intercept))
print("x-intercept:", (x_intercept, 0))


# PENDIENTE ENTRE DOS PUNTOS Y DISTANCIA EUCLIDIANA

x2, y2 = 6, 10
x1, y1 = 2, 2

y_diff = y2 - y1
x_diff = x2 - x1

pendiente_2 = y_diff / x_diff

print("La pendiente entre los puntos (2, 2) y (6, 10) es:", pendiente_2)

import math
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean distance:", distance)


# COMPARACIÓN DE PENDIENTES

if pendiente_1 > pendiente_2:
    print("La pendiente 1 es mayor que la pendiente 2")
elif pendiente_1 < pendiente_2:
    print("La pendiente 2 es mayor que la pendiente 1")
else:
    print("Las dos pendientes son iguales")

if pendiente_1 == pendiente_2:
    print("Las dos lineas son paralelas")
else:
    print("Las dos lineas no son paralelas")


# ECUACIÓN y = x^2 + 6x + 9 HALLAR CUANDO y=0

for x in range(-10, 1):
    y = x**2 + 6*x + 9
    if y == 0:
        print("El valor de x que hace que y sea 0 es:", x)


# STRINGS, LONGITUDES Y COMPARACIONES

print("La palabra 'python' tiene", len("python"), "caracteres.")
print("La palabra 'dragon' tiene", len("dragon"), "caracteres.")

print(len("python") > len("dragon"), "No son la misma longitud. (Afirmacion falsa para el ejercicio)")

print("on" in "python", "'on' esta en 'python'?" and "on" in "dragon", "'on' esta en 'dragon'?")
print("Ambas afirmaciones son verdaderas.")

print("I hope this course is not full of jargon.", "jargon" in "I hope this course is not full of jargon.")

print("no" in "python" and "no" in "dragon", "'no' esta en 'python'?" and "'no' esta en 'dragon'?")


# CONVERSIÓN DE TIPOS

python_caracteres = print("La palabra python tiene", len("python"), "caracteres.")

python_caracteres = len("python")
python_caracteres_float = float(python_caracteres)
python_caracteres_string = str(python_caracteres)


# PAR O IMPAR

numero = int(input("Hola! Vamos a ver si un numero es par o impar, dame un numero que quieras pero que sea entero: "))
numero_par_o_impar = numero % 2

if numero_par_o_impar == 0:
    print("Tu numero es par!!!")
elif numero_par_o_impar == 1:
    print("Tu numero es impar... que triste")


# DIVISIONES, TIPOS Y COMPARACIONES

floor_division = 7 // 3
print(floor_division)
print(f"{floor_division} is 2.7", "No, no son lo mismo")

print(type("10") == type(10))
print(9.8 == 10, "Falso, no lo es")


# CÁLCULO DE SUELDO

horas_trabajo = int(input("Hola!!! Cuantas horas trabajas??? "))
paga_por_hora = int(input("cuanto te pagan la hora?"))
sueldo = horas_trabajo * paga_por_hora
print("Tu ganas alrededor de: ", sueldo)


# SEGUNDOS VIVIDOS

años_vividos = int(input("Cuantos años has vivido?" ))
años_en_segunos = años_vividos * 31536000
print("Has vivido un total de ", años_en_segunos, "segundos de vida")


# TABLA DE POTENCIAS

for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)

# ==============================
# 1. Concatenación de strings
# ==============================

uno = "Thirty"
dos = "days"
tres = "of"
cuatro = "python"

palabra_completa = uno + " " + dos + " " + tres + " " + cuatro
print(palabra_completa)

one = "Coding"
two = "for"
three = "all"

whole_world = one + " " + two + " " + three
print(whole_world)


# ==============================
# 2. Variable company y métodos
# ==============================

company = "Coding For All"

print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())


# ==============================
# 3. Slicing y búsqueda
# ==============================

print(company[0:6])
print(company.find("Coding"))
print(company.replace("Coding", "Python"))
print(company.replace("All", "Everyone"))
print(company.split())


# ==============================
# 4. Split con coma
# ==============================

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))


# ==============================
# 5. Indexación de caracteres
# ==============================

print("Coding For All."[14])
print("Coding For All."[10])

print("Python For Everyone"[0])
print("Python For Everyone"[7])
print("Python For Everyone"[11])

print("Coding For All"[0])
print("Coding For All"[7])
print("Coding For All"[11])


# ==============================
# 6. index, find, rfind, rindex
# ==============================

print("Coding For All".index("C"))
print("Coding For All".index("F"))
print("Coding For All people".rfind("l"))

print("You cannot end a sentence with because because because is a conjunction".find("because"))
print(len("You cannot end a sentence with because because because is a conjunction"))
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))

print('You cannot end a sentence with because because because is a conjunction'[31:54])


# ==============================
# 7. startswith / endswith
# ==============================

print('Coding For All'.startswith("Coding"))
print('Coding For All'.endswith("Coding"))


# ==============================
# 8. strip e identificadores
# ==============================

print('   Coding For All   '.strip())
print("thirty_days_of_python".isidentifier())


# ==============================
# 9. join
# ==============================

print("#".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))


# ==============================
# 10. Secuencias de escape
# ==============================

print("I \nam \nenjoying \nthis \nchallenge.", "\nI \njust \nwonder \nwhat \nis \nnext.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")


# ==============================
# 11. String formatting (área)
# ==============================

radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {area} meters square.")


# ==============================
# 12. Operaciones con formatting
# ==============================

print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {round(8 / 6, 2)}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")

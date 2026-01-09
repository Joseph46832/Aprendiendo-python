# Level 1 Exercises

# 1. Declarar una lista vacía
lista_vacia = []
print("Lista vacía:", lista_vacia)

# 2. Declarar una lista con más de 5 items
Materias = ["Matemáticas", "Física", "Química", "Biología", "Programación"]

# 3. Encontrar la longitud de la lista
print("Tenemos un total de", len(Materias), "materias.")

# 4. Obtener el primer, medio y último item de la lista
print(Materias[0])  # Primer item
print(Materias[2])  # Item del medio
print(Materias[4])  # Último item

# 5. Declarar una lista llamada mixed_data_types con diferentes tipos de datos
mixed_data_types = ["Joseph", 18, 1.68, False, "Carrera 28"]

# 6. Declarar la lista it_companies con valores iniciales
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimir la lista
print(f"Estas son nuestras compañias: {it_companies}")

# 8. Imprimir el número de compañías
print(f"Nuestras compañias son confiables y tenemos disponibles la magnifica cantidad de {len(it_companies)} compañias.")

# 9. Imprimir la primera, media y última compañía
print(it_companies[0])  # Primera
print(it_companies[2])  # Media
print(it_companies[6])  # Última

# 10. Modificar uno de los elementos de la lista
it_companies[4] = "Instagram"
print(f"Compañías actualizadas: {it_companies}, se nos fue IBM :(")

# 11. Agregar una compañía al final
it_companies.insert(5, "IBM")
print(f"Compañías actualizadas: {it_companies}, IBM ha regresado :)")

# 12. Cambiar un nombre de compañía a mayúsculas (excepto IBM)
it_companies[0] = "FACEBOOK"
print(f"Compañías en mayúsculas: {it_companies}")

# 13. Unir las compañías con un string "#;  "
result = '#;  '.join(it_companies)
print(f"Compañías separadas por #; : {result}")

# 14. Verificar si cierta compañía existe en la lista
print("Existe amazon en la lista de comapañias", "Amazon" in it_companies)

# 15. Ordenar la lista alfabéticamente
it_companies.sort()
print(f"Compañías ordenadas alfabéticamente: {it_companies}")

# 16. Ordenar la lista en orden inverso
it_companies.sort(reverse=True)
print(f"Compañías ordenadas alfabéticamente en orden inverso: {it_companies}")

# 17. Slice: las primeras 3 compañías
it_companies.sort()
print(it_companies[0:3])

# 18. Slice: las últimas 3 compañías
print(it_companies[-3:])

# 19. Slice: la compañía del medio
print(it_companies[3])

# 20. Eliminar la primera compañía
it_companies.remove(it_companies[0])
print(f"Compañías después de eliminar la primera: {it_companies}")

# 21. Eliminar la compañía del medio
it_companies.remove(it_companies[2])
print(f"Compañías después de eliminar la del medio: {it_companies}")

# 22. Eliminar la última compañía
it_companies.pop()
print(f"Compañías después de eliminar la última: {it_companies}")

# 23. Eliminar todas las compañías
it_companies.clear()
print(f"Compañías después de limpiar la lista: {it_companies}")

# 24. Destruir la lista
del it_companies
print(f"Lista de compañías eliminada. (Saldria error si ponemos print(it_companies))")

# 25. Unir listas front_end y back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_and_back = front_end + back_end

# 26. Copiar la lista unida y agregar Python y SQL después de Redux
security_copy = front_and_back.copy()
print(front_and_back)
security_copy.insert(5, "Python")
security_copy.insert(6, "SQL")
print(security_copy)


# Level 2 Exercises

# Lista de edades de 10 estudiantes
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar la lista y encontrar min y max
ages.sort()
print("Edad mínima:", ages[0])
print("Edad máxima:", ages[-1])

# Calcular edad promedio
print("Edad promedio", sum(ages)/len(ages))

# Edad media (mediana)
print("Edad media:", ages[6])

# Rango de edades
print("Rango de edades:", ages[-1]-ages[0])

# Lista de países
countries = [

  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# Encontrar el país mediano
print("El pais del medio:", countries[len(countries)//2])

# Dividir la lista de países en dos mitades
first_half_countries = countries[0:len(countries)//2+1]
second_half_countries = countries[len(countries)//2+1:]
print(len(countries))
print(len(first_half_countries))
print(len(second_half_countries))

#Verificacion de suma primer mitad + segunda mitad = lista completa
print("Acaso la suma de la primera mitad y la segunda mitad concuerda con la cantidad de paises de la lista completa???:",len(first_half_countries)+len(second_half_countries)==len(countries))
# Unpacking de una lista de países
countries_2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic = countries_2
print(scandic)
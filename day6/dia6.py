# 💻 Day 6 – Tuples & Lists Exercises

# =========================
# Level 1
# =========================

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create tuples for brothers and sisters
brothers = ("Juan", "Leon", "Francis", "Bill", "Louis", "Ellis", "Nick")
sisters = ("Zoey", "Rochelle", "Anya", "Maria")

# 3. Join brothers and sisters into siblings tuple
siblings = brothers + sisters

# 4. Print total number of siblings and their names
print(f"My siblings are a total of: {len(siblings)} and all their names are {siblings}")

# 5. Convert siblings tuple to list to modify it
siblings = list(siblings)

# 6. Add parents to the beginning of the list
siblings.insert(0, "Ethan")   # Father
siblings.insert(0, "Joyce")   # Mother

# 7. Assign the list to family_members
family_members = siblings
print(family_members)

# =========================
# Level 2
# =========================

# 8. Unpack parents and siblings
parent_1, parent_2, *siblings = family_members

# -------------------------
# Food tuples
# -------------------------

# 9. Create tuples for fruits, vegetables, and animals
fruits = ("Mango", "Strawberry", "Watermelonnnnnnnnnnnn")
vegetables = ("Tomato", "Onion", "Carrots")
animals = ("Lion", "Cats", "Dogs")

# 10. Join all food tuples into one tuple
food_stuff_tp = fruits + vegetables + animals

# 11. Convert food tuple to list
food_stuff_lt = list(food_stuff_tp)

# 12. Access elements using indexing and slicing
print(food_stuff_lt[4])
print(food_stuff_lt[0:2])

# 13. Delete the food list completely
del food_stuff_lt

# -------------------------
# Nordic countries
# -------------------------

# 14. Create nordic countries tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# 15. Check if specific countries exist in the tuple
print("Existe el pais Estonia en los paises nordicos?", "Estonia" in nordic_countries)
print("Existe el pais Islandia en los paises nordicos?", "Iceland" in nordic_countries)

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")

print(it_companies)

more_companies = {"Samsung", "Apple", "Xiaomi"}

it_companies.update(more_companies)

print(it_companies)

# What is the difference between remove and discard

it_companies.remove("Samsung")

print(it_companies)

it_companies.discard("Samsung")

print(it_companies)

# it_companies.remove("Samsung") if we try to do this we would get an error, but with discard it doesnt happen, thats the key and big difference 

A_B = A.union(B)

print(A_B)

print(A.intersection(B))

print("Is A a subset of B????", A.issubset(B))
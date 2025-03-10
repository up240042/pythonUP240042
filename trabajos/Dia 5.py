# 1 
lst = []

# 2
lst =["Luis", "Angel", "Alonso", "Fonseca", "OK", "ojo"]

# 3
print("")
print("ejercicio 3")

print(len(lst))

# 4
print("")
print("ejercicio 4")

pri, seg, ter, *algu, ulti = lst
print(ter)
print(ulti)

mid = lst[2]
las = lst[-1]
print(mid)
print(las)


# 5
print("")
print("ejercicio 5")

mixed_data_types = ["Luis", "18", "1.75", "sol", "casa"]

# 6
print("")
print("ejercicio 6")

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7
print("")
print("ejercicio 7")

print(it_companies)

# 8
print("")
print("ejercicio 8")

print(len(it_companies))

# 9
print("")
print("ejercicio 9")

p = it_companies[0]
m = it_companies[4]
u = it_companies[-1]
print(p, m, u)

# 10
print("")
print("ejercicio 10")

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[0] = "Python"
print(it_companies)
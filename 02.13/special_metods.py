# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)

# list = ["Marius", "Mindaugas", "Gabrielė", "Ieva", "Vladas"]

# print([name for name in list if len(name) >= 5])

#Create a dictionary with 5 kay:value pairs, Keys must be strings, values must be numbers double digits(int)
# Use dictionary comprehension to create a new dictionary where keys are the same keys as your currents ones just all cappital letters, 
# and values are in reverse order. (25 -> 52)
Greek = {
    "Alpha" : 12,
    "Beta" : 13,
    "Gamma" : 14,
    "Delta" : 15,
    "Epsilon" : 16
}

# Greek_Capital = {key.upper(): int(str(value)[::-1]) for key, value in Greek.items()}

# print(Greek_Capital)
# squares = {i : i * i for i in range(10) if i <=7}
# print(squares)
Greek_Capital = {}
for Greek, value in Greek.items():
    Greek_Capital[Greek.upper()] = int(str(value)[::-1])

print(Greek_Capital)


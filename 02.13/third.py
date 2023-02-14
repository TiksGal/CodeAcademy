# Given string: text = 'In this lecture we will review some additional 
# functionalities of python built-in data structures.' calculate how many words have letter 'e' in it.

text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# loop
words = text.split()
count = 0
for word in words:
    if 'e' in word:
        count += 1

print(count)

# comprehension

words = text.split()
count = len([word for word in words if 'e' in word])

print(count)

names_list = ["Marius", "Mindaugas", "Gabrielė", "Ieva", "Vladas"]
names_dict = {name: len(name) for name in names_list}

print(names_dict)

names_list = ["Marius", "Mindaugas", "Gabrielė", "Ieva", "Vladas"]
names_dict = {index: name for index, name in enumerate(names_list)}

print(names_dict)
# Given the same string as in previous exercise: calculate count of letters that have more than 5 characters.

text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
words = text.split()
count = 0
for word in words:
    if len(word) > 5:
        count += 1

print(count)

# comprehensive

text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
words = text.split()
count = len([word for word in words if len(word) > 5])

print(count)
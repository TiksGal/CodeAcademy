# Find all of the numbers from 1-1000 that are divisible by 6.

# comprehensive method
result = [i for i in range(1, 1001) if i % 6 == 0]
print(result)

# loop

result = []
for i in range(1, 1001):
    if i % 6 == 0:
        result.append(i)

print(result)


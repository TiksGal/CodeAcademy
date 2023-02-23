# Find all number from 1-1000 that have 9 in them.

result = [i for i in range(1, 1001) if '9' in str(i)]
print(result)

# loop

result = []
for i in range(1, 1001):
    if '9' in str(i):
        result.append(i)

print(result)
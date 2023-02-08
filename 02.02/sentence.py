sentences = input("This is a sample sentence.", "Another sample sentence here.", "A third sample sentence for you.", "Here is number four.", "And finally number five.")

# Split sentences into words and store in separate lists
word_lists = [sentence.split() for sentence in sentences]

# Sort word lists
word_lists.sort(key=len, reverse=False)

# Create 5 new lists with first, second, etc. indexed elements
lists = [[word[i] for word in word_lists] for i in range(2)]

# Print length of all list items
lengths = [len(lst) for lst in lists]
print("Lengths of list items:", lengths)

# Print longest and shortest list
longest = max(lengths)
shortest = min(lengths)
print("Longest list length:", longest)
print("Shortest list length:", shortest)   
sentences = []

# Ask for 5 sentences
for i in range(5):
    sentences.append(input("Enter sentence %d: " % (i + 1)))
    


# Find the length of each sentence
sentence_lengths = [len(sentence) for sentence in sentences]

# Print the length of each sentence
print("Length of sentences:", sentence_lengths)

# Find the longest and shortest sentences
longest = max(sentence_lengths)
shortest = min(sentence_lengths)

# Print the longest and shortest sentences
print("Longest sentence:", sentences[sentence_lengths.index(longest)])
print("Shortest sentence:", sentences[sentence_lengths.index(shortest)])
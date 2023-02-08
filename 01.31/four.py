text = input("Enter your text")


leet_speak = text.replace("a", "@").replace("A", "@").replace("n", "п").replace("N", "п").replace("t", "7").replace("T", "7").replace("s", "5").replace("S", "5")

print(leet_speak)
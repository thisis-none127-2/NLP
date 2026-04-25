import re

text = input("Enter text: ").lower()

words = re.findall(r'\b[a-z]+\b', text)

bigrams = []

for i in range(len(words) - 1):
    bigrams.append((words[i], words[i + 1]))

print("Bigrams:")
for bg in bigrams:
    print(bg)
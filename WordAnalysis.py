import re
from collections import Counter

text = input("Enter text: ").lower()

words = re.findall(r'\b[a-z]+\b', text)

word_count = len(words)
unique_words = len(set(words))
frequency = Counter(words)

print("Total Words:", word_count)
print("Unique Words:", unique_words)
print("Word Frequencies:")

for word, count in frequency.items():
    print(word, ":", count)
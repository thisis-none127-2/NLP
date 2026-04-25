import random

text = input("Enter text: ").lower().split()

word_map = {}

for i in range(len(text) - 1):
    key = text[i]
    value = text[i + 1]
    word_map.setdefault(key, []).append(value)

start_word = random.choice(text)
generated = [start_word]

for _ in range(9):
    current = generated[-1]
    if current in word_map:
        next_word = random.choice(word_map[current])
        generated.append(next_word)
    else:
        break

print("Generated Text:")
print(" ".join(generated))
lexicon = {
    "i": "PRON", "you": "PRON",
    "dog": "NOUN", "cat": "NOUN",
    "run": "VERB", "eat": "VERB",
    "fast": "ADV", "quickly": "ADV"
}

sentence = input("Enter sentence: ").lower().split()

for word in sentence:
    tag = lexicon.get(word, "UNK")
    print(word, "->", tag)
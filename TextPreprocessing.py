import re

stop_words = {
    "is", "am", "are", "was", "were", "the", "a", "an",
    "in", "on", "at", "to", "for", "of", "and", "or", "with"
}

def tokenize(text):
    return text.split()

def filtration(tokens):
    return [t for t in tokens if t.isalpha()]

def script_validation(tokens):
    return [t for t in tokens if re.match("^[a-zA-Z]+$", t)]

def remove_stopwords(tokens):
    return [t for t in tokens if t.lower() not in stop_words]

def stemming(tokens):
    suffixes = ["ing", "ed", "ly", "s"]
    result = []
    for word in tokens:
        for suf in suffixes:
            if word.endswith(suf) and len(word) > len(suf) + 2:
                word = word[:-len(suf)]
                break
        result.append(word)
    return result

text = input("Enter text: ")

tokens = tokenize(text)
filtered = filtration(tokens)
validated = script_validation(filtered)
no_stop = remove_stopwords(validated)
stemmed = stemming(no_stop)

print("Tokens:", tokens)
print("Filtered:", filtered)
print("Validated:", validated)
print("After Stopword Removal:", no_stop)
print("After Stemming:", stemmed)
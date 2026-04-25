sentence = input("Enter sentence: ").split()

names = {"John", "Alice", "Ravi"}
places = {"India", "Chennai", "London"}
orgs = {"Google", "Microsoft"}

for word in sentence:
    if word in names:
        print(word, "-> PERSON")
    elif word in places:
        print(word, "-> LOCATION")
    elif word in orgs:
        print(word, "-> ORGANIZATION")
    else:
        print(word, "-> O")
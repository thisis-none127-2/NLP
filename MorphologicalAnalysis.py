words = input("Enter words: ").split()

prefixes = ["un", "re", "in", "dis"]
suffixes = ["ing", "ed", "ly", "s"]

for word in words:
    pre = ""
    suf = ""
    root = word

    for p in prefixes:
        if word.startswith(p):
            pre = p
            root = word[len(p):]

    for s in suffixes:
        if root.endswith(s):
            suf = s
            root = root[:-len(s)]

    print("Word:", word, "| Prefix:", pre, "| Root:", root, "| Suffix:", suf)
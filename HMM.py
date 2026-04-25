states = ["N", "V"]

start_p = {"N": 0.6, "V": 0.4}

trans_p = {
    "N": {"N": 0.3, "V": 0.7},
    "V": {"N": 0.8, "V": 0.2}
}

emit_p = {
    "N": {"dog": 0.5, "barks": 0.1},
    "V": {"dog": 0.1, "barks": 0.6}
}

obs = input("Enter sentence: ").lower().split()

V = [{}]

for st in states:
    V[0][st] = start_p[st] * emit_p[st].get(obs[0], 0.01)

for t in range(1, len(obs)):
    V.append({})
    for st in states:
        V[t][st] = max(
            V[t-1][prev] * trans_p[prev][st] * emit_p[st].get(obs[t], 0.01)
            for prev in states
        )

for i in range(len(obs)):
    print(obs[i], "->", max(V[i], key=V[i].get))
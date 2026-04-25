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
path = {}

for st in states:
    V[0][st] = start_p[st] * emit_p[st].get(obs[0], 0.01)
    path[st] = [st]

for t in range(1, len(obs)):
    new_path = {}
    V.append({})
    for st in states:
        prob, state = max(
            (V[t-1][prev] * trans_p[prev][st] * emit_p[st].get(obs[t], 0.01), prev)
            for prev in states
        )
        V[t][st] = prob
        new_path[st] = path[state] + [st]
    path = new_path

prob, state = max((V[-1][st], st) for st in states)

for w, s in zip(obs, path[state]):
    print(w, "->", s)
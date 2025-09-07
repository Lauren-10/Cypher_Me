def markov_chain_solver(dice, k, iterations=150):
    names = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL",
             "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1",
             "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2",
             "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
    squares = {name: i for i, name in enumerate(names)}
    
    def find_next(current, prefix):
        for step in range(1, len(names) + 1):
            nxt = (current + step) % len(names)
            if names[nxt].startswith(prefix):
                return nxt
        return current
    
    next_r = [find_next(i, 'R') for i in range(len(names))]
    next_u = [find_next(i, 'U') for i in range(len(names))]
    
    def resolve(square, prob, probs):
        s = names[square]
        if s == "G2J":
            probs[squares["JAIL"]] += prob
        elif s.startswith("CC"):
            probs[squares["GO"]] += prob / 16
            probs[squares["JAIL"]] += prob / 16
            probs[square] += 14 * prob / 16
        elif s.startswith("CH"):
            moves = [
                squares["GO"], squares["JAIL"], squares["C1"], squares["E3"],
                squares["H2"], squares["R1"], next_r[square], next_r[square],
                next_u[square], (square - 3) % len(names)
            ]
            for move in moves:
                if names[move].startswith("CC") or names[move].startswith("CH"):
                    resolve(move, prob / 16, probs)
                else:
                    probs[move] += prob / 16
            probs[square] += 6 * prob / 16
        else:
            probs[square] += prob
    
    def get_transitions(square, roll):
        new = (square + roll) % len(names)
        probs = [0] * len(names)
        resolve(new, 1, probs)
        return [p / (dice ** 2) for p in probs]
    
    rolls = [d1 + d2 for d1 in range(1, dice +1) for d2 in range(1, dice +1)]
    size = len(names)
    p_matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for roll in rolls:
            transitions = get_transitions(i, roll)
            for j in range(size):
                p_matrix[i][j] += transitions[j]
    
    def mat_mult(m1, m2):
        return [[sum(m1[i][k] * m2[k][j] for k in range(size)) for j in range(size)] for i in range(size)]
    
    current = p_matrix
    for _ in range(iterations):
        current = mat_mult(current, p_matrix)
    
    stationary = current[0]
    sorted_squares = sorted([(prob, i) for i, prob in enumerate(stationary)], reverse=True)
    return [names[i] for _, i in sorted_squares[:k]]

n, k = map(int, input().split(","))
print(" ".join(markov_chain_solver(n, k)))
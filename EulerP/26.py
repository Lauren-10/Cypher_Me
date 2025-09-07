
def p29():
    dins = []
    
    for i in range(2,101):
        for j in range(2,101):
            if i**j not in dins:
                dins.append(i**j)
    return len(dins)

print(p29())

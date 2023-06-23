    n = int(input())
    w = input()
    print(w)
    weights = [int(x) for x in w.split[" "]]
    print(n, weights)
    weights.sort()
    
    # instability if i, j are single kayakers
def get_instability(i, j):
        test = list(weights)
        test.pop(i)
        test.pop(j)
        instability = 0
        for k in range(0, len(test) - 1, 2):
            instability += abs(weights[k] - weights[k+1])
        return instability
        
    instabilities = []
    for i in range(len(weights)):
        for j in range(len(weights)):
            if i == j:
                continue
            instabilities.append(get_instability(i, j))
    
    print min(instabilities)
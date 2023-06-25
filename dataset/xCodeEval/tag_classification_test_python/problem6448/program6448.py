    
def neighbors(state, n, a, b):
        for a_i in range(4 + 1):
            for b_i in range(2 + 1):
                if n >= a_i * a + b_i * b:
                    yield (state[0] + a_i, state[1] + b_i)
    
    n = int(input())
    a = int(input())
    b = int(input())
    
    state = (0, 0)
    final_state = (4, 2)
    
    explored = set()
    to_explore = [(0, state)]
    while to_explore:
        layer, state = to_explore.pop(0)
        if state == final_state:
            print(layer)
            exit()
        if state in explored:
            continue
        explored.add(state)
        for neighbor in neighbors(state, n, a, b):
            #print("%s -> %s") % (str(state), str(neighbor))
            to_explore.append((layer + 1, neighbor))
        
        
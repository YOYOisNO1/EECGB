    import sys
    
def get_current_state(deck1, deck2, n):
        res = "".join([str(x) for x in deck1]) + "-"+"".join([str(x) for x in deck2])
        return res
    n = int(sys.stdin.readline())
    player1 = ([int(x)-1 for x in sys.stdin.readline().split()])[1:]
    player2 = ([int(x)-1 for x in sys.stdin.readline().split()])[1:]
    current_state = get_current_state(player1, player2, n)
    nb_fights = 0
    visited = set()
    while len(player1) > 0 and len(player2) > 0 and current_state not in visited:
        visited.add(current_state)
        c1 = player1[0]
        c2 = player2[0]
        if c1 > c2:
            player2 = player2[1:]
            player1 = player1[1:] + [c2, c1]
        else:
            player1 = player1[1:]
            player2 = player2[1:] + [c1, c2]
        current_state = get_current_state(player1, player2, n)
        nb_fights += 1
    
    if len(player1) == 0:
        print(str(nb_fights) + " 2")
    elif len(player2) == 0:
        print(nb_fights + " 1")
    else:
        print(-1)
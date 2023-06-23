    import sys
    
def can_make_height(n_cards, k):
        multiplier = 3 * k
        constants = 2 * k - (3 * (k * (k-1))) / 2
        n_cards_required = 3 * ((k-1) * (k)) / 2 + 2 * k
        if n_cards_required <= n_cards:
            return ((n_cards - constants) % multiplier) == 0
        return False
    
def brute_force(n_base, n_cards, d=0):
        if n_cards == 0:
            heights.add(d)
        if n_cards <= 0:
            return
        if n_base <= 0:
            return
    
        for i in range(0, n_base):
            brute_force(i, n_cards - (3*i + 2), d+1)
    
    n_cards, r = int(sys.stdin.readline()), 0
    for i in range(1, n_cards):
        if can_make_height(n_cards, i):
            #print(i)
            r += 1
    print(r)
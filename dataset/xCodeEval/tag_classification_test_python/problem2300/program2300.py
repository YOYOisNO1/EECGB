def program2300():
    # https://codeforces.com/problemset/problem/431/B
    
    """
    Only one shower and multiple students
    
    Every morning there is a line of five people
    When the shower opens the first person in the line enters the shower
    When they finish the next person enters
    
    While waiting for the person in the shower
        Person 2i-1 talk to person 2i
    
    If i and j talk then
        * student i's happiness increases by g_ij
        * student j's happiness increases by g_ji
    
    Depending on the arrangement of the line find the maximum possible total happiness
    """
    
    import itertools
    
    n = 5
    
    g = []
    for i in range(n):
        g.append(list(map(int, input().split())))
    
    # Just check, there are only 120 permutation of 1 to 5 (n!)
    # To check is n^2 ?
    permutations = list(itertools.permutations(range(5)))
    
    max_happiness = 0  # We know happiness matrix has non negative entries
    for permutation in permutations:
        happiness = 0
        for t in range(n):  # On the first turn everyone is waiting, on turn n last person is in shower
            for i in range(t, n-1, 2):
                a, b = permutation[i], permutation[i+1]
                happiness += g[a][b] + g[b][a]
    
        if max_happiness < happiness:
            max_happiness = happiness
    
    print(max_happiness)
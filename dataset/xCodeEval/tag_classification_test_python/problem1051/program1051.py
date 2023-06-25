def program1051():
    import itertools
    import copy
    
    n=int(input())
    alice=list(map(int,input().split()))
    bob=list(map(int,input().split()))
    
    max_wins=0
    max_wins+=min(alice[0],bob[1])
    max_wins+=min(alice[1],bob[2])
    max_wins+=min(alice[2],bob[0])
    
    permutations=itertools.permutations(((0,0),(0,2),(1,1),(1,0),(2,2),(2,1)))
    min_wins=n
    for permutation in permutations:
        temp_alice=copy.deepcopy(alice)
        temp_bob=copy.deepcopy(bob)
        wins=n
        for combination in permutation:
            lower=min(temp_alice[combination[0]],temp_bob[combination[1]])
            temp_alice[combination[0]]-=lower
            temp_bob[combination[1]]-=lower
            wins-=lower
        min_wins=min(min_wins,wins)
    
    print(min_wins,max_wins)
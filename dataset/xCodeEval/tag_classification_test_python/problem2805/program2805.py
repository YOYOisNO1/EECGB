def program2805():
    from sys import stdin
    
    N = int(stdin.readline())
    X = int(stdin.readline())
    
    moves = [
        [0, 1, 2],
        [1, 0, 2],
        [1, 2, 0],
        [2, 1, 0],
        [2, 0, 1],
        [0, 2, 1]
    ]
    
    print(moves[N % len(moves)][X])
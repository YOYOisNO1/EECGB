def program2250():
    # cf 937 A 800
    n = int(input())
    A = [*map(int, input().split())]
    
    count = 0
    S = set(A)
    if 0 in S:
        S.remove(0)
    print(len(S))
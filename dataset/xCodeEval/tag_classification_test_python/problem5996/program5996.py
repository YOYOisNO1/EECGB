    import itertools
    
def main():
        A = tuple(map(int, input().split()))
    
        half = sum(A) / 2
        for i in itertools.combinations(A, 3):
            points = sum(i)
            if half == points:
                print('YES')
                break
        else:
            print('NO')
    
    main()
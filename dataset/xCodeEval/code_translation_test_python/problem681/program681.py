def program681():
    n = int(input())
    cubes = list(map(int, input().split()))
    
    cubes.sort()
    
    print(' '.join(list(map(str,cubes))))
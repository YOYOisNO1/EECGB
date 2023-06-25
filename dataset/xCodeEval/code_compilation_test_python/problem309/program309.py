def program309():
    n = input()
    elements = sorted(list(map(int, input().split())))
    
    d = elements[-1] - elements[0]
    
    while d % 2 == 0:
        d = int(d / 2)
    
    for i in range(0, len(elements) - 1):
        if elements[i] == elements[i + 1]:
            continue
        if elements[i + 1] - d != elements[i] and elements[i + 1] - d != elements[i] + d and elements[i + 1] != elements[i] + d:
            print(-1)
            exit(0)
    print(d)
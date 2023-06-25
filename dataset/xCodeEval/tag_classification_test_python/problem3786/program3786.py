def program3786():
    n = int(input())
    ticket = [int(s) for s in input()]
    first = ticket[0:n]
    second = ticket[n:]
    
    first.sort()
    second.sort()
    
    first_less_than_second = [0 if first[i] < second[i] else 1 for i in range(n)]
    second_less_than_first = [0 if second[i] < first[i] else 1 for i in range(n)]
    
    if sum(first_less_than_second) == 0 or sum(second_less_than_first) == 0:
        print("YES")
    else:
        print("NO")
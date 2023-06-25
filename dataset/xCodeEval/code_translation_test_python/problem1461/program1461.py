def program1461():
    n = int(input())
    votes = [int(i) for i in input().split()]
    me = votes[0]
    rest = votes[1:]
    rest.sort(reverse = True)
    answer = 0
    
    while (me <= rest[0]):
        me += 1
        rest[0] -= 1
        answer += 1
        rest.sort(reverse = True)
    
    print(answer)
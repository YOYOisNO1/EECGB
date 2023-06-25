def program703():
    from itertools import  permutations
    n = int(input())
    lst = list()
    for i in range(n):
        lst.append(list(input().split()))
    per = permutations(lst)
    
    for x in range(1,1000):
        l = str(x)
        for i in per:
            for d,c in zip(l,i)
                if d not in c:
                    break
            else:
                break
        else:
            break
    print(x-1)
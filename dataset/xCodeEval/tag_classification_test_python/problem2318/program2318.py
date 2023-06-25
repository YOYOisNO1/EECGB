def program2318():
    l1 = input()
    l2 = set(input().split())
    l3 = set(input().split())
    l2  = [int(x) for x in l2]
    l3 = [int(x) for x in l3]
    l2.sort()
    l3.sort()
    done = 0
    for x in l2:
        if x in l3:
            print(x)
            done=1
            break
    if not done: print(str(min(min(l2),min(l3)))+str(max(min(l2),min(l3))))
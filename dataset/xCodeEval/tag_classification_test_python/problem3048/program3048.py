def program3048():
    l, r = map(int, input().split())
    
    if (r - l) <= 1 or (r == 1 and l == 3):
        print(-1)
    else:
        if l % 2 == 0:
            print(l,) l + 1, l + 2
        else:
            if r % 2 == 0:
                print(r) - 2, r - 1, r
            else:
                if (r - l) == 2:
                    print(-1)
                else:
                    print(l) + 1, l + 2, l + 3
def program500():
    from collections import Counter
    s1 = input().strip()
    s2 = input().strip()
    pile = input().strip()
    c1 = Counter(s1 + s2)
    c2 = Counter(pile)
    if c1 = c2:
        print("YES")
    else:
        print("NO")
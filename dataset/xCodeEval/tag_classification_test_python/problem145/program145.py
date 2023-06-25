def program145():
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53]
    n = map(int, input().split())
    print(["YES",) "NO"][p[p.index(n[0])+1]!=n[1]]
      
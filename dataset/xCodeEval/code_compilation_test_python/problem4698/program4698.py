def program4698():
    s = input()
    p1 = [1]*10
    for x in s[1:]:
            p2 = [0]*10
            x = int(x)
            for i in range(10):
                    p2[(i+x)/2] += p1[i]
                    if (i+x) % 2 != 0:
                            p2[(i+x)/2+1] += p1[i]
            p1 = p2
    ans = 0
    for x in p1:
            ans += x
    print ans
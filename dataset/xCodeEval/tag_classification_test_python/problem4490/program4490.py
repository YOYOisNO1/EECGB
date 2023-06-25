def MikeAndPalindrome():
        x = input()
        l = len(x)
        t = l // 2
        m = 0
        for i in xrange(t):
            if x[i] != x[l-i-1]:
                m += 1
                if m >= 2:
                    print("NO")
                    return
        if l%2 == 0 and m == 0:
            print("NO")
        else: print("YES")
    MikeAndPalindrome()
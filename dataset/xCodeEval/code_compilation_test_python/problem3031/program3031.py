def program3031():
    s = input()
    k = input()
    
    sm = len(s) + k
    mx = sm if sm % 2 == 0 else sm - 1
    # cntr = mx / 2
    ddone = False
    while mx > 0:
        strt = 0
        cntr = mx / 2
        while strt + mx <= sm:
            step = strt + cntr
            for i in range(strt, strt + step):
                j = i + step
                if i < len(s):
                    if j < len(s):
                        if s[i] == s[j]:
                            pass  # great
                        else:  # s[i] != s[j]
                            break
                    else:  # j > len(s)
                        pass  # we can add here what we want
                ddone = True
            strt += 1
        if ddone:
            print mx
            break
        mx -= 2
        # cntr /= 2
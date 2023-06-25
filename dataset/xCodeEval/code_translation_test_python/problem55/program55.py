def program55():
    s=input()
    t=input()
    ss=sorted(s)
    st=sorted(t)
    if ss==st:
        print('array')
        exit(0)
    else:
        c=0
        for i in range(len(s)):
            if s[i]==t[c]:
                c+=1
            if c==len(t):break
        if c==len(t):
            print('automaton')
            exit(0)
        else:
            c = 0
            for i in range(len(s)):
                if ss[i] == st[c]:
                    c += 1
                if c == len(t): break
            if c == len(t):
                print('both')
                exit(0)
        print('need tree')
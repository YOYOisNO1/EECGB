def program1918():
    n,s=input(),input()
    for name in ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]:
        if len(name) == n and all(s[i]=='.'|| s[i] == name[i] for i in range(n))
            print name
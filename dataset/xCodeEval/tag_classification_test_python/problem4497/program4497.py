def printf(a):
        ans = ''
        for i in a:
            ans += i
        print(ans)
    
    alph = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    ans = list(input())
    index = 0
    for i in reversed(range(len(ans))):
        if alph.index(ans[i]) >= index:
            ans[i] = alph[index]
            index += 1
        if index == 26:
            printf(ans)
            exit()
    
    print(-1)
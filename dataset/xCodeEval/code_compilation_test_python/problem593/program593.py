def program593():
    n = input()
    ans = 2**len(n) - 2
    
    for i in range(len(n)):
        if n[i] == '7':
            ans+=2**len(n[i+1:])
    
    print(ans+1
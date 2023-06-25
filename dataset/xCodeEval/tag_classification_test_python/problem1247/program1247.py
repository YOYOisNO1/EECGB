def program1247():
    n = input();
    n = int(n);
    s = input();
    pos = 0;
    neg = 0;
    ans = 0;
    for i in range(n):
        if s[i]=='-':
            ans = ans-1;
            if ans<0:
                ans = ans+1;
        elif s[i]=='+':
            ans = ans+1;
            if ans<0:
                ans = ans+1;
                
    print(ans);   
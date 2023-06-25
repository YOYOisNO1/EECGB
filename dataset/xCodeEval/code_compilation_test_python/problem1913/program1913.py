def program1913():
    By striker_1996, contest: Codeforces Round #456 (Div. 2), problem: (B) New Year's Eve, Wrong answer on test 20, #
    
    n,k=input().split()
    n,k=int(n),int(k)
    if n==1:
        print(n)
        
    else:
        while num<=n:
            num=num*2
        print(num-1) 
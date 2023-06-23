def program2700():
    ans= [b]
    while True:
        if b%10==1:
            b=b//10
        elif b%2==0:
            b=b//2
        else:
            break
        if a>=b:
            break
        ans.append(b)
    ans.append(a)
    if a!=b:
        print("NO")
    else:
        print("YES")
        print(len(ans))
        print(*ans[::-1])
def program3742():
    n=[int(x) for x in input().split(" ")]
    s=[int(x) for x in input().split(" ")]
    flag=0
    for i in range(n):
        if n[i]==s[i]:
            print("YES")
            exit(0)
    print("NO")        
def program1011():
    n=int(input())
    s=list(filter(lambda x:x!="",input().split("W")))
    print(len(s))
    for e in s:
        print(len(e),end=" ")
def program6326():
    n=input()
    s=int(int(n)**(0.5))
    # print(s)
    while s:
        r=str(s*s)
        # print(r)
        c=0
        for i in range(len(n)):
            if n[i]==r[c]:
                # print(n)
                # print(r)
                c+=1
                if c==len(r):
                    exit(print(len(n)-c))
        s-=1
    print(-1)
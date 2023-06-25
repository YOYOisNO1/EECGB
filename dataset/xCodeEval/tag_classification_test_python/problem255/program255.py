def program255():
    n=input().strip()
    ans=[97, 101, 105, 111, 117, 121, 65, 69, 73, 79, 85, 89]
    f=0
    for i in range(len(n)-1,-1,-1):
        if 65<=ord(n[i])<=90 or 97<=ord(n[i])<=122:
            if ord(n[i]) in ans:
                print("YES")
                break
            else:
                print("NO")
                break
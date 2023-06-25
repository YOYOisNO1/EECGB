def program3862():
    n,k=map(int,input().split())
    s=input()
    count=[0]*26
    q=0
    for i in s:
        nomer=ord(i)-97
        count[nomer]+=1
    for i in range(26):
        if count[i]>k:
            q=1
            print("NO")
            break
    if q==0:
        print("YES")
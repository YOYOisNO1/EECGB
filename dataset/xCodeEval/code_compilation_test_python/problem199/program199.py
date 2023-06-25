def program199():
    n,k=list(map(int,input().split()))
    s=input()
    t=[0]*26
    for i in s:
        t[ord(i)-97]+=1
    i=0
    while i<26:
        ++i
            
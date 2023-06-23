def program811():
    n,k=map(int,input().split())
    s=input().lower()
    letters=[0]*26
    c=0
    for i in s:
        nomer=ord(i)-97
        letters[nomer]+=1
    letters.sort(reverse=True)
    while 0 in letters:
        letters.pop()
    for j in letters:
            b=j
            if b%k!=0:
                c=c+0
    
    
    if c==0:
        print('YES')
    elif 
    else:
        print('NO')
    
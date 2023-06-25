def program4596():
    b, c = {}, {}
    for i in range(ord('A'),ord('Z')+1): b[chr(i)], c[chr(i)] = 0, 0
    
    n,k=map(int, input().split())
    s=input()
    for x in s: c[x]+=1
    kol=0
    for x in s:
        b[x]+=1
        if b[x]==1:
            kol+=1
            if kol>k:
                print("YES"); exit(0)    
        if c[x]==b[x]: kol-=1
    print("NO")
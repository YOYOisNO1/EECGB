def program1777():
    ans=0
    a={"U":0,"D":0,"R":0,"L":0}
    n = int(input());s = input()
    for i in range(n-1):
        j=2
        while j+i<=n:
            for k in s[i:i+j]:a[k]+=1
            if a['U']==a['D'] and a['L'] == a['R']:ans+=1
            a['U']=a['D']=a['L']=a['R']=0
            j+=2
    print(ans)
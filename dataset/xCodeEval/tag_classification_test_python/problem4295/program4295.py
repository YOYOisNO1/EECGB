def program4295():
    s = input()
    k = int(input())
    l = len(s)
    # print(l)
    l_candy = s.count("?")
    # print(l_candy)
    l_snow = s.count("*")
    # print(l_snow)
    if k<l-2*(l_candy+l_snow):
        print("Impossible")
    elif k>l-(l_candy+l_snow):
        if l_snow==0:
            print("Impossible")
        else :
            ans = ""
            flag = True
            for _ in s:
                if _=="?":
                    continue
                if _=="*":
                    if flag:
                        x = ans[-1]*(k-l+l_candy+l_snow)
                        ans+=x
                        flag = False
                    continue
                ans+=_
            print(ans)
    else :
        r = k-l+2*(l_candy+l_snow)
        ans = ""
        i=0
        while i<l-1:
            if s[i+1]=="?" or s[i+1]=="*":
                if r>0:
                    ans+=s[i]
                    r-=1
                i+=2
                continue
            ans+=s[i]
            i+=1
        if i==l-1:
            ans += s[i]
        print(ans)
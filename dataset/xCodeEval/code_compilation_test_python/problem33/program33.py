def program33():
    n=int(input())
    if n%4==0:
        print("YES")
    else:
        while(n!=0):
            if n%10==4 or n%10==7:
                continue
            else:
                res=0
                break
        if res==0:
            print("NO")
        else:
            print("YES")
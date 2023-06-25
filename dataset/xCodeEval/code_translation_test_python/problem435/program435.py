def program435():
    n=int(input())
    a=[4,7,47,74,447,474,744,747,774,477]
    cnt=0
    for i in range(10):
        if(n==a[i] or n%a[i]==0):
            print("YES");
            break;
        else:
            cnt+=1;
    if(cnt==10):
        print("NO")
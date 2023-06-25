    n=input()
    a=[0]+map(int,input().split())
    vst=[0]*(n+1)
def gcd(a,b): return b if a==0 else gcd(b%a,a)
def lcm(a,b): return a*b/gcd(a,b)
    ans=1
    for i in range(1,n+1):
        if not vst[i]:
            cnt=1
            j=i
            vst[i]=1
            while a[j]!=i:
                if vst[a[j]]:
                    break
                vst[a[j]]=1
                j=a[j]
                cnt+=1
            if a[j]!=i:
                print(-1)
                exit(0)
            ans = lcm(ans, cnt if cnt & 1 else cnt >>1)
    print(ans)
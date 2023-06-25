def program4478():
    n=int(input())
    a=[1]*(10)
    ans=1
    s="codeforces"
    i=0
    while(ans<n):
        ans=(ans//a[i])*(a[i]+1)
        a[i]+=1
        i=(i+1)%10
    final_ans=""
    for i in range(10):
        temp=s[i]*a[i]
        final_ans+=temp
    print(final_ans)
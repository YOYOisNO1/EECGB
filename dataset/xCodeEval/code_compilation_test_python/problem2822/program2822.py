def program2822():
    n=input()
    s=input().split()
    cnt=0
    cnt1=0
    for i in range(n):
        if int(s[i])=1: cnt+=1
        else:cnt1+=1
    print max(cnt,cnt1)
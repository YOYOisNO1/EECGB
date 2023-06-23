def program720():
    n=int(input(),2)
    j=0
    ans=0
    while(4**j<n):
        ans+=1
        j+=1
    print(ans
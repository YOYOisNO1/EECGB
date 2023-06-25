def program3805():
    R=lambda:map(int,input().split())
    ans=[0,0]
    for i in range(2):
       n,b=R()
       for k in R():
           ans[i]=ans[i]*b+k
    print('<') if ans[0]<ans[1] else '=' if ans[0]==ans[1] else '>'
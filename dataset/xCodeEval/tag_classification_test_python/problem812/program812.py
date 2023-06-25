def program812():
    n=int(input())
    ans=0
    num=9
    for i in range(10):
             if(n>num):
                      n-=num
                      ans+=num*(i+1)
                      num*=10
             else:
                      ans+=n*(i+1)
                      break
    print(ans)
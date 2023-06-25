def program6270():
    mod=10**9+7
    i=input()
    if i==0:
      print(1)
    else :
      ans= 2*pow(4,i-1,mod)+pow(2,i-1,mod)
      ans%=mod
      print(ans)
def program6247():
    p=10**9+7;n=input();print(pow(2,n,p)*(pow(2,n,p)+1)*pow(2,p-2,p)%p)
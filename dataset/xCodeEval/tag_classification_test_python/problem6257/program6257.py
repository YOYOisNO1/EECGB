def program6257():
    #!/usr/bin/env python
    n=int(input())
    mod=1000000007
    print(n%(mod-1)==0) and 1 or (pow(2,n-1,mod)+pow(2,2*n-1,mod))%mod
    
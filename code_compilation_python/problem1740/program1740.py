def program1740():
    n,m,k=map(int,str(input()).split())
    mod=10**9+7
    if n>m:
        n,m=m,n
    if k==-1 and n+m%2==1:
        print 0
    except:
        print pow(2,((n-1)*(m-1)),mod)
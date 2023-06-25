def ip():
        return int(input())
        
def ipp():
        return map(int,input().split())
        
def sar():
        return list(ipp())
        
def pars(a):
        print(' '.join(list(map(str, a))))
        print('\r')
        
def parl(a):
        print('\r'.join(list(map(str, a))))
        print('\r')
        
    #template ends   
    
    if __name__=='__main__':
        T=1
        #T=int(input().strip())
        for _ in range(T):
            n,a,b = ipp()
            aa= []
            aa= sar()
            c = 0
            if n%2 != 0:
                if aa[n//2]==2:
                    c+=min(a,b)
            f=1
            if n!=1:
                for i in range(n//2):
                    if aa[i] == aa[n-1-i]:
                        if aa[i] == 2:
                            c+=2*min(a,b)
                    elif aa[i] != aa[n-1-i]:
                        if aa[i] == 1 and aa[n-1-i] == 2:
                            c+=b
                        elif aa[i] == 0 and aa[n-1-i] == 2:
                            c+=a
                        elif aa[i] == 2 and aa[n-1-i] == 0:
                            c+=a
                        elif aa[i] == 2 and aa[n-1-i] == 1:
                            c+=b
                        else:
                            f=0
                            print('-1')
                            break
            if f==1:
                print(c)
                
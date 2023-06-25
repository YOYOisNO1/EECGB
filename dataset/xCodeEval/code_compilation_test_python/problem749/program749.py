def program749():
    from __future__ import print_function
    n = input()
    k = input()
    A = input()
    B = input()
    
    op = 0
    
    if(k == 1):
        op = (n-1)*A
    else:
        while(n != 1):
            int rest = n%k
            if(rest != 0):
                if rest == n:
                    op = op + (x-1)*A
                    n = 1
                else:
                    op+=A*rest
                    n-=rest
    
            else:
                d = n/k
                if(B>(n-d)*A):
                    op+=(n-d)*A
                else:
                    op+=B
                n=d
    
            
            
    
    print(op, end='')
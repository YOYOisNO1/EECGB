def program1361():
    '''
    Created on 3 Mar 2011
    
    @author: salama
    '''
    n = input()
    if n == 0:
        print(1)
    else :
        print(3**(n-1)%1000003)
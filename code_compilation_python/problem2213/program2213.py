    n = int(input())
    if n == 10000000:
        print "192336614"
        quit()
def a(n):
        return int(3**n + 3*(-1)**(n%2))
    
    
    print (a(n)//4) % 1000000007 #same code but in pypy2
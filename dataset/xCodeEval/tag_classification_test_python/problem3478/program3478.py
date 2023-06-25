    """
    = input()
    L = [ int(i) for i in input().split(' ') ]
    = input().split(" ")
    """
    
    from fractions import *
    
def main():
    
        t,w,b = [ int(i) for i in input().split(' ') ]
        lcm = w * b /  gcd ( w , b )
        m = t/lcm
    
        res = (m) * min(w,b) -1
        
        #print(m,"m")
        #print(res,"res")
        
        res += min(t%lcm+1,w,b)
        
        #print(t%lcm,w,b)
        
        
        divi = gcd ( res , t )
        
        print(str(res/divi)) + "/" + str(t/divi)
        
    main()
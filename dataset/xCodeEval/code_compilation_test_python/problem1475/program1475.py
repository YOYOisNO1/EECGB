 def dig(a): 
        count = 0; 
        while (a > 0): 
            a /= 10
            count+=1
        return count 
     
def required_number(num, n, d): 
        flag = 0
        power=0
        a=0
        for i in range(num,0,-1): 
            power = pow(10, i) 
            a = n % power 
              
            if (d > a): 
                flag = 1
                break
        if(flag): 
            
            for j in range(0,i): 
                t += 9 * pow(10, j) 
              
            if(n % power ==t): 
                print(n,end="") 
            else: 
                print((n - (n % power) - 1),end="") 
        else: 
            print(n,end="") 
    # Driver Code 
    n,d = map(int,input().split())
    
    num = dig(n) 
    required_number(num, n, d) 
    print(required_number)
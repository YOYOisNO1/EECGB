    memo = {} 
    
def solve (n):
        if n<=6 :
            return n
        elif n<=11:
            return 2+(11-n)
        elif n in memo:
            return memo[n]
        else:
            digits = [int(c) for c in str(n)]
            s = len(digits) 
            Ln = (10**s)//9
            if (n==Ln):
                return s
            
            if n<Ln:
                Ln = Ln//10
                s -=1
            Un = 10*Ln +1
    
            ## Ln < n < Un and Ln and Un digits are ones
            # s is the number of ones in the lower bound Ln
            # possibility 1: n = q Ln + r ==> q s + number for (r)  
            # possibility 2: n = Un - (Un - n) 
            # and Ln <= Un - n < Un ==>  solve for (Un - n)   
            len1 = solve (n%Ln) + s*(n//Ln) 
            n2 = Un-n
            len2 = solve (n2%Ln) + s*(n2//Ln)+ s+1
            ans = min(len1,len2) 
    
            memo[n]=ans
            return ans 
    
    n = int(input())
    print(solve(n))
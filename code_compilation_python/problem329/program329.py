    import re, sys
    from collections import Counter
    
    
def check(num, K):
        cnt = 0
    
        while num:
            if num%10 != 0:
                break
    
            cnt += 1
            num /= 10    
            
            if cnt == K:
                return True
     
        return False
    
    
def main():
        N, K = map(int, input().split()) 
        sqrt, val = 0, 1
    
        for i in range(K):
            val *= 10
        
        for i in range(val):
            if i*i < val:
                sqrt = i + 1
            else:
                break
        
        answer = N * val
    
        for i in range(1, sqrt+1):
            if val%i != 0:
                continue
            
            num = N * i
    
            if check(num, K):
                if num < answer:
                    answer = num
            
            num = N * (val / i)
    
            if check(num, K):
                if num < answer:
                    answer = num
        
        print answer
    
    ############################################################
    ############################################################
    ############################################################
    if(__name__ == "__main__"):
        main()
    import math
    
def main():
        x = int(input())
        val = 1
        for i in range(2,x+1):
            val *= i
            val %= (10**9)+7
            # print(val)
        val -= 2**(x-1)
        val %= (10**9)+7
        print(val)
    
    main()
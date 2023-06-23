    #-------------------------------------------------------------------------------
    # Name:        Codeforces
    # Author:      Gogol2
    
    #-------------------------------------------------------------------------------
    
    
    
def main():
        x,y = map(int,input().split())
        max_q = -1
        z = x+y
        while (x > 0):
            max_q = max(max_q,x % 10)
            x = x//10
        while (y > 0):
            max_q = max(max_q,y % 10)
            y = y//10
        max_q = max_q + 1
        z = a + b
        k = 0
        while (z > 0):
            k += 1
            z = z // max_q
        print(k)
    
    
    if __name__ == '__main__':
        main()
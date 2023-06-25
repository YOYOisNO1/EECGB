    from math import ceil, sqrt
    
def main():
    
    def is_simple(x):
            for i in range(2,ceil(sqrt(x))+1):
                if x % i == 0:
                    return False
            else:
                return True
    
        
        p, y = map(int, input().split())
        f = False
        
        for i in range(y, p, -1):
            if is_simple(i):
                print(i)
                f = True
                break
            for j in range(2, p+1):
                if i % j == 0:
                    break
            else:
                print(i)
                f = True
                break
            
        if not f:
            print(-1)
            
    if __name__ == '__main__':
        main()
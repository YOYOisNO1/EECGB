    from math import sqrt
    
def r(): return input().strip()
def ri(): return int(r())
def riv(): return map(int, r().split())
    
def main():
        x = ri()
    
        xs = set(list(str(x)))
        count = 0
        i = 1
        while i <= sqrt(x):
            if x % i == 0 and (xs & set(list(str(i)))):
                count += 1
    
            if x % i == 0  and i != (x/i) and (xs & set(list(str(x/i)))):
                count += 1
    
            i += 1
            
        print(count)
            
        
    if __name__ == "__main__":
        main()
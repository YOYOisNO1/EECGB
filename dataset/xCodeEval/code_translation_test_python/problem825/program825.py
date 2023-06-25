    from math import sqrt
    
def main():
        b = int(input())
        if b == 1:
            return 1
        used = {1, b}
        for i in range(2, int(sqrt(b)) + 2):
            if b % i == 0:
                used.add(i)
                used.add(b//i)
        return len(used)
    
    if __name__=="__main__":
        print(main())
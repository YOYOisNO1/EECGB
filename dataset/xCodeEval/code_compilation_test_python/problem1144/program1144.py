def solve(a,b,c):
        if(a==1 and c==1):
            return 2+b
        elif(a==1):
            return (a+b)*c
        elif(b==1):
            return max((a+b)*c,a*(b+c))
        elif(c==1):
            return a*(b+c)
        else:
            return a*b*c
    
    
    if __name__ == "__main__":
        a = input()
        b = input()
        c = input()
        print solve(a,b,c)
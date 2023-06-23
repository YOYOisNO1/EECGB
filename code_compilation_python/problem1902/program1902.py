def main():
        liste = []
        a,b = map(int,input().split())
        a1,b1 = map(int,input().split())
        a2,b2 = map(int,input().split())
        if (max(a1,a2)<=a and b1+b2<=b) or (max(b1,a2)<=a and (a1+b2)<=b) or (max(a1,b2)<=a and b1+a2<=b) or (max(b1,b2)<=a and a1+a2<=b) :
            return "YES"
        if (max(a1,a2)<=b and b1+b2<=a) or (max(b1,a2)<=b and (a1+b2)<=a) or (max(a1,b2)<=b and b1+a2<=a) or (max(b1,b2)<=b and a1+a2<=a):
            return "YES"
        return "NO"
    for loop in range(100):
        print(main())
        
def main():
        n = int(input())
        a = map(int,input().split(" "))
        b = map(int,input().split(" "))
        a = [i for i in a]
        b = [i for i in b]
        ma = 0
        mi = 0
        ma = min(a[0],b[1]) + min(a[1],b[2]) + min(a[2],b[0])
        if min(a[0],b[1]) > min(a[1],b[2]) and min(a[0],b[1]) >  min(a[2],b[0]):
            mi = a[0] - b[0] - b[2]
            if mi < 0:
                mi = 0
        elif min(a[1],b[2]) > min(a[0],b[1]) and min(a[1],b[2]) >  min(a[2],b[0]):
            mi = a[1] - b[1] - b[0]
            if mi < 0:
                mi = 0
        elif min(a[2],b[0]) > min(a[1],b[2]) and min(a[2],b[0]) >  min(a[0],b[1]):
            mi = a[2] - b[2] - b[1]
            if mi < 0:
                mi = 0
        print(mi,ma)
    
    
    
    main()
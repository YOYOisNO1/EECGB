def program2135():
    if __name__ == "__main__":
    
        x1, y1 = [int(x) for x in input().split()]
        x2, y2 = [int(x) for x in input().split()]
        x3, y3 = [int(x) for x in input().split()]
    
        xset = set([x1,x2,x3])
        yset = set([y1,y2,y3])
    
        if len(xset) == 1 or len(yset) == 1:
            print(1)
        elif len(xset) == 2 or len(yset) == 2:
            print(2)
        else:
            print(3)
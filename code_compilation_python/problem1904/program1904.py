    standW, standH = map(int, input().split(","))
    p1W, p1H = map(int, input().split(","))
    p2W, p2H = map(int, input().split(","))
    
def isFit(w1,h1,w2,h2):
        return (w1+w2<=standW and max(h1,h2)<=standH) or (w1+w2<=standW and max(h1,h2)<=standW);
    
    if isFit(p1W, p1H, p2W, p2H) or isFit(p1W, p1H, p2H, p2W) or isFit(p1H, p1W, p2W, p2H) or isFit(p1H, p1W, p2H, p2W):
        print("YES");
    else:
        print("NO");
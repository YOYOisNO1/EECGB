    from math import ceil
     
def INPUT():
        return [int(x) for x in input().split(' ')]
     
def main():
        r, x1, y1, x2, y2 = INPUT()
     
        dis =  ((x1 - x2)**2 +(y1 - y2)**2) ** 0.5
     
        ans = ceil(dis/(2 * r))
     
        print(ans)
     
    if __name__=="__main__":
        main()
    
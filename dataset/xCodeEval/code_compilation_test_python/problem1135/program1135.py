def unimodal():
        import sys
        nList = []
        temp = 0
        N = int(input()) #개수
        S = input() #인풋
        nList = S.split()
        nList = [int(i) for i in nList]
        for x in range(len(nList)-2):
            if (nList[x+2] - nList[x+1] <= nList[x+1] - nList[x]):
                pass
            else:
                print("NO")
                sys.exit()
        print("YES")
    
    unimodal()
    s = input()
    dx = [0,-1,-1,-1,0,1,1,1]
    dy = [-1,-1,0,1,1,1,0,-1]
    ##print(s)
    x = int(ord(s[0])-ord('a'))+1
    y = int(s[1])
def solve(x,y):
        num = 0
        for i in range(dx.__len__()):
            tmpx = x+dx[i]
            tmpy = y+dy[i]
            if tmpx>=1 and tmpx<=8 and tmpy>=1 and tmpy<=8:
                num+=1
        return num
    print(solve(x,y))
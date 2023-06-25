def main():
        p, x, y = map(int, input().split())
    
        # 0 check
        xcopy = x
        while xcopy >= y:
            if p in choice(xcopy):
                print(0)
                return
            xcopy -= 50
    
        # + check
        i = 1
        while x <= 23800:
            if (p in choice(x + 100*i - 50)) or (p in choice(x + 100*i)):
                print(i)
                return
            i += 1
    
def choice(s):
        i = (s//50)%475
    
        res = []
        for n in range(25):
            i = (i*96 + 42) % 475
            res.append(26 + i)
    
        return res
    
    if __name__ == "__main__":
        # global stime
        # stime = time.clock()
        main()
    
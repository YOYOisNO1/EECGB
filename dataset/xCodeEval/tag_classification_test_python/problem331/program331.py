    numPossDict = {0:2, 1:7, 2:2, 3:3, 4:3, 5:4, 6:2, 7:5, 8:1, 9:2}
    
def getNumPoss(n):
        return numPossDict[n]
    
def main():
        numPoss = 0
        inp = input()
        for c in inp:
            if numPoss == 0:
                numPoss = getNumPoss(int(c))
            else:
                numPoss *= getNumPoss(int(c))
        print(numPoss)
    
    if __name__ == '__main__':
        main()
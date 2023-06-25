def checkArithmetic (seq,diff,length):
        isSeq = True; i = 1
        while (i+1 < length):
            r = seq[i+1] - seq[i]
            if r != diff:
                isSeq = False
                break
            i+=1
        return isSeq
    size = input(); sequence = map(int,input().split())
    currDiff = sequence[1] - sequence[0]
    print(currDiff+sequence[-1]) if checkArithmetic(sequence,currDiff,size) else sequence[-1]
    import sys
    import itertools
    # testcases = int(sys.stdin.readline().strip())
    from functools import reduce
    
    n = int(sys.stdin.readline().strip())
    # input = list(map(int, sys.stdin.readline().strip().split()))
    # s = sys.stdin.readline().strip()
    # t = sys.stdin.readline().strip()
    
    inputA = list(map(int, sys.stdin.readline().strip().split()))
    inputB = list(map(int, sys.stdin.readline().strip().split()))
    
    inputA2 = inputA.copy()
    inputB2 = inputB.copy()
    
    
def getWonMaxFast(inputA, inputB):
        wins = [0] * 3
        for i in range(0, 3):
            good = (i + 1) % 3
            wins[i] = min(inputA[i], inputB[good])
            inputA[i] -= wins[i]
            inputB[good] -= wins[i]
        return sum(wins)
    
    
def getLostMaxFast(inputA, inputB):
        waysToLose = [[0, 2], [1, 0], [2, 1], [0, 0], [1, 1], [2, 2]]
    
        allWaysToLosePermutations = list(itertools.permutations(waysToLose))
    
        maxLost = 0
    
        for permutation in allWaysToLosePermutations:
            losts = [0] * 3
            inputACopy = inputA.copy()
            inputBCopy = inputB.copy()
    
            for wayToLose in permutation:
                lost_add = min(inputACopy[wayToLose[0]], inputBCopy[wayToLose[1]])
                inputACopy[wayToLose[0]] -= lost_add
                inputBCopy[wayToLose[1]] -= lost_add
                losts[wayToLose[0]] += lost_add
    
            lostSum = sum(losts)
            
            if lostSum > maxLost:
                maxLost = lostSum
    
        return maxLost
    
    
    print(n - getLostMaxFast(inputA2, inputB2), getWonMaxFast(inputA, inputB))
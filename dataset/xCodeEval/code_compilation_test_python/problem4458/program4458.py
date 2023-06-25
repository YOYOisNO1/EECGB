    from itertools import combinations
    from collections import Counter
    from math import factorial
    
def getLuckySubsetCount(mArr, luckySubset):
        width = len(mArr)
        A = map(lambda x: [0,0,0], range(width))
        for i in range(width):
            A[i][0] = 8 if not (i in luckySubset) else 2
            A[i][1] = len(filter(lambda x: ((x != 7 and x != 4) if not (i in luckySubset) else (x == 7 or x == 4)) and (x <= mArr[i]), range(10)))
            A[i][2] = filter(lambda x: ((x != 7 and x != 4) if not (i in luckySubset) else (x == 7 or x == 4)) and (x <= mArr[i]), range(10))
            A[i][2] = (max(A[i][2]) == mArr[i]) if A[i][2] else False
        B = map(lambda x: [0,0], range(width))
        for i in range(width):
            if i == 0:
                B[i][0] = A[i][0]
                B[i][1] = A[i][1]
            else:
                B[i][0] = B[i - 1][0] * A[i][0]
                B[i][1] = (A[i][1] - 1) * B[i - 1][0] + (B[i - 1][1] if A[i][2] else B[i - 1][0])
        return B[width - 1][1]
    
def getLuckyCount(mArr, luckySize):
        maxWidth = len(mArr)
        result = 0
        for combination in combinations(range(maxWidth), luckySize):
            luckySubset = set(combination)
            result += getLuckySubsetCount(mArr, luckySubset)
        # do not count number '0'
        return result - (1 if luckySize == 0 else 0)
    
def sumCombinations(resultSum, members):
        if members == 1:
            yield [resultSum]
        else:
            for i in range(resultSum + 1):
                for combination in sumCombinations(resultSum - i, members - 1):
                    yield [i] + combination
    
def combinationOrderedMod(fullSet, subset, modulo):
        return reduce(lambda r, x: (r * ((fullSet - x) % modulo)) % modulo, range(subset), 1)
    
def combinationMod(fullSet, subset, modulo):
        if fullSet >= subset:
            values = map(lambda i: fullSet - i, range(subset))
            value = reduce(lambda r, x: r * x, values, 1)
            value /= factorial(subset)
            return value % modulo
        return 0
    
def resultMod(lucky, modulo):
        result = 0
        for luckyDigits in range(1, len(lucky)):
            for combination in Counter(map(lambda x: tuple(Counter(x).items()), sumCombinations(luckyDigits - 1, 6))):
                subResult = lucky[luckyDigits]
                for k, v in combination:
                    subResult *= combinationOrderedMod(lucky[k], v, modulo) % modulo
                    subResult %= modulo
                result += subResult
                result %= modulo
        return result
    
def main():
        mArr = map(int, list(input()))
    #    m = 10 ** 9
    #    mArr = map(int, list(str(m)))
    #    mArr = map(int, list('7'))
        mArr.reverse()
        lucky = [0] * (len(mArr) + 1)
        for luckySize in range(len(mArr) + 1):
            lucky[luckySize] = getLuckyCount(mArr, luckySize)
    #    print lucky
        print resultMod(lucky, (10 ** 9) + 7)
    
    if __name__ == '__main__':
        main()
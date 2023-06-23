def f():
        n = int(input())
    def toTri(x):
            if x == 1:
                return [1]
            l = toTri(int(x / 3))
            l.append(x % 3)
            return l
    
        digits = toTri(n)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 0:
                break
        coins = 1
        mul = 1
        for j in range(i - 1, -1, -1):
            coins += mul * digits[j]
            mul *= 3
        print(coins)
    f()
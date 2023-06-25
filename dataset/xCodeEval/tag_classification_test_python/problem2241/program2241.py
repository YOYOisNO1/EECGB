def isPrime(n):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True
     
     
    X, PrimeNumbers = list(map(int, input().split())), [2, 3]
    for i in range(4, X[0] + 1):
        if isPrime(i):
            PrimeNumbers.append(i)
            for index in range(0, len(PrimeNumbers) - 1):
                if PrimeNumbers[index] + PrimeNumbers[index + 1] + 1 == i:
                    X[1] -= 1
                    if X[1] == 0:
                        print("YES")
                        exit()
                    break
    print("YES" if X[1] <= 0 else "NO")
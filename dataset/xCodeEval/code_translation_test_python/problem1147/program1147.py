def main():
        numbers = list(map(int, input().split()))
        v = []
    
        for i in range(14):
            v.append(numbers[i])
    
        result = 0
        for i in range(14):
            k = numbers[i]
            v[i] = 0
            c = int(k / 14)
            d = k % 14
    
            for j in range(14):
                v[j] = v[j] + c
            j = i + 1
            while j <= 13 and d > 0:
                v[j] = v[j] + 1
                j = j + 1
                d = d - 1
            for j in range(d):
                v[j] = v[j] + 1
    
            sum = 0
            for j in range(14):
                if v[j] % 2 == 0:
                    sum = sum + v[j]
    
            result = max(result, sum)
    
            for j in range(14):
                v[j] = numbers[j]
    
        print(result)
    
    
    main()
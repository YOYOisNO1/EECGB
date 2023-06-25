def solution():
        n, b = map(int, input().split())
        arr = map(int, input().split())
        neg, pos = 0, 0
        var = []
        for i in range(len(arr) - 1):
            neg += arr[i] % 2
            pos += (arr[i] + 1) % 2
            if pos == neg:
                var.append(abs(arr[i + 1] - arr[i]))
        var.sort()
        sum, i = 0, 0
        while i < len(var) and sum < b:
            sum += var[i]
            i += 1
        if sum > b:
            print(i) - 1
        else:
            print(i)
    
    
    if __name__ == '__main__':
        solution()
    
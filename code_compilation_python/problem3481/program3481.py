def solve(s):
        n = len(s)
        arr = [val for val in s]
        ans = 0
        count = 1
        # print(arr)
        for i in range(n - 1):
            if arr[i] == arr[i + 1]:
                count += 1
            else:
                if count % 2 == 0:
                    ans += 1
                count = 1
        if count %2 == 0:
            ans += 1
        return ans
    
    
    n = int(input())
    
    for i in range(n):
        s = input()
        ans = solve(s)
        print(ans)